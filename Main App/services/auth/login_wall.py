import streamlit as st


def render_login_wall():
    if st.session_state.get("user_id") is not None:
        return True
    
    st.title("RepCheck 💪")
    st.markdown("### Welcome! Please enter your details to start.")

    with st.form("login_form", clear_on_submit=False):
        username = st.text_input("Name (unique)", placeholder="e.g. Anadhya")
        weight = st.number_input("Your Weight (kg)", min_value=30, max_value=200, value=70, step=1)
        submit_button = st.form_submit_button("Start Session", width="stretch")

    if submit_button:
        if not username:
            st.error("Name cannot be empty.")
            return False
        
        st.session_state["username"] = username
        st.session_state["user_id"] = 1
        st.session_state["weight_kg"] = weight

        st.rerun()

    return False