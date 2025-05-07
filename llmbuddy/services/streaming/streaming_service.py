import streamlit as st
from langchain.callbacks.base import BaseCallbackHandler

class StreamlitStreamingService(BaseCallbackHandler):
    def __init__(self):
        super().__init__()
        self.container = st.empty()
        self.text = ""
    
    def on_llm_new_token(self, token: str, **kwargs):
        self.text += token 
        self.container.markdown(self.text)  