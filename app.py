import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_blog(input_text, no_of_words, blog_style):

    model = 'gpt-4o'

    template ="""
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_of_words} words.
        """
    
    prompt = template.format(blog_style=blog_style, input_text=input_text, no_of_words=no_of_words)
    
    response = openai.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system", 
                "content": prompt
            }
        ],
        temperature=0.5,
        top_p=1
    )
    # print(response.choices[0].message.content)
    return response.choices[0].message.content


get_blog("what is chat-gpt", 100, "Common People")


st.set_page_config(page_title="Blog Generation", 
                   page_icon="📝", 
                   layout="wide",
                   initial_sidebar_state="expanded")

st.header("Blog Generation 📝")

input_text = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns([5,5])

with col1:
    no_of_words = st.slider("Select the number of words: ", 100 , 1000)
with col2:
    blog_style = st.selectbox('Writing the blog for: ',['Researcher', 'Professional', 'Common People'], index=0)

submit = st.button("Generate Blog")

if submit:
    st.write(get_blog(input_text, no_of_words, blog_style))


