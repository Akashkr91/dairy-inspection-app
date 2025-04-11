import os
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Text, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import json

# Get the database URL from environment variables
DATABASE_URL = os.environ.get("DATABASE_URL")

# If DATABASE_URL is not set or empty, raise an error
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set. Please ensure the database is properly configured.")

# Create SQLAlchemy engine with SSL parameters
engine = create_engine(
    DATABASE_URL,
    connect_args={
        'sslmode': 'require',
        'connect_timeout': 30
    }
)

# Create a base class for declarative models
Base = declarative_base()

# Define the dairy entry model
class DairyEntry(Base):
    """Dairy collection center entry model"""
    __tablename__ = "dairy_entries"
    
    id = Column(Integer, primary_key=True)
    center_id = Column(String(50))
    center_name = Column(String(100))
    date_of_visit = Column(String(50))
    visit_time = Column(String(50))
    member_suppliers = Column(Integer)
    non_member_suppliers = Column(Integer)
    morning_milk_collected = Column(String(50))
    evening_milk_collected = Column(String(50))
    average_fat = Column(String(50))
    average_snf = Column(String(50))
    
    # Account maintenance
    account_maintenance = Column(String(100))
    
    # CCTV installation
    cctv_installation = Column(String(100))
    
    # AMCS software
    amcs_edit_delete_options = Column(String(100))
    
    # Other fields
    adulteration_details = Column(JSON)
    milk_testing_equipment = Column(JSON)
    rejected_milk_details = Column(Text)
    fssai_license = Column(String(100))
    cattle_feed_license = Column(String(100))
    other_details = Column(Text)
    
    # Photo references
    truck_sheet_photo = Column(String(255), nullable=True)
    challan_sheet_photo = Column(String(255), nullable=True)
    purchase_sheet_photo = Column(String(255), nullable=True)
    bmc_building_photo = Column(String(255), nullable=True)
    cattle_feed_storage_photo = Column(String(255), nullable=True)
    bmc_premises_photo = Column(String(255), nullable=True)
    team_visit_photo = Column(String(255), nullable=True)
    
    timestamp = Column(DateTime, default=datetime.now)

# Create all tables
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)

def add_entry(entry_data):
    """
    Add a new entry to the database
    
    Args:
        entry_data (dict): Form data to be saved
    
    Returns:
        bool: Success status
    """
    try:
        # Create a new database session
        session = Session()
        
        # Process data for database storage
        dairy_entry = DairyEntry()
        
        # Process basic fields
        form_prefix = "form_"
        for key, value in entry_data.items():
            # Skip the form_ prefix to match column names
            if key.startswith(form_prefix):
                attribute_name = key[len(form_prefix):]
                
                # Special handling for JSON fields
                if attribute_name == "adulteration_details" or attribute_name == "milk_testing_equipment":
                    if isinstance(value, list):
                        setattr(dairy_entry, attribute_name, json.dumps(value))
                    else:
                        setattr(dairy_entry, attribute_name, json.dumps([]))
                else:
                    # Only set attributes that exist in the model
                    if hasattr(dairy_entry, attribute_name):
                        setattr(dairy_entry, attribute_name, value)
        
        # Add timestamp
        dairy_entry.timestamp = datetime.now()
        
        # Add to database
        session.add(dairy_entry)
        session.commit()
        
        # Close session
        session.close()
        
        return True
    except Exception as e:
        st.error(f"Error saving data to database: {e}")
        return False

def get_entries():
    """
    Get all entries from the database
    
    Returns:
        list: List of entries as dictionaries
    """
    try:
        # Create a new database session
        session = Session()
        
        # Query all entries
        entries = session.query(DairyEntry).all()
        
        # Convert to list of dictionaries
        result = []
        for entry in entries:
            entry_dict = {c.name: getattr(entry, c.name) for c in entry.__table__.columns}
            
            # Special handling for JSON fields
            if entry_dict.get('adulteration_details') and isinstance(entry_dict['adulteration_details'], str):
                entry_dict['adulteration_details'] = json.loads(entry_dict['adulteration_details'])
            
            if entry_dict.get('milk_testing_equipment') and isinstance(entry_dict['milk_testing_equipment'], str):
                entry_dict['milk_testing_equipment'] = json.loads(entry_dict['milk_testing_equipment'])
            
            result.append(entry_dict)
        
        # Close session
        session.close()
        
        return result
    except Exception as e:
        st.error(f"Error retrieving data from database: {e}")
        return []

def delete_entry(entry_id):
    """
    Delete an entry from the database
    
    Args:
        entry_id (int): ID of the entry to delete
    
    Returns:
        bool: Success status
    """
    try:
        # Create a new database session
        session = Session()
        
        # Find the entry
        entry = session.query(DairyEntry).filter(DairyEntry.id == entry_id).first()
        
        if entry:
            # Delete the entry
            session.delete(entry)
            session.commit()
            session.close()
            return True
        else:
            session.close()
            return False
    except Exception as e:
        st.error(f"Error deleting entry from database: {e}")
        return False

def get_data_as_dataframe():
    """
    Get all entries as a pandas DataFrame
    
    Returns:
        DataFrame: Pandas DataFrame with all entries
    """
    entries = get_entries()
    if entries:
        return pd.DataFrame(entries)
    return pd.DataFrame()

def migrate_from_json():
    """
    Migrate data from JSON file to database
    
    Returns:
        bool: Success status
    """
    try:
        # Check if JSON file exists
        json_file = "dairy_collection_data.json"
        if os.path.exists(json_file):
            # Load data from JSON file
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Add each entry to database
            for entry in data:
                add_entry(entry)
            
            return True
        return False
    except Exception as e:
        st.error(f"Error migrating data from JSON: {e}")
        return False

# Run migration if this file is executed directly
if __name__ == "__main__":
    migrate_from_json()
