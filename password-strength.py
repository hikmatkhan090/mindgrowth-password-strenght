import streamlit as st
import  re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title("🔐Password Strength Checker By Hikmat khan")
st.markdown("""
## Welcome to Password Strength Checker!🥳
Use this tool to check the strength of your password and make it more secure.
            we will give you helpful tips to create a **Strong Password**🔏""")

password = st.text_input("Enter your password", type="password")

feedback = []

score = 0

if password :
    if len (password) < 8:
        score += 1
    else :
        feedback.append("❌ Password should be at least 6 characters Long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else :
        feedback.append("❌ Password should contain both uppercase and lowercase letters.")
    

    if re.search(r"\d", password):
        score += 1
    else :
        feedback.append("❌ Password should contain atleast one digit number.") 

    if re.search(r"[!@#$-%]", password):
        score += 1
    else :
        feedback.append("❌ Password should contain atleast one special character.")
    if score == 4:
        feedback.append("✅ Password is strong!🏴‍☠️")
    elif score == 3:
        feedback.append("🟡 Password is medium strength. It could be stronger!🔐")
    else :
        feedback.append("🔴 Password is weak. please make it sronger!🔓")

    if feedback:
        st.markdown("## Improvement Tips:")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Enter a password to get started⏳.")


    
