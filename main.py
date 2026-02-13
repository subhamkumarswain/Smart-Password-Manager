import streamlit as st
from auth import verify_master_password, set_master_password
from password_generator import generate_password
from strength_checker import check_strength
from password_store import save_password, retrieve_password, update_password, delete_password



st.set_page_config(page_title="Smart Password Manager", page_icon="🔐")

st.title("🔐 Smart Password Manager")

# ---------------------------
# MASTER PASSWORD SETUP
# ---------------------------

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "master_exists" not in st.session_state:
    import os
    st.session_state.master_exists = os.path.exists("master.hash")

# If master password not set
if not st.session_state.master_exists:
    st.subheader("Set Master Password")
    new_pass = st.text_input("Create Master Password", type="password")

    if st.button("Set Password"):
        if new_pass:
            set_master_password(new_pass)
            st.success("Master Password Set Successfully ✅")
            st.session_state.master_exists = True
        else:
            st.error("Password cannot be empty")

# If master exists but not authenticated
elif not st.session_state.authenticated:
    st.subheader("Login")
    password = st.text_input("Enter Master Password", type="password")

    if st.button("Login"):
        if verify_master_password(password):
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Access Denied ❌")

# If authenticated
else:
    st.success("Logged in successfully 🎉")

    st.header("Generate Secure Password")

    length = st.slider("Select Password Length", 8, 32, 12)

    if st.button("Generate Password"):
        generated = generate_password(length)
        st.session_state.generated_password = generated

    if "generated_password" in st.session_state:
        st.code(st.session_state.generated_password)
        st.write("Strength:", check_strength(st.session_state.generated_password))

        st.divider()
        st.header("Save Password")

        website = st.text_input("Website Name")
        username = st.text_input("Username / Email")

        if st.button("Save Password"):
            save_password(
                website,
                username,
                st.session_state.generated_password
            )
            st.success("Password Saved Successfully ✅")

        st.divider()
        st.header("Retrieve Password")

        search_site = st.text_input("Enter Website to Retrieve")

        if st.button("Retrieve"):
            data = retrieve_password(search_site)

            if data:
                st.write("Username:", data["username"])
                st.code(data["password"])
            else:
                st.error("No password found for this website")



