# Import necessary libraries
import streamlit as st
from utility import prompt
from processor import Processor

# Initialize Processor object
processor = Processor()

# Define tones and their descriptions
tones = {
    'Grammar Guide': "Precision in correcting grammar, spelling, and anomalies, ensuring clear and accurate written communication with a focus on style consistency",
    'Ambiguity Resolver': "Enhances text by identifying and resolving ambiguity in sentence structure, references, and expressions. Precision in suggestions ensures clarity while preserving the original intent and context.",
    'Smart Summarizer': "Creates concise, clear, and unbiased summaries, emphasizing essential content and addressing ambiguity."
}

# Configure Streamlit page settings
st.set_page_config(
    page_title="Craft AI",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Main title and subheader
st.markdown("<h1 style='text-align: center; font-size: 2.9em;'>Your writing, Expertly Crafted</h1>", unsafe_allow_html=True)
st.subheader("")

# Sidebar content
with st.sidebar:
    # Craft AI title and description
    st.markdown("<h1 style='text-align: center; font-size: 3.5em;'>Craft <span style='color: red;'>AI</span></h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='font-size: 1.14em;'>It's your ultimate writing powerup! Polish prose, condense text, and banish ambiguity with lightning speed. From grammar guru to clarity master, write smart, clear, and confident. Unleash your writing potential, one sentence at a time.</p>",
        unsafe_allow_html=True
    )
    # Dropdown for selecting feature/tone
    selected_tone = st.selectbox("Feature selection", tones)

# Display selected tone and its description
st.subheader(selected_tone)
st.markdown(
    f"<p style='font-size: 1.14em;'>{tones[selected_tone]}</p>",
    unsafe_allow_html=True
)

# Text input area
st.markdown("Enter your text here:")
input_text = st.text_area(label="Enter the text:", height=70, label_visibility='collapsed')

# Button to trigger text processing
if st.button("Craft Text"):
    try:
        # Process input text based on selected tone
        redrafted_text = processor.craft(input_text, selected_tone)
        
        # Display the redrafted text
        st.markdown(f"<div class='content'>{redrafted_text}</div>", unsafe_allow_html=True)

    except Exception as e:
        # Display error message if an exception occurs
        st.error("An error occurred: " + str(e))
