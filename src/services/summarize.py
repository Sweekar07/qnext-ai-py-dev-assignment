import logging
import google.generativeai as genai
import json
from src.config.config import sys_prompt
from dotenv import load_dotenv
import os

logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=gemini_api_key)

# Function to interact with Gemini API
def summarize_transcript(company_name, transcript_text):
    try:
        # Interact with Google Generative AI
        model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
        result = model.generate_content(sys_prompt + f"\n\nInput: {transcript_text}\n\n")
        response_text = result.candidates[0].content.parts[0].text
        response_json = json.loads(response_text.replace("```json", "").replace("```", "").strip())
        response_json["company_name"] = company_name
        return response_json, None
    except Exception as e:
        logger.error(f"Error summarizing transcript: {e}")
        return None, str(e)