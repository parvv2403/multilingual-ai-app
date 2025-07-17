import streamlit as st
from transformers import MarianMTModel, MarianTokenizer
from gtts import gTTS
import os

# Load translation model and tokenizer
@st.cache_resource
def load_model():
    model_name = "Helsinki-NLP/opus-mt-hi-en"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_model()

# Translation function
def translate(text):
    tokens = tokenizer(text, return_tensors="pt", padding=True)
    translated = model.generate(**tokens)
    output = tokenizer.batch_decode(translated, skip_special_tokens=True)
    return output[0]

# Text to speech function
def speak(text, filename="output.mp3"):
    tts = gTTS(text)
    tts.save(filename)
    os.system(f"start {filename}" if os.name == "nt" else f"xdg-open {filename}")

# Streamlit UI
st.title("AI-Powered Multilingual Learning Assistant")
st.markdown("### Hindi to English Translator with Speech Output")

user_input = st.text_input("Enter text in Hindi:")

if st.button("Translate and Speak"):
    if user_input.strip() != "":
        with st.spinner("Translating..."):
            english_text = translate(user_input)
            st.success(f"English Translation: {english_text}")
            speak(english_text)
    else:
        st.warning("Please enter some text in Hindi.")