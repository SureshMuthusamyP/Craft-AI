# Import necessary libraries
from dotenv import load_dotenv
import os
import google.generativeai as genai
from utility import prompt

# Load environment variables from a .env file
load_dotenv()

# Processor class for handling text generation
class Processor():
    def __init__(self, API_KEY: None|str = None) -> None:
        # If API_KEY is not provided, attempt to retrieve it from environment variables
        if API_KEY is None:
            API_KEY = os.getenv("API_KEY")
            assert API_KEY is not None, "Cannot Load API key"
        
        # Configure the Generative AI with the provided API key
        genai.configure(api_key=API_KEY)
        
        # Initialize the Generative Model ('gemini-pro')
        self.model = genai.GenerativeModel('gemini-pro')

    def craft(self, query: str, tone: str) -> str:
        # Convert tone to lowercase for consistent handling
        tone = tone.lower()
        
        # Retrieve the prompt associated with the selected tone
        sel_prompt = prompt[tone]
        
        # Generate content using the provided query and selected prompt
        response = self.model.generate_content([sel_prompt, query])

        # Print the generated content (for debugging purposes)
        print(response.text)

        # Return the generated text
        return response.text
