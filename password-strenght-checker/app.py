import streamlit as st
import re

# TITLE
st.title("🔐 Ultimate Password Strength Checker")

# DESCRIPTION
st.markdown("""
Welcome to the **Ultimate Password Strength Checker!**

We'll check your password for:
- ✅ Length (at least 8 characters)
- ✅ Upper & Lowercase letters
- ✅ Numbers
- ✅ Special Characters

*Improve your online security by using strong passwords!*
""")

# INPUT
password = st.text_input("Enter your password:", type="password")

# PASSWORD STRENGTH CHECK FUNCTION
def check_password_strength(password):
    score = 0
    feedback = []

    # LENGTH CHECK
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least **8 characters** long.")

    # UPPERCASE AND LOWERCASE LETTER CHECK
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include **both uppercase and lowercase** letters.")

    # DIGIT CHECK
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least **one number (0-9)**.")

    # SPECIAL CHARACTER CHECK
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least **one special character (!@#$%^&* etc.)**.")

    return score, feedback

# BUTTON
if st.button("🔍 Check Password Strength"):
    if password:
        score, feedback = check_password_strength(password)

        st.subheader("🔎 Password Strength Result:")
        if score == 4:
            st.success("✅ Strong Password! Your password is secure.")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below.")

        if feedback:
            st.info("💡 Suggestions to improve your password:")
            for tip in feedback:
                st.write("- " + tip)
    else:
        st.error("🚫 Please enter a password to check.")

# FOOTER
st.markdown("---")
st.markdown("Made with ❤ by **Aleeza Khan**")