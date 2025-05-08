from google import genai
from google.genai import types

class DocumentService:
    def __init__(self):
        self.document_reader = genai.Client()
        self.prompt = """Hãy trích xuất các thông tin sau: Tên văn bản, số hiệu văn bản, các căn cứ, 
        chương, mục, điều luật, khoản, điểm, và các ý. Trong đó LƯU Ý các điểm sau để dễ phân biệt:
        - Tên văn bản thường được viết in đậm ở đầu mỗi văn bản.
        - Số hiệu nằm ở góc trên phía bên tay trái.
        - Các căn cứ được viết in nghiêng và ở ngay dưới tên văn bản.
        - Chương hay được viết bắt đầu bằng: Chương I, Chương II, ... và được in đậm
        - Mục hay được viết bắt đầu bằng: Mục 1, Mục 2, ... và được in đậm
        - Điều luật hay được viết bắt đầu bằng: Điều 1, Điều 2, ... và được in đậm
        - Khoản thường hay được đán ký hiệu đầu dòng theo số. 
        - Điểm thường hay được đánh ký hiệu đầu dòng theo chữ cái.
        - Các ý khác thường sử dụng dấu gạch đầu dòng, các ký hiệu khác hoặc không có gì tùy theo yêu cầu cụ thể của văn bản.
        Mỗi một thông tin trích xuất được cần được cách dòng.
        """
        
        
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