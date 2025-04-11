import streamlit as st
import json
import os
from datetime import datetime, time
import pandas as pd
from database_manager import add_entry as db_add_entry, delete_entry as db_delete_entry, get_data_as_dataframe as db_get_data_as_dataframe, get_entries, migrate_from_json

def initialize_session_state():
    """Initialize session state variables"""
    if 'language' not in st.session_state:
        st.session_state.language = 'kannada'  # Default language
    
    if 'form_data' not in st.session_state:
        st.session_state.form_data = {}
    
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    
    if 'form_submitted' not in st.session_state:
        st.session_state.form_submitted = False
    
    # We don't need to initialize file upload fields in session_state
    # as Streamlit manages them internally

def toggle_language():
    """Toggle between Kannada and English"""
    st.session_state.language = 'english' if st.session_state.language == 'kannada' else 'kannada'

def save_form_data():
    """Save form data to session state and database"""
    # Get all form inputs from the session state
    form_data = {k: v for k, v in st.session_state.items() if k.startswith('form_')}
    
    # Process time inputs to ensure they're stored as strings in a consistent format
    for key, value in form_data.items():
        if isinstance(value, time):
            # Format time objects as strings in 24-hour format
            form_data[key] = value.strftime("%H:%M")
    
    # Process adulteration checkboxes into a list
    adulteration_list = []
    if st.session_state.get('form_sugar_adulteration', False):
        adulteration_list.append("Sugar")
    if st.session_state.get('form_water_adulteration', False):
        adulteration_list.append("Water")
    if st.session_state.get('form_no_adulteration', False):
        adulteration_list.append("None")
    form_data['form_adulteration_details'] = adulteration_list
    
    # Clear individual checkbox fields
    if "form_sugar_adulteration" in form_data:
        del form_data["form_sugar_adulteration"]
    if "form_water_adulteration" in form_data:
        del form_data["form_water_adulteration"]
    if "form_no_adulteration" in form_data:
        del form_data["form_no_adulteration"]
    
    # Process equipment checkboxes into a list
    equipment_list = []
    equipment_keys = [k for k in list(form_data.keys()) if k.startswith("form_equipment_")]
    for key in equipment_keys:
        if form_data[key]:
            # Extract the equipment name from the key (form_equipment_lactometer -> lactometer)
            equipment_name = key.replace("form_equipment_", "")
            equipment_list.append(equipment_name)
        del form_data[key]
    form_data['form_milk_testing_equipment'] = equipment_list
    
    # Handle file upload data
    photo_fields = [
        'form_truck_sheet_photo',
        'form_challan_sheet_photo',
        'form_purchase_sheet_photo',
        'form_bmc_building_photo',
        'form_cattle_feed_storage_photo',
        'form_bmc_premises_photo',
        'form_team_visit_photo'
    ]
    
    # Remove the dry fodder usage field from form data if it exists
    if "form_dry_fodder_usage_low" in form_data:
        del form_data["form_dry_fodder_usage_low"]
    
    for field in photo_fields:
        if field in form_data and form_data[field] is not None:
            # Store the filename or a reference instead of the actual file data
            if form_data[field] is not None:
                form_data[field] = form_data[field].name
    
    # Add timestamp
    form_data['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Store in session state
    st.session_state.form_data = form_data
    
    # Save to database
    success = db_add_entry(form_data)
    
    # Set form submission flag
    st.session_state.form_submitted = success
    
    return form_data

def clear_form():
    """Clear all form data from session state"""
    for key in list(st.session_state.keys()):
        if key.startswith('form_'):
            del st.session_state[key]
    
    st.session_state.form_submitted = False

def load_data():
    """Load data from database"""
    return get_entries()

def save_data(form_data=None):
    """Save data to database (legacy function, kept for compatibility)"""
    if form_data:
        return db_add_entry(form_data)
    return True

def delete_entry(entry_id):
    """Delete an entry from the database"""
    return db_delete_entry(entry_id)

def get_data_as_dataframe():
    """Get data as pandas DataFrame from database"""
    return db_get_data_as_dataframe()

def migrate_legacy_data():
    """Migrate data from JSON file to database if it exists"""
    # Define old JSON file path
    json_file = "dairy_collection_data.json"
    
    # Check if file exists and migrate if needed
    if os.path.exists(json_file):
        st.info("Migrating legacy data from JSON to database...")
        if migrate_from_json():
            st.success("Data migration completed successfully")
            return True
        else:
            st.error("Error migrating data")
            return False
    return True

1.	visualization.py - Data visualization components
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

def plot_milk_collection_trend(df):
    """
    Plot the trend of milk collection over time
    
    Args:
        df: Pandas DataFrame with milk collection data
    """
    if 'timestamp' not in df.columns or df.empty:
        st.info("Not enough data to generate trends.")
        return
    
    # Convert timestamp to datetime
    df['date'] = pd.to_datetime(df['timestamp']).dt.date
    
    # Group by date and calculate daily totals
    if 'form_total_suppliers' in df.columns:
        daily_data = df.groupby('date')['form_total_suppliers'].sum().reset_index()
        
        # Create the figure
        fig = px.line(
            daily_data, 
            x='date', 
            y='form_total_suppliers',
            title='Daily Milk Collection Trend',
            labels={'date': 'Date', 'form_total_suppliers': 'Total Suppliers'}
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Supplier data not available for trend visualization.")

def plot_member_vs_nonmember(df):
    """
    Plot comparison between member and non-member suppliers
    
    Args:
        df: Pandas DataFrame with milk collection data
    """
    if 'form_member_suppliers' not in df.columns or 'form_non_member_suppliers' not in df.columns or df.empty:
        st.info("Member vs non-member data not available.")
        return
    
    # Calculate totals
    total_members = df['form_member_suppliers'].sum()
    total_non_members = df['form_non_member_suppliers'].sum()
    
    # Create pie chart
    fig = px.pie(
        values=[total_members, total_non_members],
        names=['Members', 'Non-Members'],
        title='Member vs Non-Member Suppliers',
        color_discrete_sequence=px.colors.sequential.Blues
    )
    
    st.plotly_chart(fig, use_container_width=True)

def plot_shift_distribution(df):
    """
    Plot distribution of milk collection by shift
    
    Args:
        df: Pandas DataFrame with milk collection data
    """
    if 'form_shift' not in df.columns or df.empty:
        st.info("Shift data not available.")
        return
    
    # Count shift distribution
    shift_counts = df['form_shift'].value_counts().reset_index()
    shift_counts.columns = ['Shift', 'Count']
    
    # Create bar chart
    fig = px.bar(
        shift_counts,
        x='Shift',
        y='Count',
        title='Milk Collection by Shift',
        color='Shift',
        color_discrete_sequence=px.colors.sequential.Viridis
    )
    
    st.plotly_chart(fig, use_container_width=True)

def plot_software_usage(df):
    """
    Plot AMCS software implementation status
    
    Args:
        df: Pandas DataFrame with AMCS data
    """
    if 'form_amcs_software_status' not in df.columns or df.empty:
        st.info("AMCS software status data not available.")
        return
    
    # Count AMCS status
    amcs_counts = df['form_amcs_software_status'].value_counts().reset_index()
    amcs_counts.columns = ['Status', 'Count']
    
    # Create horizontal bar chart
    fig = px.bar(
        amcs_counts,
        y='Status',
        x='Count',
        title='AMCS Software Implementation Status',
        color='Count',
        orientation='h',
        color_continuous_scale=px.colors.sequential.Plasma
    )
    
    st.plotly_chart(fig, use_container_width=True)

def plot_mobile_app_usage(df):
    """
    Plot mobile app usage statistics
    
    Args:
        df: Pandas DataFrame with mobile app usage data
    """
    if 'form_mobile_app_usage' not in df.columns or df.empty:
        st.info("Mobile app usage data not available.")
        return
    
    # Count mobile app usage
    app_usage_counts = df['form_mobile_app_usage'].value_counts().reset_index()
    app_usage_counts.columns = ['Usage Level', 'Count']
    
    # Create bar chart
    fig = px.bar(
        app_usage_counts,
        x='Usage Level',
        y='Count',
        title='Mobile App Usage Among Producers',
        color='Count',
        color_continuous_scale=px.colors.sequential.Viridis
    )
    
    st.plotly_chart(fig, use_container_width=True)

def plot_cleanliness_stats(df):
    """
    Plot cleanliness statistics
    
    Args:
        df: Pandas DataFrame with cleanliness data
    """
    cleanliness_columns = [
        'form_pipeline_cleanliness',
        'form_center_surroundings_cleanliness',
        'form_water_tank_cleanliness'
    ]
    
    # Check if at least one column exists
    if not any(col in df.columns for col in cleanliness_columns) or df.empty:
        st.info("Cleanliness data not available.")
        return
    
    # Prepare data for each available column
    data = []
    for col in cleanliness_columns:
        if col in df.columns:
            clean_name = col.replace('form_', '').replace('_', ' ').title()
            counts = df[col].value_counts()
            
            for category, count in counts.items():
                data.append({
                    'Area': clean_name,
                    'Rating': category,
                    'Count': count
                })
    
    if not data:
        st.info("Cleanliness data not available.")
        return
    
    # Convert to DataFrame
    cleanliness_df = pd.DataFrame(data)
    
    # Create grouped bar chart
    fig = px.bar(
        cleanliness_df,
        x='Area',
        y='Count',
        color='Rating',
        title='Cleanliness Ratings by Area',
        barmode='group',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    
    st.plotly_chart(fig, use_container_width=True)

def create_dashboard(df):
    """
    Create a comprehensive dashboard with all visualizations
    
    Args:
        df: Pandas DataFrame with all collection data
    """
    if df.empty:
        st.info("No data available for visualization.")
        return
    
    st.header("Dairy Collection Dashboard")
    
    # Overview metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Records", len(df))
    
    with col2:
        if 'form_total_suppliers' in df.columns:
            total_suppliers = df['form_total_suppliers'].sum()
            st.metric("Total Suppliers", total_suppliers)
    
    with col3:
        if 'timestamp' in df.columns:
            df['date'] = pd.to_datetime(df['timestamp']).dt.date
            latest_date = df['date'].max()
            today = datetime.now().date()
            days_since_update = (today - latest_date).days if latest_date else None
            st.metric("Days Since Last Update", days_since_update if days_since_update is not None else "N/A")
    
    # Create two columns for charts
    col1, col2 = st.columns(2)
    
    with col1:
        plot_milk_collection_trend(df)
        plot_shift_distribution(df)
        plot_cleanliness_stats(df)
    
    with col2:
        plot_member_vs_nonmember(df)
        plot_software_usage(df)
        plot_mobile_app_usage(df)
