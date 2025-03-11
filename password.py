import streamlit as st
import re

# Page Configuration
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

# Custom CSS for Background
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #fbc2eb, #a6c1ee);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 10px 30px rgb(7, 7, 7);
        }
    </style>
""", unsafe_allow_html=True)

# Title and Introduction
st.title("🔐 Password Strength Checker!")
st.markdown("## Welcome to the Ultimate Password Strength Checker! 👋")
st.markdown("Check your password strength and get expert tips to make it stronger. Stay secure with our smart suggestions.")

# Input Field
password = st.text_input("Enter your Password", type="password")

feedback = []
score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ A password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both uppercase and lowercase letters.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")

    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (!@#$%^&*).")

    # Strength Feedback
    if score == 4:
        feedback.insert(0, "✅ Your password is strong! 🎉")
    elif score == 3:
        feedback.insert(0, "🟡 Your password is medium strength. It could be stronger.")
    else:
        feedback.insert(0, "🔴 Your password is weak. Please make it stronger.")

    # Display Feedback
    st.markdown("## Improvement Suggestions")
    for tip in feedback:
        st.write(tip)

else:
    st.info("Please enter your password to get started.")
