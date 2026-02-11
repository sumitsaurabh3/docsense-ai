from pypdf import PdfReader
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data")

def load_documents(data_path=DATA_PATH):
    documents = []

    for file in os.listdir(data_path):
        if file.endswith(".pdf"):
            reader = PdfReader(os.path.join(data_path, file))
            for page_num, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    documents.append({
                        "text": text,
                        "source": file,
                        "page": page_num + 1
                    })

    return documents


if __name__ == "__main__":
    docs = load_documents()
    print("Number of documents loaded:", len(docs))
    if docs:
        print(docs[0])
