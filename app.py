import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
client =Groq(api_key=os.getenv("GROQ_API_KEY"))
def get_friendly_response(user_input):
    # Check if it's a name question first
    if "name" in user_input.lower() or "who are you" in user_input.lower():
        return "Hi! I'm ELI5a, but you can call me Elisa! I'm here to explain complex topics in simple ways. What would you like to learn about?"
    
    # Check if it's casual conversation
    casual_words = ["hi", "hello", "hey", "thanks", "cool", "awesome", "how are you"]
    
    if any(word in user_input.lower() for word in casual_words):
        try:
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": f"You are ELI5a (but people can call you Elisa), a friendly AI that explains complex topics simply. Respond in a friendly, casual way to: {user_input}"}],
                model="llama-3.1-8b-instant",
                max_tokens=100
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        # It's probably a topic to explain
        try:
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": f"You are ELI5a (Elisa). Give a brief, friendly overview of {user_input}. Keep it conversational."}],
                model="llama-3.1-8b-instant",
                max_tokens=200
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"
# Simple background CSS
st.markdown("""
<style>
    .stApp {
        background-color: #1e1e1e;
    }
    
    .main .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }
</style>
""", unsafe_allow_html=True)
st.set_page_config(page_title="ELI5a",page_icon=":robot_face:", layout="wide")
st.title("ELI5a-AI Explanation Tool")
st.write("Enter any complex topic and get explanations for different levels bro!")
topic = st.text_input("Enter a topic to explain in simple terms:")
if st.button("Chat with ELI5a😄"):
    if topic:
        with st.spinner("Thinking..."):
            response = get_friendly_response(topic)
            st.write(response)
    else:
        st.warning("please enter a topic to explain")
def get_simple_explanation(topic):
    try:
        response=client.chat.completions.create(
            messages=[{"role": "user", "content": f"Explain {topic} in simple terms"}],
            model="llama-3.1-8b-instant",
            max_tokens=200
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error:{str(e)}"

if st.button("Generate Simple Explanation"):
    if topic:
        with st.spinner("Generating simple explanation..."):
            explanation = get_simple_explanation(topic)
            st.write(explanation)
    else:
        st.warning("Please enter a topic to explain in simple terms.")
        