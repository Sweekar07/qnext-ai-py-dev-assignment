from flask import request, jsonify
from src.services.summarize import summarize_transcript
from src.services.file_utils import extract_text_from_pdf, get_pdf_files
import logging

# Configure logger
logger = logging.getLogger(__name__)


def initialize_routes(app):

    # Default Home Route
    @app.route('/', methods=['GET'])
    def home():
        return jsonify({"message": "Welcome to the Home Page!"}), 200


    # Route to list PDF files
    @app.route('/list_pdfs', methods=['GET'])
    def list_pdfs():
        try:
            pdf_files = get_pdf_files()
            if not pdf_files:
                return jsonify({"message": "No PDF files found"}), 200
        except Exception as e:
            logger.error(f"Error listing PDF files: {e}")
            return jsonify({"error": "Error listing PDF files"}), 500
        else:
            return jsonify({
                "Message": "Here are the list of available PDFs.",
                "pdf_files": pdf_files,
            }), 200

        
    # Route for the earnings transcript summary API
    @app.route('/earnings_transcript_summary', methods=['POST', 'GET'])
    def earnings_transcript_summary():
        try:
            if request.method == 'GET':
                company_name = request.args.get("company_name", "")
                transcript_text = request.args.get("transcript_text", "")
            elif request.method == 'POST':
                data = request.get_json()
                company_name = data.get("company_name", "")
                transcript_text = data.get("transcript_text", "")
            
            pdf_files = get_pdf_files()
            if company_name not in pdf_files:
                return jsonify({"error": "Company name not found!"}), 400
            
            transcript_text = extract_text_from_pdf(pdf_files[company_name])
            summary, error = summarize_transcript(company_name, transcript_text)
            
            if error:
                return jsonify({"error": f"Processing error: {error}"}), 500
        except Exception as e:
            logger.error(f"API Error: {e}")
        else:
            return jsonify(summary), 200
    