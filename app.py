import streamlit as st
import pandas as pd
from datetime import datetime, time
import os
import json

from utils import initialize_session_state, toggle_language, load_data, save_data, migrate_legacy_data
from components import render_header, render_form_sections, render_admin_dashboard
from auth import check_password, login_form
from translations import get_text
from sustainability_game import render_game
from database_manager import get_entries

# Page configuration
st.set_page_config(
    page_title="Dairy Collection Center Monitoring",
    page_icon="🥛",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
initialize_session_state()

# Try to migrate legacy data from JSON files to database if needed
try:
    # Check for legacy data and migrate if needed
    if 'db_migration_attempted' not in st.session_state:
        migrate_legacy_data()
        st.session_state.db_migration_attempted = True
except Exception as e:
    st.error(f"Database initialization error: {e}")

# Render header with language toggle
render_header()

# Main application logic
def main():
    # Sidebar
    with st.sidebar:
        st.title(get_text("app_title"))
        
        # Language selector
        if st.button(get_text("toggle_language")):
            toggle_language()
            st.rerun()
        
        # Navigation
        page = st.radio(
            get_text("navigation"),
            [get_text("data_entry"), get_text("reports"), get_text("admin"), "Community Game"]
        )
        
        st.divider()
        
        # Login for admin section
        if page == get_text("admin") and not st.session_state.authenticated:
            authenticated = login_form()
            if authenticated:
                st.session_state.authenticated = True
                st.success(get_text("login_success"))
                st.rerun()
        
        # Logout button if authenticated
        if st.session_state.authenticated:
            if st.button(get_text("logout")):
                st.session_state.authenticated = False
                st.rerun()
    
    # Main content area
    if page == get_text("data_entry"):
        st.title(get_text("data_entry"))
        render_form_sections()
        
    elif page == get_text("reports"):
        st.title(get_text("reports"))
        
        # Load saved data
        data = load_data()
        
        if not data:
            st.info(get_text("no_data_available"))
        else:
            # Convert to DataFrame for display
            try:
                df = pd.DataFrame(data)
                
                # Basic statistics
                st.subheader(get_text("collection_statistics"))
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric(get_text("total_entries"), len(df))
                
                with col2:
                    if 'form_total_suppliers' in df.columns:
                        st.metric(get_text("avg_suppliers"), round(df['form_total_suppliers'].mean(), 1))
                
                with col3:
                    if 'form_member_suppliers' in df.columns and 'form_non_member_suppliers' in df.columns:
                        member_ratio = df['form_member_suppliers'].sum() / (df['form_member_suppliers'].sum() + df['form_non_member_suppliers'].sum()) * 100
                        st.metric(get_text("member_percentage"), f"{round(member_ratio, 1)}%")
                
                # Data table
                st.subheader(get_text("data_table"))
                st.dataframe(df)
                
                # Export options
                st.download_button(
                    label=get_text("download_csv"),
                    data=df.to_csv(index=False).encode('utf-8'),
                    file_name=f'dairy_collection_data_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv',
                    mime='text/csv',
                )
                
            except Exception as e:
                st.error(f"Error processing data: {e}")
        
    elif page == get_text("admin"):
        if st.session_state.authenticated:
            render_admin_dashboard()
        else:
            st.warning(get_text("admin_login_required"))
    
    elif page == "Community Game":
        render_game()

if __name__ == "__main__":
    main()
