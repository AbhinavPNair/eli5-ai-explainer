import os
import streamlit as st
from groq import Groq

# 🔧 Fix for watchdog crash in some Streamlit deployments
os.environ["STREAMLIT_WATCHDOG_MODE"] = "poll"

# ✅ Use secrets — NOT dotenv
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# 🧠 Explain or chat with user
def get_friendly_response(user_input):
    if "name" in user_input.lower() or "who are you" in user_input.lower():
        return "Hi! I'm ELI5a (Elisa) — I explain things in super simple ways!"

    casual_words = ["hi", "hello", "hey", "thanks", "cool", "awesome", "how are you"]
    if any(word in user_input.lower() for word in casual_words):
        try:
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": f"You're ELI5a (Elisa), a friendly AI that explains complex topics simply. Respond to: {user_input}"}],
                model="llama-3.1-8b-instant",
                max_tokens=300
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        try:
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": f"You're ELI5a. Explain this in a friendly, brief way: {user_input}"}],
                model="llama-3.1-8b-instant",
                max_tokens=400
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"

# 🧠 Simple explanation
def get_simple_explanation(topic):
    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": f"Explain {topic} in simple terms."}],
            model="llama-3.1-8b-instant",
            max_tokens=400
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# 🎨 Streamlit UI
st.set_page_config(page_title="ELI5a", page_icon="🤖", layout="wide")
st.markdown("<h1 style='color:#ff4b4b;'>ELI5a - AI Explainer 🤖</h1>", unsafe_allow_html=True)
st.write("Type any complex topic below and ELI5a will break it down!")

topic = st.text_input("🔍 Enter a topic:")
if st.button("Chat with ELI5a"):
    if topic:
        with st.spinner("Thinking..."):
            st.write(get_friendly_response(topic))
    else:
        st.warning("Please enter a topic first.")

if st.button("Generate Simple Explanation"):
    if topic:
        with st.spinner("Explaining..."):
            st.write(get_simple_explanation(topic))
    else:
        st.warning("Please enter a topic first.")
