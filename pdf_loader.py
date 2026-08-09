import pypdf

def extract_text_from_pdfs(pdf_files):
    documents = []
    for pdf_file in pdf_files:
        try:
            pdf_reader = pypdf.PdfReader(pdf_file)
            full_text = ""
            for page_num, page in enumerate(pdf_reader.pages):
                text = page.extract_text()
                if text:
                    full_text += f"\n--- Page {page_num + 1} ---\n" + text
            
            if full_text.strip():
                documents.append({"filename": pdf_file.name, "content": full_text})
        except Exception as e:
            print(f"Error loading {pdf_file.name}: {e}")
            
    return documents
