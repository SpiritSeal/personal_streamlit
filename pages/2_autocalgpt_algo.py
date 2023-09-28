import streamlit as st
from utils import hide_streamlit_style
import openai

'''
TODO:
- Clean up the code
- Parse date and time events to be in the format that Google Calendar accepts
    - Then actually make a button that adds the event to Google Calendar
[
    See:
    - https://support.google.com/calendar/thread/128416249/calendar-url-generator-which-parameters?hl=en
    - https://developers.google.com/calendar/api/v3/reference/events/i
    - https://github.com/InteractionDesignFoundation/add-event-to-calendar-docs/blob/main/services/google.mdnsert
]
- Clean up/ modularize the code so that the prompts are all in one place
    - Mb use a langchain implementation?


Later:
- iCal/ etc integration
'''



st.set_page_config(
    page_title="Autocalendar GPT Algorithm",
    page_icon="📅",
    # layout="wide",
)

@st.cache_data
def queryCalenbot(input_text:str, prompt:str) -> str:
    # Create a chatbot using ChatCompletion.create() function
    completion = openai.ChatCompletion.create(
        # Use GPT 3.5 as the LLM
        model="gpt-3.5-turbo",
        # Pre-define conversation messages for the possible roles
        messages=[
            {"role": "system", "content": "You are a helpful assistant that parses text and generates calendar entries. Here is the information you have been provided with:\n"+input_text},
            {"role": "user", "content": prompt}
        ]
    )
    print("API was recalled!")
    return completion.choices[0].message["content"]

def extract_angle_features(input_text:str) -> str:
    # Takes in a string and returns the first text enclosed in angle brackets
    # Example: "Hello, my name is <John> and I am <20> years old." -> "John"
    for i in range(len(input_text)):
        if input_text[i] == "<":
            j = i+1
            while input_text[j] != ">":
                j += 1
            return input_text[i+1:j]

def main():
    st.title("Autocalendar GPT Algorithm")
    st.write("Set OpenAI API key: ")
    openai.api_key = st.text_input("API Key:", type="password")
    input_text = st.text_area("Enter the text you want to calenderize:")
    st.write("Original Prompt:")
    input_text


    st.header("Calenderization of Prompt:")
    # Event Title
    event_title = queryCalenbot(input_text,"Generate an event title with no other text.")
    st.markdown(f'Event Title: :red[{event_title}]')
    
    # Event Start Date
    event_start_date_raw = queryCalenbot(input_text,"What is the event start date? Tell me only the date in angle brackets. If you don't know the date, just say 'None'.")
    event_start_date = extract_angle_features(event_start_date_raw)
    st.markdown(f'Event Date: :red[{event_start_date}]')

    # Event End Date
    event_end_date_raw = queryCalenbot(input_text,"What is the event end date? Tell me only the date in angle brackets. If you don't know the date, just say 'None'.")
    event_end_date = extract_angle_features(event_end_date_raw)
    st.markdown(f'Event End Date: :red[{event_end_date}]')
    
    # Event Time
    event_start_time_raw = queryCalenbot(input_text,"What is the event start time? Tell me only the time in angle brackets. If you don't know the time, just say 'None'.")
    event_start_time = extract_angle_features(event_start_time_raw)
    st.markdown(f'Event Start Time: :red[{event_start_time}]')
    
    # Event End Time
    event_end_time_raw = queryCalenbot(input_text,"What is the event end time? Tell me only the time in angle brackets. If you don't know the time, just say 'None'.")
    event_end_time = extract_angle_features(event_end_time_raw)
    st.markdown(f'Event End Time: :red[{event_end_time}]')


if __name__ == "__main__":
    # hide_streamlit_style()
    main()