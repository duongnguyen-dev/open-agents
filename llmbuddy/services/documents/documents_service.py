from google import genai
from google.genai import types

class DocumentService:
    def __init__(self):
        self.document_reader = genai.Client()
        
        self.prompt = "Answer user question based on the provided context."
        
    def read_document(self, doc_data):
        response = self.document_reader.models.generate_content(
            model = "gemini-2.0-flash",
            contents=[
                types.Part.from_bytes(
                    data = doc_data,
                    mime_type="application/pdf",
                ),
                self.prompt
            ]
        )
    
        return response.text