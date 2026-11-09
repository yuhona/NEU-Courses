import os

import streamlit as st
from openai import OpenAI

# Must match the model pulled in entrypoint.sh (e.g. `ollama pull llama3.2`)
MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2")
OLLAMA_PORT = os.environ.get("OLLAMA_PORT", "11434")

# Ollama exposes an OpenAI-compatible API; the key is ignored but must be non-empty
client = OpenAI(base_url=f"http://localhost:{OLLAMA_PORT}/v1", api_key="ollama")

DEFAULT_SYSTEM_PROMPT = "You are a helpful assistant."
GREETING = {"role": "assistant", "content": "How can I help you?"}

st.set_page_config(page_title="Ollama Chatbot", page_icon="🤖")

with st.sidebar:
    name = st.text_input("What's your name?", value="")
    st.markdown(f"**Model:** `{MODEL}`")
    temperature = st.slider("Temperature", 0.0, 1.5, 0.7, 0.05)
    system_prompt = st.text_area("System prompt", value=DEFAULT_SYSTEM_PROMPT)
    if st.button("Clear chat"):
        st.session_state.messages = [GREETING]
        st.rerun()

st.title(f"Hi there, {name or 'friend'} 👋")
st.caption(f"🚀 A Streamlit chatbot powered by {MODEL} via Ollama")

if "messages" not in st.session_state:
    st.session_state.messages = [GREETING]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("Your message"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=MODEL,
            temperature=temperature,
            messages=[{"role": "system", "content": system_prompt}]
            + [m for m in st.session_state.messages if m is not GREETING],
            stream=True,
        )
        reply = st.write_stream(
            chunk.choices[0].delta.content or "" for chunk in stream
        )
    st.session_state.messages.append({"role": "assistant", "content": reply})
