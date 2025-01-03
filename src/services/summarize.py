import logging
import google.generativeai as genai
import json
from src.config.config import sys_prompt

logger = logging.getLogger(__name__)

genai.configure(api_key="AIzaSyABfSdfCdMdddCjw1fvBPzwN9tEo7E4OSM")

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