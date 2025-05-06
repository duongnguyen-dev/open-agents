import streamlit as st

# ===== Constants =====
SUPPORTED_FILE_TYPES = ["pdf", "docx", "txt"]
DEFAULT_MODELS = ["BERT", "GPT-4", "RAG"]
DEFAULT_FEATURES = ["Tra cứu điều luật", "Tóm tắt văn bản", "Giải thích quy định"]
USER_ROLE = "user"
BOT_ROLE = "bot"

# ===== Sidebar: Model + Feature Selection =====
def render_sidebar_options():
    st.sidebar.header("⚙️ Tùy chọn")
    
    selected_model = st.sidebar.selectbox("🔍 Chọn mô hình:", DEFAULT_MODELS)
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

# ===== Main App =====
def main():
    st.title("📚 Chatbot Luật - Giao diện Demo")

    selected_model, selected_feature, uploaded_file = render_sidebar_options()
    initialize_chat_history()
    display_chat_history()

    user_input = st.text_input("Nhập câu hỏi hoặc điều luật bạn muốn hỏi:")
    send_button_clicked = st.button("📨 Gửi")

    if send_button_clicked:
        handle_message_submission(user_input, selected_model, selected_feature)

# ===== Entry Point =====
if __name__ == "__main__":
    main()
