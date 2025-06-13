from pypdf import PdfReader
import pyttsx3


reader = PdfReader('autobiography.pdf')
num_pages = len(reader.pages)

print(f"Total pages: {num_pages}")

for i in range(num_pages):
    page = reader.pages[i]
    text = page.extract_text()
    print(text)
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    engine.say(text)
    engine.runAndWait()