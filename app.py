import streamlit as st
import cohere
from chatbot import MedicalChatBot


COHERE_API_KEY = "leKGpK1kojv9JIOqduGjiJfevBphofbWMmfRyQrj"
CREATIVITY = 0

uploaded_files = st.sidebar.file_uploader("Upload image", type=['png', 'jpg', 'pdf'], accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        print(uploaded_file)
        if uploaded_file.type.startswith('image'):
            st.sidebar.image(uploaded_file.getvalue())


st.title("Cohere clone")

co = cohere.Client(COHERE_API_KEY)
st.session_state.bot = MedicalChatBot(COHERE_API_KEY, uploaded_files)

if "cohere_model" not in st.session_state:
    st.session_state["cohere_model"] = "command"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["message"])


if prompt := st.chat_input("What is up?"):
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        full_response = st.session_state.bot.query(prompt)
        for response in co.chat(
            message=prompt,
            model=st.session_state["cohere_model"],
            chat_history=[
                {"role": m["role"], "message": m["message"]}
                for m in st.session_state.messages
            ],
            stream=True
        ):
            if response.event_type == 'text-generation':
                full_response += (response.text)
                message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "user", "message": prompt})
    st.session_state.messages.append({"role": "assistant", "message": full_response})