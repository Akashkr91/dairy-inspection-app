import streamlit as st
from datetime import datetime, time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import numpy as np
import math

from utils import save_form_data, clear_form, load_data, delete_entry, get_data_as_dataframe
from translations import get_text

def analog_time_input(label="", value=None, key=None):
    """Simple time input using Streamlit time_input"""
    if value is None:
        value = time(12, 0)
    return st.time_input(label, value=value, key=key)

def render_header():
    """Render the application header"""
    col1, col2 = st.columns([1, 5])
    
    with col1:
        st.image("assets/logo.svg", width=80)
    
    with col2:
        st.title(get_text("app_title"))
        st.write(get_text("app_description"))

def render_form_sections():
    """Render all form sections for data collection"""
    # Create a form
    with st.form("dairy_collection_form"):
        # Section 1: Basic Information
        st.subheader(get_text("basic_info_section"))
        
        col1, col2 = st.columns(2)
        with col1:
            st.text_input(get_text("email"), key="form_email")
        
        with col2:
            st.date_input(get_text("date"), key="form_date", value=datetime.now().date())
        
        # Time of visit with analog clock style
        st.write(get_text("visit_time"))
        visit_time = analog_time_input(
            label="",
            value=time(12, 0),  # Default to noon
            key="form_time_picker_analog"
        )
        # Store the time in the session state
        st.session_state.form_visit_time = visit_time
        
        # Shift selection
        st.selectbox(
            get_text("shift"),
            [get_text("morning"), get_text("evening")],
            key="form_shift"
        )
        
        # Team Leader Selection
        st.selectbox(
            get_text("team_leader"),
            [
                "ಎ.ಕೆ.ನಾಗೇಶ್", "ಚೇತನ್.ಎಸ್", "ಪೂರ್ಣಿಮ.ಹೆಚ್.ಡಿ", "ನವೀನ್‌ಕುಮಾರ್.ಎಂ.ವಿ",
                "ರಶ್ಮೀ.ಎಂ.ಆರ್", "ಜಮುನ.ಎನ್", "ಡಾ||ಗೌರಿಶಂಕರ್ ಸಾಹು", "ಶೃತಿ.ಎನ್.ಎಂ",
                "ಸಂಜಯ್.ಎಸ್", "ಶ್ವೇತ.ಎಂ", "ಗಗನ.ಕೆ.ಜಿ", "ಗಿರಿಜ.ಎಸ್", "ಪ್ರಭುಶಂಕರ್.ವಿ",
                "ಎಲ್.ಆರ್.ಕರಿಬಸವರಾಜು", "ಬಸವರಾಜು.ಎಸ್", "ಬಬಿತ.ಸಿ", "ಡಿ.ಜಿ.ನಿತಿನ್",
                "ಚಿನ್ಮಯಾನಂದರಾಜೇ ಅರಸ್.ಹೆಚ್.ಎಂ", "ಲಿಖಿತ.ಕೆ", "ಅನುಪಮ.ಡಿ.ಎಸ್", "ಚರಮಣ.ಎಂ.ಬಿ",
                "ಪವಿತ್ರ.ಎನ್", "ಅಚ್ಯುತನ್.ಎಸ್", "ಸಂದೇಶ್.ಎಸ್", "ಹರ್ಷವರ್ಧನ್.ಎಸ್",
                "ನಂದಿನಿ.ಎಂ", "ಮನೋಹರ್.ಕೆ.ಎಂ", "ಜಿ.ಎನ್.ಸಂತೋಷ್", "ಮನೋಜ್ ಕುಮಾರ್.ಆರ್.ಕೆ",
                "ಮಹಾಲಕ್ಷ್ಮೀ.ಆರ್", "ತೃಪ್ತಿ ಕೃಷ್ಣಪ್ಪ ಪಟಗಾರ್", "ಶ್ರೀನಿವಾಸ್ ಪ್ರಸಾದ್.ಸಿ",
                "ನಂದಿನಿ.ಹೆಚ್.ಎಸ್", "ನಾಗವೇಣಿ.ಓ", "ಕಿಶೋರ್ ಕುಮಾರ್.ಜಿ.ಎಸ್", "ಸೌಮ್ಯ.ಜಿ.ಎಸ್",
                "ಪ್ರದೀಪ್.ಎಸ್", "ಸೈದಾ ಉಮ್ಮೆ ರುಮ್ಮಾನ್", "ಎಸ್.ವಿ.ಲಾವಣ್ಯವತಿ", "ಶ್ವೇತ.ಬಿ.ಎಲ್"
            ],
            key="form_team_leader"
        )
        
        # Extension Officer Selection
        st.selectbox(
            get_text("extension_officer"),
            [
                "ಆಕಾಶ್ ಕೆ.ಆರ್", "ಸಂತೋಷ್ ಕುಮಾರ್", "ವಿನುತ ಆರ್", "ಮೇಘನಾ ಎಂ",
                "ಪ್ರವೀಣ್ ಕೆ.ಎಸ್", "ಡಾ||ಶಿವಕುಮಾರ್ ಎಂ", "ಪರಮೇಶ್.ಎಂ", "ಮಹದೇವಿ ಎಂ.ಜೆ",
                "ಗೌತಮ್ ಬಿ", "ವಸಂತ", "ನಿಶಾಂತ್ ಸಿ", "ಅಂಜಲಿ .ಎನ್", "ಪ್ರಮೋದ್.ಆರ್",
                "ದಿವ್ಯಶ್ರೀ.ಎನ್", "ಶಿವಕುಮಾರಬೋವಿ", "ಅನಿತಾ.ಸಿ", "ಶೃತಿ ಕೆ.ಎನ್", "ರಂಜಿತ ಬಿ.ಎಸ್",
                "ರಶ್ಮಿ.ಸಿ.ಕೆ", "ಸುಮಂತ್ ಬಿ.ಯು", "ನೇಮ್ಮಣ್ಣ ಮಾಕಣಿ", "ವರಲಕ್ಷಿ ಎನ್.ಎಂ",
                "ನಾಗರಾಜು ಎನ್.ಡಿ", "ಶೃತಿ ಆರ್", "ಶಿವಕುಮಾರ್ ಎಂ", "ಡಾ|| ರಮ್ಯಾ.ಎಂ.ಆರ್",
                "ಮಹದೇವಸ್ವಾಮಿ.ಕೆ", "ವೀಣಾ ಎಸ್", "ನಿಶ್ಚಿತ್ ಬಿ.ಎಸ್", "ನಂದಿನಿ ಎಂ",
                "ಸತೀಶ", "ಅವಿನಾಶ್.ಎಂ", "ಆರೀಫ್ ಇಕ್ಬಾಲ್", "ಯೋಗೀಶ್.ಪಿ", "ರಾಮಪ್ಪಬಾರ್ಕಿ",
                "ಜಯಂತ್‌ಕುಮಾರ್ ಕೆ.ಆರ್", "ಜಗದಾಂಬ ಎಂ.ವೈ", "ತಾಹೀರ ಗರಗ", "ರಮ್ಯಶ್ರೀ. ಎಲ್"
            ],
            key="form_extension_officer"
        )
        
        # Chemist Selection
        st.selectbox(
            get_text("chemist"),
            [
                "ಮಧುಚೇತನ್.ಡಿ.ಸಿ", "ಸಂತೋಷ್.ಎನ್", "ಶರ್ಮಿಳಾ.ಬಿ.ಆರ್", "ಶೃತಿ.ಪಿ",
                "ಸುರೇಶ್ ತಾಂವಶಿ", "ಜಮುನ.ಎನ್", "ಸುಪ್ರಿಯಾ.ಎನ್.ಪಿ", "ನಿಶ್ಚಿತ.ಹೆಚ್.ಜಿ",
                "ಜಯಶೀಲ.ಎಸ್", "ಅರ್ಪಿತ ವರದರಾಜ್", "ಅನ್ನಪೂರ್ಣ.ಜಿ", "ನಾಗೇಂದ್ರ ಪ್ರಸಾದ್.ಟಿ.ಸಿ",
                "ಪೂರ್ಣಚಂದ್ರ.ಕೆ.ಎನ್", "ಅಶ್ವಿನಿ.ಎಸ್", "ನವ್ಯಶ್ರೀ.ಕೆ", "ನಾಗರಾಜು.ಎಂ", "ಪವಿತ್ರ.ಎನ್"
            ],
            key="form_chemist"
        )
        
        # BMC Center Information
        st.text_input(get_text("bmc_center_name"), key="form_bmc_center_name")
        
        st.text_input(get_text("bmc_staff_details"), key="form_bmc_staff_details")
        
        col1, col2 = st.columns(2)
        with col1:
            st.write(get_text("milk_collection_start_time"))
            milk_start_time = analog_time_input(
                label="",
                key="form_milk_start_analog"
            )
            st.session_state.form_milk_collection_start_time = milk_start_time
        
        with col2:
            st.write(get_text("milk_collection_end_time"))
            milk_end_time = analog_time_input(
                label="",
                key="form_milk_end_analog"
            )
            st.session_state.form_milk_collection_end_time = milk_end_time
        
        col1, col2 = st.columns(2)
        with col1:
            st.write(get_text("tanker_arrival_time"))
            tanker_arrival_time = analog_time_input(
                label="",
                key="form_tanker_arrival_analog"
            )
            st.session_state.form_tanker_arrival_time = tanker_arrival_time
        
        with col2:
            st.write(get_text("tanker_departure_time"))
            tanker_departure_time = analog_time_input(
                label="",
                key="form_tanker_departure_analog"
            )
            st.session_state.form_tanker_departure_time = tanker_departure_time
        
        # Section 2: AMCS Software Information
        st.subheader(get_text("amcs_section"))
        
        st.selectbox(
            get_text("amcs_software_status"),
            [
                get_text("amcs_installed_working"),
                get_text("amcs_installed_not_working"),
                get_text("amcs_not_installed")
            ],
            key="form_amcs_software_status"
        )
        
        st.selectbox(
            get_text("weighing_machine_status"),
            [
                get_text("weighing_online_working"),
                get_text("weighing_online_not_working"),
                get_text("weighing_not_online")
            ],
            key="form_weighing_machine_status"
        )
        
        st.selectbox(
            get_text("fat_analyzer_status"),
            [
                get_text("fat_analyzer_online_working"),
                get_text("fat_analyzer_online_not_working"),
                get_text("fat_analyzer_not_online")
            ],
            key="form_fat_analyzer_status"
        )
        
        st.selectbox(
            get_text("mobile_app_usage"),
            [
                get_text("mobile_app_usage_0_25"),
                get_text("mobile_app_usage_25_50"),
                get_text("mobile_app_usage_50_75"),
                get_text("mobile_app_usage_75_100"),
                get_text("mobile_app_no_info")
            ],
            key="form_mobile_app_usage"
        )
        
        st.selectbox(
            get_text("secretary_mobile_app_usage"),
            [
                get_text("secretary_using_app"),
                get_text("secretary_not_using_app"),
                get_text("secretary_no_info")
            ],
            key="form_secretary_mobile_app_usage"
        )
        
        # Section 3: Milk Collection Information
        st.subheader(get_text("milk_collection_section"))
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.number_input(get_text("total_suppliers"), min_value=0, key="form_total_suppliers")
        
        with col2:
            st.number_input(get_text("member_suppliers"), min_value=0, key="form_member_suppliers")
        
        with col3:
            st.number_input(get_text("non_member_suppliers"), min_value=0, key="form_non_member_suppliers")
        
        st.text_area(get_text("card_issues"), key="form_card_issues")
        
        # Adulteration details as checkboxes
        st.write(get_text("adulteration_details"))
        col1, col2, col3 = st.columns(3)
        
        with col1:
            sugar_adulteration = st.checkbox(
                get_text("sugar_adulteration"),
                key="form_sugar_adulteration"
            )
        
        with col2:
            water_adulteration = st.checkbox(
                get_text("water_adulteration"),
                key="form_water_adulteration"
            )
        
        with col3:
            no_adulteration = st.checkbox(
                get_text("no_adulteration"),
                key="form_no_adulteration"
            )
            
        # Store the results as a list for compatibility with the existing data structure
        if 'form_adulteration_details' not in st.session_state:
            st.session_state.form_adulteration_details = []
            
        # Update the list based on checkboxes
        adulteration_details = []
        if sugar_adulteration:
            adulteration_details.append(get_text("sugar_adulteration"))
        if water_adulteration:
            adulteration_details.append(get_text("water_adulteration"))
        if no_adulteration:
            adulteration_details.append(get_text("no_adulteration"))
        
        st.session_state.form_adulteration_details = adulteration_details
        
        # Milk testing equipment as checkboxes
        st.write(get_text("testing_equipment"))
        
        # Define equipment options
        equipment_options = [
            "Fatomatic",
            "Milk Analyser",
            "Lactosure",
            "Milkoscreen",
            "Gerber",
            "Adulteration kit",
            "Reagents"
        ]
        
        # Create multiple columns for better layout
        cols = st.columns(3)
        
        # Initialize list to store selected equipment
        selected_equipment = []
        
        # Create checkbox for each equipment option
        for i, equipment in enumerate(equipment_options):
            col_index = i % 3  # Distribute across 3 columns
            with cols[col_index]:
                if st.checkbox(equipment, key=f"form_equipment_{equipment.lower().replace(' ', '_')}"):
                    selected_equipment.append(equipment)
        
        # Store the selection in session state
        st.session_state.form_testing_equipment = selected_equipment
        
        st.selectbox(
            get_text("weighing_machine_certification"),
            [
                get_text("certification_available"),
                get_text("certification_not_available"),
                get_text("certification_info_not_available")
            ],
            key="form_weighing_machine_certification"
        )
        
        st.selectbox(
            get_text("weighing_seal"),
            [
                get_text("seal_available"),
                get_text("seal_not_available"),
                get_text("seal_info_not_available")
            ],
            key="form_weighing_seal"
        )
        
        # Cleanliness & Hygiene
        st.selectbox(
            get_text("pipeline_cleanliness"),
            [
                get_text("very_clean"),
                get_text("average_clean"),
                get_text("not_clean")
            ],
            key="form_pipeline_cleanliness"
        )
        
        st.selectbox(
            get_text("center_surroundings_cleanliness"),
            [
                get_text("very_clean"),
                get_text("average_clean"),
                get_text("not_clean")
            ],
            key="form_center_surroundings_cleanliness"
        )
        
        st.selectbox(
            get_text("water_tank_cleanliness"),
            [
                get_text("very_clean"),
                get_text("average_clean"),
                get_text("not_clean")
            ],
            key="form_water_tank_cleanliness"
        )
        
        st.text_area(get_text("rejected_milk_details"), key="form_rejected_milk_details")
        
        st.selectbox(
            get_text("fssai_license"),
            [
                get_text("license_available"),
                get_text("license_not_available")
            ],
            key="form_fssai_license"
        )
        
        # Adding cattle feed license field
        st.selectbox(
            get_text("cattle_feed_license"),
            [
                get_text("license_available"),
                get_text("license_not_available")
            ],
            key="form_cattle_feed_license"
        )
        
        # Account maintenance section
        st.selectbox(
            get_text("account_maintenance"),
            [
                get_text("accounts_maintained_properly"),
                get_text("accounts_not_maintained_properly"),
                get_text("accounts_info_not_available")
            ],
            key="form_account_maintenance"
        )
        
        # CCTV installation and maintenance
        st.selectbox(
            get_text("cctv_installation"),
            [
                get_text("cctv_installed_maintained"),
                get_text("cctv_installed_not_maintained"),
                get_text("cctv_not_installed")
            ],
            key="form_cctv_installation"
        )
        
        # AMCS software edit/delete options
        st.selectbox(
            get_text("amcs_edit_delete_options"),
            [
                get_text("edit_delete_disabled"),
                get_text("edit_delete_enabled")
            ],
            key="form_amcs_edit_delete_options"
        )
        
        # Other observations
        st.subheader(get_text("other_observations"))
        
        # Other details (removed the dry fodder checkbox)
        st.text_area(
            get_text("other_details"),
            key="form_other_details"
        )
        
        # Photo upload section
        st.subheader(get_text("photo_upload"))
        st.write(get_text("photo_upload_note"))
        
        # Truck sheet photo
        st.file_uploader(
            get_text("truck_sheet_photo"),
            type=["jpg", "jpeg", "png"],
            key="form_truck_sheet_photo"
        )
        
        # Challan sheet photo
        st.file_uploader(
            get_text("challan_sheet_photo"),
            type=["jpg", "jpeg", "png"],
            key="form_challan_sheet_photo"
        )
        
        # Purchase sheet photo
        st.file_uploader(
            get_text("purchase_sheet_photo"),
            type=["jpg", "jpeg", "png"],
            key="form_purchase_sheet_photo"
        )
        
        # BMC building photo
        st.file_uploader(
            get_text("bmc_building_photo"),
            type=["jpg", "jpeg", "png"],
            key="form_bmc_building_photo"
        )
        
        # Cattle feed storage room photo
        st.file_uploader(
            get_text("cattle_feed_storage_photo"),
            type=["jpg", "jpeg", "png"],
            key="form_cattle_feed_storage_photo"
        )
        
        # BMC premises photo
        st.file_uploader(
            get_text("bmc_premises_photo"),
            type=["jpg", "jpeg", "png"],
            key="form_bmc_premises_photo"
        )
        
        # Team visit photo
        st.file_uploader(
            get_text("team_visit_photo"),
            type=["jpg", "jpeg", "png"],
            key="form_team_visit_photo"
        )
        
        # Form submission
        submitted = st.form_submit_button(get_text("submit_form"))
        
        if submitted:
            save_form_data()
    
    # Display success message if form was submitted
    if st.session_state.form_submitted:
        st.success(get_text("form_submit_success"))
        
        if st.button(get_text("clear_form")):
            clear_form()
            st.rerun()

def render_admin_dashboard():
    """Render the admin dashboard"""
    st.title(get_text("admin_dashboard"))
    
    # Tabs for different admin functions
    tab1, tab2, tab3 = st.tabs([
        get_text("data_management"),
        get_text("user_management"),
        get_text("system_settings")
    ])
    
    with tab1:
        st.subheader(get_text("data_management"))
        
        # Load data
        df = get_data_as_dataframe()
        
        if df.empty:
            st.info(get_text("no_data_available"))
        else:
            # Display data
            st.dataframe(df)
            
            # Data management options
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button(get_text("export_all_data")):
                    # Export all data as CSV
                    st.download_button(
                        label=get_text("download_csv"),
                        data=df.to_csv(index=False).encode('utf-8'),
                        file_name=f'complete_data_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv',
                        mime='text/csv',
                    )
            
            with col2:
                # Delete entry by ID
                if 'id' in df.columns:
                    entry_ids = df['id'].tolist()
                    selected_id = st.selectbox(
                        get_text("select_entry_to_delete"),
                        options=entry_ids,
                        format_func=lambda x: f"ID #{x}"
                    )
                    
                    if st.button(get_text("delete_selected_entry")):
                        if delete_entry(selected_id):
                            st.success(get_text("entry_deleted"))
                            st.rerun()
                        else:
                            st.error(get_text("error_deleting_entry"))
                else:
                    st.warning("No entries with IDs found. Database may be empty.")
    
    with tab2:
        st.subheader(get_text("user_management"))
        st.info(get_text("user_management_info"))
        
        # Simple user management form
        with st.form("user_management_form"):
            st.text_input(get_text("username"))
            st.text_input(get_text("password"), type="password")
            st.text_input(get_text("confirm_password"), type="password")
            st.selectbox(get_text("user_role"), [get_text("admin"), get_text("user")])
            
            if st.form_submit_button(get_text("add_user")):
                st.success(get_text("user_added"))
    
    with tab3:
        st.subheader(get_text("system_settings"))
        st.info(get_text("system_settings_info"))
        
        # Basic system settings
        default_language = st.selectbox(
            get_text("default_language"),
            [get_text("kannada"), get_text("english")],
            index=0 if st.session_state.language == 'kannada' else 1
        )
        
        if st.button(get_text("save_settings")):
            st.session_state.language = 'kannada' if default_language == get_text("kannada") else 'english'
            st.success(get_text("settings_saved"))
            st.rerun()
