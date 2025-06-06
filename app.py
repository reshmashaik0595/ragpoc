from rag_pipeline import rag_answer
from ingest import ingest_text
import streamlit as st

st.set_page_config(
    page_title="Chat with us!",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <h2 style='
        color:#202A44;  
        font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 600;
        margin-bottom: 20px;
    '> 🚀 Chat with us!</h2>
    <hr/>
    """,
    unsafe_allow_html=True
)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "raw_text" not in st.session_state:
    st.session_state.raw_text = ""
if "query_input" not in st.session_state:
    st.session_state.query_input = ""

toggle = st.toggle("🔐 Switch to Admin Insert Mode")

def insert_text():
    if st.session_state.raw_text.strip():
        count = ingest_text(st.session_state.raw_text)
        st.success(f"Successfully inserted and embedded {count} chunks.")
        st.session_state.raw_text = ""
    else:
        st.warning("⚠️ Please paste some text before inserting.")

def submit_query():
    if st.session_state.query_input.strip():
        with st.spinner("Loading..."):
            answer = rag_answer(st.session_state.query_input)
        st.session_state.chat_history.append({"role": "user", "content": st.session_state.query_input})
        st.session_state.chat_history.append({"role": "bot", "content": answer})
        st.session_state.query_input = ""
    else:
        st.warning("⚠️ Please enter a question before submitting.")

if toggle:
    with st.expander("Insert Text"):
        st.text_area(
            label="Enter raw text ",
            key="raw_text",
            placeholder="Your text goes here",
            label_visibility="collapsed"
        )
        st.button("Insert", on_click=insert_text)

else:
    st.text_input(
        label="Ask anything ?",
        key="query_input",
        placeholder="Enter your query here",
        label_visibility="collapsed"
    )
    st.button("Submit Query", on_click=submit_query)

if toggle and not st.session_state.get("prev_toggle", False):
    st.session_state.chat_history = []

st.session_state.prev_toggle = toggle

for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.markdown(
            f"""
            <div style="background-color:#e6ffe6; padding:10px; border-radius:10px; margin-bottom:5px; max-width:70%; float:right;">
                <b>You:</b> {msg['content']}
            </div>
            <div style="clear: both;"></div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div style="background-color:#ECECEC; padding:10px; border-radius:10px; margin-bottom:5px; max-width:70%; float:left;">
                <img src="https://cdn-icons-png.flaticon.com/512/1998/1998592.png" width="28" style="margin-right:8px; vertical-align: middle;">
                <b>Bot:</b> {msg['content']}
            </div>
            <div style="clear: both;"></div>
            """,
            unsafe_allow_html=True,
        )
