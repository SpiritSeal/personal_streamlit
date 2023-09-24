import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    page_icon="👋",
)

def main():
    st.title("Dashboard")
    st.sidebar.markdown('# Landing Page')
    st.write("This is the app Dashboard!")


if __name__ == "__main__":
    main()