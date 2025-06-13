import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfReader
from googletrans import Translator
import os

def translate_pdf_to_urdu(pdf_path, output_dir="translated_pdfs"):
    try:
        reader = PdfReader(pdf_path)
        translator = Translator()

        full_translated_text = ""
        
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        base_name = os.path.basename(pdf_path)
        name_without_ext = os.path.splitext(base_name)[0]
        translated_txt_filename = os.path.join(output_dir, f"{name_without_ext}_urdu.txt")

        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                print(f"Translating page {i + 1}...") # This will print to console, not GUI
                translated_segment = translator.translate(text, dest='ur').text
                full_translated_text += f"\n--- Page {i + 1} (Urdu) ---\n"
                full_translated_text += translated_segment
            else:
                full_translated_text += f"\n--- Page {i + 1} (No extractable text found) ---\n"
        
        with open(translated_txt_filename, 'w', encoding='utf-8') as f:
            f.write(full_translated_text)
        
        return translated_txt_filename

    except FileNotFoundError:
        raise FileNotFoundError(f"PDF file not found at '{pdf_path}'")
    except Exception as e:
        raise Exception(f"An error occurred during translation or saving: {e}")

# --- GUI Application ---
class PDFTranslatorApp:
    def __init__(self, master):
        self.master = master
        master.title("PDF to Urdu Translator")

        self.pdf_path = tk.StringVar()
        self.output_status = tk.StringVar()
        self.output_status.set("Select a PDF to begin.")

        # PDF File Selection
        self.label_pdf = tk.Label(master, text="Select PDF File:")
        self.label_pdf.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_pdf = tk.Entry(master, textvariable=self.pdf_path, width=50)
        self.entry_pdf.grid(row=0, column=1, padx=10, pady=10)

        self.btn_browse = tk.Button(master, text="Browse", command=self.browse_pdf)
        self.btn_browse.grid(row=0, column=2, padx=10, pady=10)

        # Translate Button
        self.btn_translate = tk.Button(master, text="Translate to Urdu", command=self.start_translation)
        self.btn_translate.grid(row=1, column=0, columnspan=3, pady=20)

        # Status Label
        self.status_label = tk.Label(master, textvariable=self.output_status, fg="blue")
        self.status_label.grid(row=2, column=0, columnspan=3, pady=10)

    def browse_pdf(self):
        filename = filedialog.askopenfilename(
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        if filename:
            self.pdf_path.set(filename)
            self.output_status.set(f"Selected: {os.path.basename(filename)}")

    def start_translation(self):
        pdf_file = self.pdf_path.get()
        if not pdf_file:
            messagebox.showwarning("Input Error", "Please select a PDF file first.")
            return

        self.output_status.set("Translating... Please wait.")
        self.master.update_idletasks() # Update the GUI immediately

        try:
            translated_file_path = translate_pdf_to_urdu(pdf_file)
            if translated_file_path:
                self.output_status.set(f"Translation complete! Saved to: {os.path.basename(translated_file_path)}")
                messagebox.showinfo("Success", f"PDF translated successfully!\nSaved to: {translated_file_path}")
            else:
                self.output_status.set("Translation failed.")
                messagebox.showerror("Error", "Translation failed. Check console for details.")
        except Exception as e:
            self.output_status.set(f"Error: {e}")
            messagebox.showerror("Translation Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFTranslatorApp(root)
    root.mainloop()