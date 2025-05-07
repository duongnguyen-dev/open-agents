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

# ===== State Initialization =====
def initialize_chat_history():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

# ===== Display Chat Messages =====
def display_chat_history():
    st.subheader("💬 Khung Chat")
    for sender_role, message_text in st.session_state.chat_history:
        sender_name = "🧑 Bạn" if sender_role == USER_ROLE else "🤖 Bot"
        st.markdown(f"**{sender_name}:** {message_text}")

# ===== Generate Bot Response (Placeholder) =====
def generate_mock_response(model_name: str, feature_name: str) -> str:
    return f"(🔁 Trả lời giả lập từ {model_name} cho chức năng {feature_name})"

# ===== Handle Message Submission =====
def handle_message_submission(user_message: str, model: str, feature: str):
    if not user_message.strip():
        return
    
    st.session_state.chat_history.append((USER_ROLE, user_message))
    bot_response = generate_mock_response(model, feature)
    st.session_state.chat_history.append((BOT_ROLE, bot_response))
    st.experimental_rerun()  # Rerun to refresh chat display

async def fetch_stream(message: str):
    async with httpx.AsyncClient() as client:
        async with client.stream("POST", "http://127.0.0.1:8001/chat/generate", json={'user_input': message}) as response:
            async for line in response.aiter_lines():
                if line:
                    yield line

# ===== Main App =====
def main():
    st.title("📚 Chatbot Luật - Giao diện Demo")

    selected_model, selected_feature, uploaded_file = render_sidebar_options()
    initialize_chat_history()
    display_chat_history()

    user_input = st.text_input("Nhập câu hỏi hoặc điều luật bạn muốn hỏi:")
    send_button_clicked = st.button("📨 Gửi")

    if send_button_clicked:
        payload = {"user_input": user_input}
        response_container = st.empty()
        response_text = ""

        with requests.post('http://127.0.0.1:8001/chat/generate', json=payload, stream=True) as response:
            if response.status_code == 200:
                print(response.content)
                for chunk in response.iter_content(chunk_size=1):
                    if chunk:
                        token = chunk.decode('utf-8')
                        response_text += token
                        response_container.markdown(response_text)
                        
# ===== Entry Point =====
if __name__ == "__main__":
    main()
