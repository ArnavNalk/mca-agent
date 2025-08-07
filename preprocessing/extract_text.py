import fitz
import os

def extract_text_from_pdf(file_path):
    text = ""
    doc = fitz.open(file_path)
    for page in doc:
        text += page.get_text()
    return text

def extract_all_texts(folder_path):
    all_texts = []
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            path = os.path.join(folder_path, file)
            text = extract_text_from_pdf(path)
            all_texts.append({"filename": file, "text": text})
    return all_texts