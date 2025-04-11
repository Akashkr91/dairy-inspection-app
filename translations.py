import streamlit as st

# Dictionary of translations
translations = {
    # App general
    "app_title": {
        "kannada": "ಹಾಲು ಸಂಗ್ರಹ ಕೇಂದ್ರ ಮೇಲ್ವಿಚಾರಣೆ",
        "english": "Dairy Collection Center Monitoring"
    },
    "app_description": {
        "kannada": "ಹಾಲು ಸಂಗ್ರಹ ಕೇಂದ್ರಗಳ ದತ್ತಾಂಶ ಸಂಗ್ರಹಣೆ ಮತ್ತು ಮೇಲ್ವಿಚಾರಣೆ ವ್ಯವಸ್ಥೆ",
        "english": "Data collection and monitoring system for dairy collection centers"
    },
    "toggle_language": {
        "kannada": "English ಭಾಷೆಗೆ ಬದಲಾಯಿಸಿ",
        "english": "ಕನ್ನಡಕ್ಕೆ ಬದಲಾಯಿಸಿ (Switch to Kannada)"
    },
    "navigation": {
        "kannada": "ನ್ಯಾವಿಗೇಶನ್",
        "english": "Navigation"
    },
    "data_entry": {
        "kannada": "ದತ್ತಾಂಶ ನಮೂದಿಸುವಿಕೆ",
        "english": "Data Entry"
    },
    "reports": {
        "kannada": "ವರದಿಗಳು",
        "english": "Reports"
    },
    "admin": {
        "kannada": "ಆಡಳಿತ",
        "english": "Admin"
    },
    
    # Authentication
    "login": {
        "kannada": "ಲಾಗಿನ್",
        "english": "Login"
    },
    "logout": {
        "kannada": "ಲಾಗ್ ಔಟ್",
        "english": "Logout"
    },
    "username": {
        "kannada": "ಬಳಕೆದಾರ ಹೆಸರು",
        "english": "Username"
    },
    "password": {
        "kannada": "ಪಾಸ್‌ವರ್ಡ್",
        "english": "Password"
    },
    "login_button": {
        "kannada": "ಲಾಗಿನ್",
        "english": "Login"
    },
    "login_error": {
        "kannada": "ತಪ್ಪಾದ ಬಳಕೆದಾರ ಹೆಸರು ಅಥವಾ ಪಾಸ್‌ವರ್ಡ್",
        "english": "Incorrect username or password"
    },
    "login_success": {
        "kannada": "ಯಶಸ್ವಿಯಾಗಿ ಲಾಗಿನ್ ಆಗಿದೆ",
        "english": "Successfully logged in"
    },
    "admin_login_required": {
        "kannada": "ಆಡಳಿತ ವಿಭಾಗವನ್ನು ಪ್ರವೇಶಿಸಲು ಲಾಗಿನ್ ಮಾಡಿ",
        "english": "Please login to access the admin section"
    },
    
    # Form sections
    "basic_info_section": {
        "kannada": "ಮೂಲಭೂತ ಮಾಹಿತಿ",
        "english": "Basic Information"
    },
    "email": {
        "kannada": "ಇಮೇಲ್",
        "english": "Email"
    },
    "date": {
        "kannada": "ದಿನಾಂಕ",
        "english": "Date"
    },
    "visit_time": {
        "kannada": "ಭೇಟಿಯ ಸಮಯ",
        "english": "Time of Visit"
    },
    "shift": {
        "kannada": "ಸರದಿ",
        "english": "Shift"
    },
    "morning": {
        "kannada": "ಬೆಳಿಗ್ಗೆ",
        "english": "Morning"
    },
    "evening": {
        "kannada": "ಸಂಜೆ",
        "english": "Evening"
    },
    "team_leader": {
        "kannada": "ಅನಿರೀಕ್ಷಿತ ತಂಡದ ಮುಖ್ಯಸ್ಥರ ಹೆಸರು ಮತ್ತು ಹುದ್ದೆ",
        "english": "Team Leader Name and Designation"
    },
    "extension_officer": {
        "kannada": "ವಿಸ್ತರಣಾಧಿಕಾರಿಗಳ ಹೆಸರು",
        "english": "Extension Officer Name"
    },
    "chemist": {
        "kannada": "ಕೆಮಿಸ್ಟ್ ಹೆಸರು",
        "english": "Chemist Name"
    },
    "bmc_center_name": {
        "kannada": "ಬಿ.ಎಂ.ಸಿ ಕೇಂದ್ರದ ಹೆಸರು ಮತ್ತು ತಾಲ್ಲೂಕು",
        "english": "BMC Center Name and Taluk"
    },
    "bmc_staff_details": {
        "kannada": "ಬಿ.ಎಂ.ಸಿ ಕೇಂದ್ರದ ಸಿಬ್ಬಂದಿಗಳ ವಿವರ",
        "english": "BMC Center Staff Details"
    },
    "milk_collection_start_time": {
        "kannada": "ಹಾಲು ಶೇಖರಣೆ ಪ್ರಾರಂಭವಾದ ಸಮಯ",
        "english": "Milk Collection Start Time"
    },
    "milk_collection_end_time": {
        "kannada": "ಹಾಲು ಶೇಖರಣೆ ಮುಕ್ತಾಯವಾದ ಸಮಯ",
        "english": "Milk Collection End Time"
    },
    "tanker_arrival_time": {
        "kannada": "ಬಿ.ಎಂ.ಸಿ ಕೇಂದ್ರಕ್ಕೆ ಟ್ಯಾಂಕರ್ ಬಂದ ವೇಳೆ",
        "english": "Tanker Arrival Time at BMC Center"
    },
    "tanker_departure_time": {
        "kannada": "ಬಿ.ಎಂ.ಸಿ ಕೇಂದ್ರಕ್ಕೆ ಟ್ಯಾಂಕರ್ ಹೊರಟ ವೇಳೆ",
        "english": "Tanker Departure Time from BMC Center"
    },
    
    # AMCS section
    "amcs_section": {
        "kannada": "ಎನ್.ಡಿ.ಡಿ.ಬಿ ಅಭಿವೃದ್ದಿ ಪಡಿಸಿರುವ ಎ.ಎಮ್.ಸಿ.ಎಸ್ ಸಾಫ್ಟ್ ವೇರ್ ಅಳವಡಿಕೆ ಕುರಿತು",
        "english": "About NDDB Developed AMCS Software Implementation"
    },
    "amcs_software_status": {
        "kannada": "ಸಾಫ್ಟ್ ವೇರ್ ಅಳವಡಿಕೆ ಬಗ್ಗೆ",
        "english": "Software Implementation Status"
    },
    "amcs_installed_working": {
        "kannada": "AMCS ಸಾಫ್ಟ್ ವೇರ್ ಅಳವಡಿಸಲಾಗಿದೆ, Data Fetch ಆಗುತ್ತಿರುತ್ತದೆ",
        "english": "AMCS software installed, data fetch working"
    },
    "amcs_installed_not_working": {
        "kannada": "AMCS ಸಾಫ್ಟ್ ವೇರ್ ಅಳವಡಿಸಲಾಗಿದೆ, Data Fetch ಆಗುತ್ತಿರುವುದಿಲ್ಲ",
        "english": "AMCS software installed, data fetch not working"
    },
    "amcs_not_installed": {
        "kannada": "AMCS ಸಾಫ್ಟ್ ವೇರ್ ಅಳವಡಿಸಲಾಗಿರುವುದಿಲ್ಲ",
        "english": "AMCS software not installed"
    },
    "weighing_machine_status": {
        "kannada": "ತೂಕದ ಯಂತ್ರವನ್ನು ಆನ್‌ಲೈನ್ ಮಾಡಿಸಿ, ತೂಕವನ್ನು ಪಡೆಯುತ್ತಿರುವ ಬಗ್ಗೆ",
        "english": "About weight machine online status and weight measurement"
    },
    "weighing_online_working": {
        "kannada": "ಆನ್‌ಲೈನ್ ಆಗಿರುತ್ತದೆ, ಆನ್‌ಲೈನ್ ಮೂಲಕ ತೂಕ ಪಡೆಯುತ್ತಿರುತ್ತಾರೆ",
        "english": "Online and getting weight through online"
    },
    "weighing_online_not_working": {
        "kannada": "ಆನ್‌ಲೈನ್ ಆಗಿರುತ್ತದೆ, ಆನ್‌ಲೈನ್ ಮೂಲಕ ತೂಕ ಪಡೆಯುತ್ತಿರುವುದಿಲ್ಲ",
        "english": "Online but not getting weight through online"
    },
    "weighing_not_online": {
        "kannada": "ಆನ್‌ಲೈನ್ ಆಗಿರುವುದಿಲ್ಲ",
        "english": "Not online"
    },
    "fat_analyzer_status": {
        "kannada": "ಫ್ಯಾಟ್ ಅಥವಾ ಅನಲೈಜರ್ ಯಂತ್ರವನ್ನು ಆನ್‌ಲೈನ್ ಮಾಡಿಸಿ ದರ ನೀಡುತ್ತಿರುವ ಬಗ್ಗೆ",
        "english": "About fat analyzer online status and pricing"
    },
    "fat_analyzer_online_working": {
        "kannada": "ಆನ್‌ಲೈನ್ ಮಾಡಿಸಿದ್ದು, ಅದರಂತೆ ದರ ನೀಡುತ್ತಿರುತ್ತಾರೆ",
        "english": "Online and pricing accordingly"
    },
    "fat_analyzer_online_not_working": {
        "kannada": "ಆನ್‌ಲೈನ್ ಮಾಡಿಸಿದ್ದು, ಅದರಂತೆ ದರ ನೀಡುತ್ತಿರುವುದಿಲ್ಲ",
        "english": "Online but not pricing accordingly"
    },
    "fat_analyzer_not_online": {
        "kannada": "ಆನ್‌ಲೈನ್ ಮಾಡಿಸಿರುವುದಿಲ್ಲ",
        "english": "Not online"
    },
    "mobile_app_usage": {
        "kannada": "ಉತ್ಪಾದಕರ ಮೊಬೈಲ್ ಆಪ್ (App)ನ ಬಳಕೆ ಬಗ್ಗೆ",
        "english": "About producer mobile app usage"
    },
    "mobile_app_usage_0_25": {
        "kannada": "ಶೇಕಡಾವಾರು 0-25(%) ಉತ್ಪಾದಕರು ಮೊಬೈಲ್ ಆಪ್ (App)ನ ಬಳಕೆ ಮಾಡುತ್ತಿರುತ್ತಾರೆ",
        "english": "0-25% of producers use mobile app"
    },
    "mobile_app_usage_25_50": {
        "kannada": "ಶೇಕಡಾವಾರು 25-50(%) ಉತ್ಪಾದಕರು ಮೊಬೈಲ್ ಆಪ್ (App)ನ ಬಳಕೆ ಮಾಡುತ್ತಿರುತ್ತಾರೆ",
        "english": "25-50% of producers use mobile app"
    },
    "mobile_app_usage_50_75": {
        "kannada": "ಶೇಕಡಾವಾರು 50-75(%) ಉತ್ಪಾದಕರು ಮೊಬೈಲ್ ಆಪ್ (App)ನ ಬಳಕೆ ಮಾಡುತ್ತಿರುತ್ತಾರೆ",
        "english": "50-75% of producers use mobile app"
    },
    "mobile_app_usage_75_100": {
        "kannada": "ಶೇಕಡಾವಾರು 75-100(%) ಉತ್ಪಾದಕರು ಮೊಬೈಲ್ ಆಪ್ (App)ನ ಬಳಕೆ ಮಾಡುತ್ತಿರುತ್ತಾರೆ",
        "english": "75-100% of producers use mobile app"
    },
    "mobile_app_no_info": {
        "kannada": "ಉತ್ಪಾದಕರಿಗೆ ಮೊಬೈಲ್ ಆಪ್ (App)ನ ಬಗ್ಗೆ ಮಾಹಿತಿ ಇರುವುದಿಲ್ಲ",
        "english": "Producers do not have information about mobile app"
    },
    "secretary_mobile_app_usage": {
        "kannada": "ಕಾರ್ಯದರ್ಶಿಗಳ ಮೊಬೈಲ್ ಆಪ್ ಬಳಕೆ ಬಗ್ಗೆ",
        "english": "About secretary mobile app usage"
    },
    "secretary_using_app": {
        "kannada": "ಬಳಕೆ ಮಾಡುತ್ತಿರುತ್ತಾರೆ",
        "english": "Using the app"
    },
    "secretary_not_using_app": {
        "kannada": "ಬಳಕೆ ಮಾಡುತ್ತಿರುವುದಿಲ್ಲ",
        "english": "Not using the app"
    },
    "secretary_no_info": {
        "kannada": "ಮಾಹಿತಿ ಇರುವುದಿಲ್ಲ",
        "english": "No information"
    },
    
    # Milk Collection section
    "milk_collection_section": {
        "kannada": "ಹಾಲು ಶೇಖರಣೆಯ ಮಾಹಿತಿ ಕುರಿತು",
        "english": "About Milk Collection Information"
    },
    "total_suppliers": {
        "kannada": "ಒಟ್ಟು ಹಾಲು ಸರಬರಾಜು ಮಾಡಿದ ಉತ್ಪಾದಕರ ಸಂಖ್ಯೆ",
        "english": "Total number of milk suppliers"
    },
    "member_suppliers": {
        "kannada": "ಸದಸ್ಯತ್ವ ಪಡೆದು ಹಾಲು ಸರಬರಾಜು ಮಾಡುತ್ತಿರುವವರ ಸಂಖ್ಯೆ",
        "english": "Number of suppliers with membership"
    },
    "non_member_suppliers": {
        "kannada": "ಸದಸ್ಯತ್ವ ಪಡೆಯದೆ ಹಾಲು ಸರಬರಾಜು ಮಾಡುತ್ತಿರುವವರ ಸಂಖ್ಯೆ",
        "english": "Number of suppliers without membership"
    },
    "card_issues": {
        "kannada": "ಸಂಘದಲ್ಲಿನ ನಕಲಿ ಕಾರ್ಡ್ ಮತ್ತು ಇತರೆ ನ್ಯೂನ್ಯತೆಗಳನ್ನು ಗಮನಿಸಿದ್ದ ಬಗ್ಗೆ",
        "english": "About fake cards and other deficiencies observed in the association"
    },
    "adulteration_details": {
        "kannada": "ಕಲಬೆರಕೆ ವಿವರ",
        "english": "Adulteration details"
    },
    "sugar_adulteration": {
        "kannada": "ಸಕ್ಕರೆ ಕಲಬೆರೆಕೆ",
        "english": "Sugar adulteration"
    },
    "water_adulteration": {
        "kannada": "ನೀರು ಕಲಬೆರೆಕೆ",
        "english": "Water adulteration"
    },
    "no_adulteration": {
        "kannada": "ಕಲಬೆರೆಕೆ ಇರುವುದಿಲ್ಲ",
        "english": "No adulteration"
    },
    "testing_equipment": {
        "kannada": "ಹಾಲು ಪರೀಕ್ಷಾ ಪರಿಕರಗಳ ವಿವರ",
        "english": "Milk testing equipment details"
    },
    "weighing_machine_certification": {
        "kannada": "ಹಾಲಿನ ತೂಕ ಯಂತ್ರದ ನಿರ್ವಹಣೆ ಬಗ್ಗೆ",
        "english": "About milk weighing machine maintenance"
    },
    "certification_available": {
        "kannada": "ಸತ್ಯಮಾಪನ ಪ್ರಮಾಣ ಪತ್ರ ಇರುತ್ತದೆ",
        "english": "Verification certificate available"
    },
    "certification_not_available": {
        "kannada": "ಸತ್ಯಮಾಪನ ಪ್ರಮಾಣ ಪತ್ರ ಇರುವುದಿಲ್ಲ",
        "english": "Verification certificate not available"
    },
    "certification_info_not_available": {
        "kannada": "ಮುಖ್ಯಕಾರ್ಯನಿರ್ವಾಹಕರು ಲಭ್ಯವಿರದ ಕಾರಣ ಮಾಹಿತಿ ಇರುವುದಿಲ್ಲ",
        "english": "Information not available as CEO is not available"
    },
    "weighing_seal": {
        "kannada": "ಹಾಲಿನ ತೂಕ ಯಂತ್ರದ ನಿರ್ವಹಣೆ ಬಗ್ಗೆ",
        "english": "About milk weighing machine maintenance"
    },
    "seal_available": {
        "kannada": "ತೂಕದ ಬೊಟ್ಟು ಇರುತ್ತದೆ",
        "english": "Weighing seal available"
    },
    "seal_not_available": {
        "kannada": "ತೂಕದ ಬೊಟ್ಟು ಇರುವುದಿಲ್ಲ",
        "english": "Weighing seal not available"
    },
    "seal_info_not_available": {
        "kannada": "ಮುಖ್ಯಕಾರ್ಯನಿರ್ವಾಹಕರು ಲಭ್ಯವಿರದ ಕಾರಣ ಮಾಹಿತಿ ಇರುವುದಿಲ್ಲ",
        "english": "Information not available as CEO is not available"
    },
    "pipeline_cleanliness": {
        "kannada": "ಪೈಪ್‌ಲೈನ್ ಮತ್ತು ಇತರೆ ಪರಿಕರಗಳ ಶುಚಿತ್ವದ ಬಗ್ಗೆ",
        "english": "About cleanliness of pipeline and other equipment"
    },
    "center_surroundings_cleanliness": {
        "kannada": "ಕೇಂದ್ರದ ಸುತ್ತಮುತ್ತಲಿನ ಶುಚಿತ್ವದ ಬಗ್ಗೆ",
        "english": "About cleanliness of center surroundings"
    },
    "water_tank_cleanliness": {
        "kannada": "ನೀರಿನ ಸಂಪ್ ಮತ್ತು ಓವರ್‌ಹೆಡ್ ಟ್ಯಾಂಕಿನ ಶುಚಿತ್ವದ ಬಗ್ಗೆ",
        "english": "About cleanliness of water sump and overhead tank"
    },
    "very_clean": {
        "kannada": "ಶುಚಿಯಾಗಿರುತ್ತದೆ",
        "english": "Very clean"
    },
    "average_clean": {
        "kannada": "ಸಾಧಾರಣವಾಗಿರುತ್ತದೆ",
        "english": "Average cleanliness"
    },
    "not_clean": {
        "kannada": "ಶುಚಿಯಾಗಿರುವುದಿಲ್ಲ",
        "english": "Not clean"
    },
    "rejected_milk_details": {
        "kannada": "ಕಳಪೆ ಹಾಗೂ ಕಲಬೆರಕೆ ಹಾಲನ್ನು ತಿರಸ್ಕರಿಸಿದ ವಿವರ",
        "english": "Details of rejected poor quality and adulterated milk"
    },
    "fssai_license": {
        "kannada": "ಎಫ್.ಎಸ್.ಎಸ್.ಎ.ಐ ಪರವಾನಿಗೆ ಬಗ್ಗೆ",
        "english": "About FSSAI license"
    },
    "license_available": {
        "kannada": "ಪರವಾನಿಗೆ ಇರುತ್ತದೆ",
        "english": "License available"
    },
    "license_not_available": {
        "kannada": "ಪರವಾನಿಗೆ ಇರುವುದಿಲ್ಲ",
        "english": "License not available"
    },
    
    # Cattle Feed License
    "cattle_feed_license": {
        "kannada": "ಪಶುಆಹಾರ ಪರವಾನಿಗೆ",
        "english": "Cattle Feed License"
    },
    
    # Account maintenance
    "account_maintenance": {
        "kannada": "ಸಂಘದ ಲೆಕ್ಕ ಪುಸ್ತಕಗಳ ನಿರ್ವಹಣೆ ಬಗ್ಗೆ",
        "english": "About society account book maintenance"
    },
    "accounts_maintained_properly": {
        "kannada": "ಸಮರ್ಪಕವಾಗಿ ನಿರ್ವಹಿಸಿರುತ್ತಾರೆ",
        "english": "Maintained properly"
    },
    "accounts_not_maintained_properly": {
        "kannada": "ಸಮರ್ಪಕವಾಗಿ ನಿರ್ವಹಿಸಿರುವುದಿಲ್ಲ",
        "english": "Not maintained properly"
    },
    "accounts_info_not_available": {
        "kannada": "ಮುಖ್ಯಕಾರ್ಯನಿರ್ವಾಹಕರು ಲಭ್ಯವಿರದ ಕಾರಣ ಮಾಹಿತಿ ಇರುವುದಿಲ್ಲ",
        "english": "Information not available as CEO is not available"
    },
    
    # CCTV installation
    "cctv_installation": {
        "kannada": "ಸಿ.ಸಿ ಟಿ.ವಿ ಅಳವಡಿಕೆ ಮತ್ತು ನಿರ್ವಹಣೆ ಕುರಿತು",
        "english": "About CCTV installation and maintenance"
    },
    "cctv_installed_maintained": {
        "kannada": "ಸಿ.ಸಿ ಟಿ.ವಿ ಅಳವಡಿಸಲಾಗಿದ್ದು, ಸರಿಯಾಗಿ ನಿರ್ವಹಿಸಲಾಗುತ್ತಿದೆ",
        "english": "CCTV installed and properly maintained"
    },
    "cctv_installed_not_maintained": {
        "kannada": "ಸಿ.ಸಿ ಟಿ.ವಿ ಅಳವಡಿಸಲಾಗಿದ್ದು, ಸರಿಯಾದ ನಿರ್ವಹಣೆ ಇರುವುದಿಲ್ಲ",
        "english": "CCTV installed but not properly maintained"
    },
    "cctv_not_installed": {
        "kannada": "ಸಿ.ಸಿ ಟಿ.ವಿ ಅಳವಡಿಸಿರುವುದಿಲ್ಲ, ಹಾಗು ಅಳವಡಿಸುವಂತೆ ಮುಖ್ಯಕಾರ್ಯನಿರ್ವಾಹಕರಿಗೆ ಸೂಚಿಸಲಾಯಿತು",
        "english": "CCTV not installed, CEO was instructed to install it"
    },
    
    # AMCS software edit/delete options
    "amcs_edit_delete_options": {
        "kannada": "AMCS ಸಾಫ್ಟ್ ವೇರ್ ನಲ್ಲಿ EDIT ಮತ್ತು DELETE option ತೆಗೆದಿರುವ ಬಗ್ಗೆ",
        "english": "About EDIT and DELETE options in AMCS software"
    },
    "edit_delete_disabled": {
        "kannada": "EDIT ಮತ್ತು DELETE option ನಿಷ್ಕಿಯವಾಗಿರುತ್ತದೆ",
        "english": "EDIT and DELETE options are disabled"
    },
    "edit_delete_enabled": {
        "kannada": "EDIT ಮತ್ತು DELETE option ಸಕ್ರಿಯವಾಗಿರುತ್ತದೆ",
        "english": "EDIT and DELETE options are enabled"
    },
    
    # Other observations
    "other_observations": {
        "kannada": "ಇತರೆ ಗಮನಿಸಿದ ವಿಷಯಗಳು",
        "english": "Other observed issues"
    },
    "other_details": {
        "kannada": "ಇತರೆ ವಿವರ",
        "english": "Other details"
    },
    
    # Photo upload
    "photo_upload": {
        "kannada": "ಭಾವ ಚಿತ್ರವನ್ನು ಅಪ್ಲೋಡ್‌ ಮಾಡಿ",
        "english": "Upload photo"
    },
    "truck_sheet_photo": {
        "kannada": "ಟ್ರಕ್‌ ಶೀಟ್‌ ಭಾವ ಚಿತ್ರವನ್ನು ಅಪ್ಲೋಡ್‌ ಮಾಡಿ",
        "english": "Upload truck sheet photo"
    },
    "challan_sheet_photo": {
        "kannada": "ಚಲನ್ ಶೀಟ್‌ ಭಾವ ಚಿತ್ರವನ್ನು ಅಪ್ಲೋಡ್‌ ಮಾಡಿ",
        "english": "Upload challan sheet photo"
    },
    "purchase_sheet_photo": {
        "kannada": "ಖರೀದಿ ಶೀಟ್‌ ಭಾವ ಚಿತ್ರವನ್ನು ಅಪ್ಲೋಡ್‌ ಮಾಡಿ",
        "english": "Upload purchase sheet photo"
    },
    "bmc_building_photo": {
        "kannada": "ಬಿ.ಎಂ.ಸಿ ಕಟ್ಟಡದ ಭಾವಚಿತ್ರವನ್ನು ಅಪ್ಲೋಡ್‌ ಮಾಡಿ",
        "english": "Upload BMC building photo"
    },
    "cattle_feed_storage_photo": {
        "kannada": "ಪಶು ಆಹಾರ ದಾಸ್ತನು ಕೊಠಡಿ ಭಾವಚಿತ್ರವನ್ನು ಅಪ್ಲೋಡ್‌ ಮಾಡಿ",
        "english": "Upload cattle feed storage room photo"
    },
    "bmc_premises_photo": {
        "kannada": "ಬಿ.ಎಂ.ಸಿ ಆವರಣದ ಭಾವಚಿತ್ರವನ್ನು ಅಪ್ಲೋಡ್‌ ಮಾಡಿ",
        "english": "Upload BMC premises photo"
    },
    "team_visit_photo": {
        "kannada": "ಅನಿರೀಕ್ಷಿತ ಬೇಟಿ ನೀಡಿದ ಸದಸ್ಯರನ್ನೂಳಗೊಂಡ ತಂಡದ ಭಾವಚಿತ್ರವನ್ನು ಅಪ್ಲೋಡ್‌ ಮಾಡಿ",
        "english": "Upload photo of team members who made the surprise visit"
    },
    "photo_upload_note": {
        "kannada": "5 ಭಾವ ಚಿತ್ರವನ್ನು ಅಪ್ಲೋಡ್‌ ಮಾಡಬಹುದು",
        "english": "You can upload up to 5 photos"
    },
    
    # Form submission
    "submit_form": {
        "kannada": "ಫಾರ್ಮ್ ಸಲ್ಲಿಸಿ",
        "english": "Submit Form"
    },
    "clear_form": {
        "kannada": "ಫಾರ್ಮ್ ಅಳಿಸಿ",
        "english": "Clear Form"
    },
    "form_submit_success": {
        "kannada": "ಫಾರ್ಮ್ ಯಶಸ್ವಿಯಾಗಿ ಸಲ್ಲಿಸಲಾಗಿದೆ",
        "english": "Form submitted successfully"
    },
    
    # Reports page
    "collection_statistics": {
        "kannada": "ಹಾಲು ಸಂಗ್ರಹಣೆಯ ಅಂಕಿಅಂಶಗಳು",
        "english": "Milk Collection Statistics"
    },
    "avg_suppliers": {
        "kannada": "ಸರಾಸರಿ ಸರಬರಾಜುದಾರರು",
        "english": "Average Suppliers"
    },
    "member_percentage": {
        "kannada": "ಸದಸ್ಯರ ಶೇಕಡಾವಾರು",
        "english": "Member Percentage"
    },
    "data_table": {
        "kannada": "ದತ್ತಾಂಶ ಕೋಷ್ಟಕ",
        "english": "Data Table"
    },
    "download_csv": {
        "kannada": "CSV ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ",
        "english": "Download CSV"
    },
    "no_data_available": {
        "kannada": "ಯಾವುದೇ ದತ್ತಾಂಶ ಲಭ್ಯವಿಲ್ಲ",
        "english": "No data available"
    },
    "total_entries": {
        "kannada": "ಒಟ್ಟು ನಮೂದುಗಳು",
        "english": "Total Entries"
    },
    
    # Admin dashboard
    "admin_dashboard": {
        "kannada": "ಆಡಳಿತ ಡ್ಯಾಶ್‌ಬೋರ್ಡ್",
        "english": "Admin Dashboard"
    },
    "data_management": {
        "kannada": "ದತ್ತಾಂಶ ನಿರ್ವಹಣೆ",
        "english": "Data Management"
    },
    "user_management": {
        "kannada": "ಬಳಕೆದಾರ ನಿರ್ವಹಣೆ",
        "english": "User Management"
    },
    "system_settings": {
        "kannada": "ಸಿಸ್ಟಮ್ ಸೆಟ್ಟಿಂಗ್‌ಗಳು",
        "english": "System Settings"
    },
    "export_all_data": {
        "kannada": "ಎಲ್ಲಾ ದತ್ತಾಂಶವನ್ನು ರಫ್ತು ಮಾಡಿ",
        "english": "Export All Data"
    },
    "download_json": {
        "kannada": "JSON ಡೌನ್‌ಲೋಡ್ ಮಾಡಿ",
        "english": "Download JSON"
    },
    "select_entry_to_delete": {
        "kannada": "ಅಳಿಸಲು ನಮೂದನ್ನು ಆಯ್ಕೆಮಾಡಿ",
        "english": "Select Entry to Delete"
    },
    "delete_selected_entry": {
        "kannada": "ಆಯ್ಕೆಮಾಡಿದ ನಮೂದನ್ನು ಅಳಿಸಿ",
        "english": "Delete Selected Entry"
    },
    "entry_deleted": {
        "kannada": "ನಮೂದು ಯಶಸ್ವಿಯಾಗಿ ಅಳಿಸಲಾಗಿದೆ",
        "english": "Entry successfully deleted"
    },
    "error_deleting_entry": {
        "kannada": "ನಮೂದನ್ನು ಅಳಿಸುವಲ್ಲಿ ದೋಷ",
        "english": "Error deleting entry"
    },
    "user_management_info": {
        "kannada": "ಈ ವಿಭಾಗದಲ್ಲಿ ಬಳಕೆದಾರರನ್ನು ಸೇರಿಸಬಹುದು, ಸಂಪಾದಿಸಬಹುದು ಮತ್ತು ಅಳಿಸಬಹುದು.",
        "english": "In this section, you can add, edit and delete users."
    },
    "confirm_password": {
        "kannada": "ಪಾಸ್‌ವರ್ಡ್ ದೃಢೀಕರಿಸಿ",
        "english": "Confirm Password"
    },
    "user_role": {
        "kannada": "ಬಳಕೆದಾರ ಪಾತ್ರ",
        "english": "User Role"
    },
    "add_user": {
        "kannada": "ಬಳಕೆದಾರರನ್ನು ಸೇರಿಸಿ",
        "english": "Add User"
    },
    "user_added": {
        "kannada": "ಬಳಕೆದಾರರನ್ನು ಯಶಸ್ವಿಯಾಗಿ ಸೇರಿಸಲಾಗಿದೆ",
        "english": "User added successfully"
    },
    "system_settings_info": {
        "kannada": "ಈ ವಿಭಾಗದಲ್ಲಿ ನೀವು ಸಿಸ್ಟಮ್ ಸೆಟ್ಟಿಂಗ್‌ಗಳನ್ನು ಬದಲಾಯಿಸಬಹುದು.",
        "english": "In this section, you can change system settings."
    },
    "default_language": {
        "kannada": "ಡೀಫಾಲ್ಟ್ ಭಾಷೆ",
        "english": "Default Language"
    },
    "kannada": {
        "kannada": "ಕನ್ನಡ",
        "english": "Kannada"
    },
    "english": {
        "kannada": "ಇಂಗ್ಲಿಷ್",
        "english": "English"
    },
    "save_settings": {
        "kannada": "ಸೆಟ್ಟಿಂಗ್‌ಗಳನ್ನು ಉಳಿಸಿ",
        "english": "Save Settings"
    },
    "settings_saved": {
        "kannada": "ಸೆಟ್ಟಿಂಗ್‌ಗಳನ್ನು ಯಶಸ್ವಿಯಾಗಿ ಉಳಿಸಲಾಗಿದೆ",
        "english": "Settings saved successfully"
    }
}

def get_text(key):
    """Get text based on the current language"""
    if key not in translations:
        return key
    
    language = st.session_state.language if 'language' in st.session_state else 'kannada'
    return translations[key][language]


1.	auth.py - Authentication logic
import streamlit as st
import hashlib
import os
from translations import get_text

# This is a simple authentication system - in a production environment,
# you would implement more secure authentication methods

# Default admin credentials - in production, use environment variables
DEFAULT_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
DEFAULT_PASSWORD = os.getenv("ADMIN_PASSWORD", "dairy2023")

def hash_password(password):
    """Create a hash of the password"""
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(username, password):
    """Check if the provided username and password are correct"""
    hashed_password = hash_password(password)
    
    # In a real application, you would check against a secure database
    return username == DEFAULT_USERNAME and hash_password(DEFAULT_PASSWORD) == hashed_password

def login_form():
    """Render a login form and validate credentials"""
    st.subheader(get_text("login"))
    
    username = st.text_input(get_text("username"))
    password = st.text_input(get_text("password"), type="password")
    
    if st.button(get_text("login_button")):
        if check_password(username, password):
            return True
        else:
            st.error(get_text("login_error"))
    
    return False
