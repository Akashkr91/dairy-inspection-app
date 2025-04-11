import streamlit as st
import hashlib
import os
from translations import get_text

# Default admin credentials - in production, use environment variables or secure storage
DEFAULT_USERNAME = os.getenv("ADMIN_USERNAME", "admin")
DEFAULT_PASSWORD = os.getenv("ADMIN_PASSWORD", "dairy2023")

def hash_password(password):
    """Create a hash of the password"""
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(username, password):
    """Check if the provided username and password are correct"""
    hashed_password = hash_password(password)
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
