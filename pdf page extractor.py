import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader, PdfWriter
import os

def extract_pdf_pages(input_path, output_path, page_numbers):
    with open(input_path, 'rb') as file:
        reader = PdfReader(file)
        writer = PdfWriter()

        for page_number in page_numbers:
            page = reader.pages[page_number - 1]
            writer.add_page(page)

        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

def select_pdf_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    return file_path

def select_pdf_pages(input_path):
    root = tk.Tk()
    root.withdraw()

    page_numbers = []
    page_input = input("Enter page numbers to extract (separated by commas or ranges): ")
    page_input = page_input.replace(" ", "")  # Remove spaces

    for part in page_input.split(","):
        if "-" in part:
            start, end = part.split("-")
            if start.isdigit() and end.isdigit():
                page_numbers.extend(range(int(start), int(end) + 1))
        elif part.isdigit():
            page_numbers.append(int(part))

    return page_numbers



# Usage example
input_pdf_path = select_pdf_file()

if input_pdf_path:
    root = tk.Tk()
    root.withdraw()
    
    # Prompt the user to select the output directory
    output_directory = filedialog.askdirectory(title="Select Output Directory")
    if not output_directory:
        print("No output directory selected.")
        exit()

    # Prompt the user to enter the output filename
    output_filename = filedialog.asksaveasfilename(
        initialdir=output_directory,
        title="Save As",
        filetypes=[("PDF Files", "*.pdf")],
        defaultextension=".pdf"
    )
    if not output_filename:
        print("No output filename specified.")
        exit()

    output_pdf_path = os.path.join(output_directory, output_filename)

    page_numbers = select_pdf_pages(input_pdf_path)

    extract_pdf_pages(input_pdf_path, output_pdf_path, page_numbers)
    print(f"Selected pages extracted from '{input_pdf_path}' and saved as '{output_pdf_path}'.")
else:
    print("No PDF file selected.")
