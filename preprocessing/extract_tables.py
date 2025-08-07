import pdfplumber
import os

def extract_tables_from_pdf(file_path):
    table_texts = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            for table in tables:
                table_texts.append(convert_table_to_text(table))
    return "\n\n".join(table_texts)

def convert_table_to_text(table):
    if not table:
        return ""
    lines = []
    header = table[0]
    header = [str(cell).strip() if cell else "" for cell in header]
    lines.append(" | ".join(header))
    lines.append("-" * len(" | ".join(header)))
    for row in table[1:]:
        row = [cell.strip() if cell else "" for cell in row]
        lines.append(" | ".join(row))
    return "\n".join(lines)

def extract_all_tables(folder_path):
    all_tables = []
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            path = os.path.join(folder_path, file)
            tables = extract_tables_from_pdf(path)
            all_tables.append({"filename": file, "tables": tables})
    return all_tables