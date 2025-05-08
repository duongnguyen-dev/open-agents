from dotenv import load_dotenv
from loguru import logger
from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface.llms import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from llmbuddy.services.llm.base_service import LLMService

load_dotenv()

class Phi4Service(LLMService):
    def __init__(self, model_path):
        super().__init__()

        if model_path == None:
            model_id = "microsoft/Phi-4-mini-reasoning"
            self.llm = AutoModelForCausalLM.from_pretrained(
                model_id,
                device_map="cpu",
                torch_dtype="auto",
                trust_remote_code=True,
            )
            self.tokenizer = AutoTokenizer.from_pretrained(model_id)
            
            self.pipeline = pipeline(
                "text-generation", 
                model=self.llm, 
                tokenizer=self.tokenizer, 
                max_new_tokens=32768,
                temperature=0.8,
                top_p=0.95,
                do_sample=True,
            )
            
            self.hf = HuggingFacePipeline(pipeline=self.pipeline)
        else:
            logger.error("We haven't support local model yet!")
            self.llm = None
        
    def generate_text(self, question: str):
        template = """Question: {question}
        Answer: Let's think step by step."""
        
        prompt = PromptTemplate.from_template(template)

        chain = prompt | self.hf 
        
        for chunk in chain.stream(question):
            yield chunk
        
        