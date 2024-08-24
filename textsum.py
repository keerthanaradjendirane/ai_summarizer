import google.generativeai as genai
import streamlit as st
from langchain import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI


api_key = st.secret["GEMINI_API"]
genai.configure(api_key=api_key)


model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def summarize_text(text, max_words):
    prompt = f"Summarize the following text in {max_words} words: {text}"
    response = model.generate_content([prompt])
    return response.text


st.title("Text Summarization Tool")
st.write("Enter the text you want to summarize and click the button to get a summary.")

user_text = st.text_area("Enter your text here:", height=300)


max_words = st.slider("Select the number of words for the summary:", min_value=10, max_value=2000, value=100, step=10)

if st.button("Summarize Text"):
    if user_text:
        summary = summarize_text(user_text, max_words)
        st.write("Summary:")
        st.write(summary)
    else:
        st.write("Please enter some text to summarize.")
