# textbook_scanner.py
from PyPDF2 import PdfReader


class TextbookScanner:

    @staticmethod
    def scan_textbook(pdf_path: str) -> str:
        with open(pdf_path, 'rb') as pdf_file:
            pdf = PdfReader(pdf_file)

            text_content = ''
            for page in pdf.pages:
                text = page.extract_text()
                text_content += text.encode('utf-8', errors='ignore').decode('utf-8')

        return text_content
