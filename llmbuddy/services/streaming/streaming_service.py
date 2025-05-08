from langchain.callbacks.base import BaseCallbackHandler

class StreamingCallback(BaseCallbackHandler):
    def __init__(self):
        super().__init__()
    
    def on_llm_new_token(self, token: str, **kwargs):
        yield token