import os
import PyPDF2
import logging

logger = logging.getLogger(__name__)

def get_pdf_files():
    directory = os.path.join("src", "documents")
    pdf_files = {}
    if os.path.exists(directory):
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".pdf"):
                    pdf_files[file] = os.path.join(root, file)
    return pdf_files

def extract_text_from_pdf(file_path):
    text = ""
    try:
        with open(file_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page in reader.pages:
                text += page.extract_text()
    except Exception as e:
        logger.warning(f"Error reading PDF: {e}")
    return text
