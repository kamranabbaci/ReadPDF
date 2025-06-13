from googletrans import Translator # Import the Translator
import os # To handle file paths
from pypdf import PdfReader

file = PdfReader('mytext.pdf')
num_pages = len(file.pages)
translator = Translator()
full_translated_text = ""

for i in range(num_pages):
    page = file.pages[i]
    text = page.extract_text()

    if text:
        print(f"Translating page {i + 1}...")
        # Translate text to Urdu ('ur')
        translated_segment = translator.translate(text, dest='ur').text
        full_translated_text += f"\n--- Page {i + 1} (Urdu) ---\n"
        full_translated_text += translated_segment
    else:
        full_translated_text += f"\n--- Page {i + 1} (No extractable text found) ---\n"

    print(full_translated_text)