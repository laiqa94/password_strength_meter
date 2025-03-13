import streamlit as st
import re
import requests
import hashlib
import random
import string

def check_password_strength(password):
    if not password:
        return ("Empty", "#FF4B4B"), 0
    
    length = len(password) >= 8
    has_digit = bool(re.search(r"\d", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    
    score = sum([length, has_digit, has_upper, has_lower, has_special])
    
    strength_levels = {
        0: ("Empty", "#FF4B4B"),
        1: ("Very Weak", "#FF4B4B"),
        2: ("Weak", "#FF914B"),
        3: ("Moderate", "#FFD700"),
        4: ("Strong", "#4BB543"),
        5: ("Very Strong", "#008000"),
    }
    
    return strength_levels.get(score, ("Very Weak", "#FF4B4B")), score

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

st.set_page_config(page_title="🔒 Password Strength Checker", layout="centered")
st.title("🔐 Smart Password Strength Checker")

password = st.text_input("Enter your password", type="password")

if password:
    (strength, color), score = check_password_strength(password)
    st.markdown(f"### Strength: <span style='color:{color}; font-size:22px; font-weight:bold'>{strength}</span>", unsafe_allow_html=True)
    st.progress(score / 5 if score > 0 else 0.01)
    
    feedback = []
    if len(password) < 8: feedback.append("🔴 Use at least **8 characters** for better security.")
    if not re.search(r"\d", password): feedback.append("🔴 Add at least **one number**.")
    if not re.search(r"[A-Z]", password): feedback.append("🔴 Include an **uppercase letter**.")
    if not re.search(r"[a-z]", password): feedback.append("🔴 Include a **lowercase letter**.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): feedback.append("🔴 Use at least **one special character** (e.g., @, #, $).")
    
    if feedback:
        st.warning("🚀 Suggestions to Improve:")
        for tip in feedback:
            st.write(tip)
    else:
        st.success("✅ Your password is **secure!**")

if st.button("🔑 Generate Secure Password"):
    strong_password = generate_password(12)
    st.text_input("Your Secure Password:", strong_password)

st.markdown("### 🔑 **Tips for a Stronger Password**")
st.info("""
- ✅ Use **at least 8+ characters**.
- ✅ Mix **letters, numbers, and symbols**.
- ✅ Avoid **common words & patterns**.
- ✅ Use a **password manager** to store passwords securely.
""")
