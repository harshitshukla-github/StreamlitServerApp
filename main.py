import sqlite3

import streamlit as st

from database import add_user, create_table, verify_user

# Create the user table
create_table()

def main():
    st.set_page_config(page_title="Server Purchase App", layout="centered")

    st.title("Server Purchase App")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        marketplace(st.session_state.username)
    else:
        menu = ["Login", "Sign Up"]
        choice = st.sidebar.selectbox("Menu", menu)

        if choice == "Login":
            login()
        elif choice == "Sign Up":
            signup()

def login():
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        user = verify_user(username, password)
        if user:
            st.success(f"Logged In as {username}")
            st.session_state.logged_in = True
            st.session_state.username = username
        else:
            st.error("Username or password is incorrect")

def signup():
    st.subheader("Create New Account")

    new_username = st.text_input("Enter Username")
    new_password = st.text_input("Enter Password", type='password')
    confirm_password = st.text_input("Confirm Password", type='password')

    if st.button("Sign Up"):
        if new_password == confirm_password:
            try:
                add_user(new_username, new_password)
                st.success("You have successfully created an account")
                st.info("Go to Login Menu to login")
            except sqlite3.IntegrityError:
                st.error("Username already taken, please choose a different one.")
        else:
            st.warning("Passwords do not match")

def marketplace(username):
    st.subheader("Marketplace")
    st.write("Welcome to the CPU/GPU server marketplace!")
    st.image("src/image01.png", width=100)  # Adjust width as needed
    col1, col2 = st.columns(2)
    with col1:
        st.text(f"Member Name: {username}")
    with col2:
        st.text("CPU Stats")
        st.text_input("CPU Stats", value="16 Cores, 3.5GHz")
    col3, col4 = st.columns(2)
    with col3:
        st.text("GPU Stats")
        st.text_input("GPU Stats", value="NVIDIA RTX 3080, 10GB VRAM")
    st.button("BUY MORE CPU")
    st.slider("CPU Amount", min_value=0, max_value=100, value=50)
    st.button("BUY MORE GPU")
    st.slider("GPU Amount", min_value=0, max_value=100, value=50)


if __name__ == '__main__':
    main()