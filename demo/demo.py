import streamlit as st
import httpx
import requests
from configs import *

# ===== Sidebar: Model + Feature Selection =====
def render_sidebar_options():
    st.sidebar.header("⚙️ Tùy chọn")
    
    selected_model = st.sidebar.selectbox("🔍 Chọn mô hình:", EMBEDDING_MODELS)
    selected_feature = st.sidebar.selectbox("🛠️ Chọn tính năng:", DEFAULT_FEATURES)
    uploaded_file = st.sidebar.file_uploader(
        "📄 Tải lên file văn bản luật", type=SUPPORTED_FILE_TYPES
    )
    
    return selected_model, selected_feature, uploaded_file

# ===== Chat History Initialization =====
def initialize_chat_session():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

# ===== Display Chat Messages =====
def render_chat_history():
    st.subheader("💬 Chat Window")
    for sender, message in st.session_state.chat_history:
        sender_label = "🧑 You" if sender == USER_ROLE else "🤖 bot"
        st.markdown(f"**{sender_label}:** {message}")

# ===== Main App =====
def main():
    st.title("📚 Legal Chatbot - Demo Interface")

    selected_model, selected_feature, uploaded_file = render_sidebar_options()
    initialize_chat_session()
    render_chat_history()

    user_input = st.text_input("Enter your legal question:")
    send_button_clicked = st.button("📨 Send")

    if send_button_clicked:
        with st.spinner("Generating response..."):
            response = requests.post(
                "http://127.0.0.1:8002//chat/generate",
                json={"user_input": user_input},
                stream=True
            )

            if response.status_code == 200:
                full_response = ""
                placeholder = st.empty()
                for chunk in response.iter_content():
                    print(chunk)
                    if chunk:
                        text_chunk = chunk.decode("utf-8")
                        full_response += text_chunk
                        placeholder.text(full_response)
            else:
                st.error(f"Error: {response.status_code}")
# ===== Entry Point =====
if __name__ == "__main__":
    main()
