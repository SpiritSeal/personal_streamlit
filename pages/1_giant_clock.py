import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
import time
from utils import hide_streamlit_style

st.set_page_config(
    page_title="Giant Clock",
    page_icon="🕰️",
    layout="wide",
)

def display_info():
    st.title("Giant Clock")
    st.write("Click the time to fullscreen it!")

def display_todo():
    todo = """
    *TODO: Add options to show/ hide date and seconds*
    """
    st.markdown(todo)

def server_time():
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        st.write(f'<div class="clock">{current_time}</div>', unsafe_allow_html=True)

        # Sleep for a second to update the time
        time.sleep(1)


def client_time():
    # st.title("Giant Clock App")
    hide_streamlit_style()
    with open('./html/1_giant_clock.html') as file:
        data = file.read()
    st.components.v1.html(data, height=450, scrolling=True)

def main():
    display_info()
    display_todo()
    client_time()


if __name__ == "__main__":
    main()
