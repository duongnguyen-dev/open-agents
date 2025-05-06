import streamlit as st

# ===== Constants =====
SUPPORTED_FILE_TYPES = ["pdf", "docx", "txt"]
AVAILABLE_MODELS = ["BERT", "GPT-4", "RAG"]
AVAILABLE_FEATURES = ["Legal Lookup", "Document Summarization", "Law Explanation"]
USER = "user"
BOT = "bot"

# ===== Sidebar Section =====
def render_sidebar_controls():
    st.sidebar.header("⚙️ Settings")

    selected_model = st.sidebar.selectbox("🔍 Select Model:", AVAILABLE_MODELS)
    selected_feature = st.sidebar.selectbox("🛠️ Select Feature:", AVAILABLE_FEATURES)
    uploaded_document = st.sidebar.file_uploader(
        "📄 Upload Legal Document", type=SUPPORTED_FILE_TYPES
    )

    return selected_model, selected_feature, uploaded_document

# ===== Chat History Initialization =====
def initialize_chat_session():
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

# ===== Display Chat Messages =====
def render_chat_history():
    st.subheader("💬 Chat Window")
    for sender, message in st.session_state.chat_history:
        sender_label = "🧑 You" if sender == USER else "🤖 Bot"
        st.markdown(f"**{sender_label}:** {message}")

# ===== Simulated Bot Response (Placeholder) =====
def get_mock_response(model: str, feature: str) -> str:
    return f"(🔁 Simulated response from {model} using feature: {feature})"

# ===== Process User Message =====
def process_user_message(message: str, model: str, feature: str):
    if not message.strip():
        return

    st.session_state.chat_history.append((USER, message))
    bot_reply = get_mock_response(model, feature)
    st.session_state.chat_history.append((BOT, bot_reply))
    st.experimental_rerun()

# ===== Main App =====
def main():
    st.title("📚 Legal Chatbot - Demo Interface")

    selected_model, selected_feature, uploaded_file = render_sidebar_controls()
    initialize_chat_session()
    render_chat_history()

    user_query = st.text_input("Enter your legal question:")
    is_submit_clicked = st.button("📨 Send")

    if is_submit_clicked:
        process_user_message(user_query, selected_model, selected_feature)

# ===== Entry Point =====
if __name__ == "__main__":
    main()
