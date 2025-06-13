PDF to Urdu Translator
A simple yet effective Python application that extracts text from PDF files, translates it into Urdu, and saves the translated content as a plain text file. This tool is perfect for quickly getting the gist of PDF documents in Urdu.

Features
PDF Text Extraction: Reliably extracts text content from each page of a PDF document.
Urdu Translation: Utilizes Google Translate to translate the extracted English (or other source language) text into Urdu.
Plain Text Output: Saves the translated content into a .txt file, preserving page breaks for readability.
User-Friendly GUI: Features a simple graphical interface (Tkinter) for easy file selection and translation initiation.
How It Works
The application performs the following steps:

A user selects a PDF file through the GUI.
The application reads the PDF page by page using pypdf.
For each page, the extracted text is sent to the Google Translate service via googletrans-py to be translated into Urdu.
The translated text from all pages is compiled and saved into a new .txt file in a dedicated translated_pdfs directory.
