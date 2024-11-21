from dotenv import load_dotenv
load_dotenv()
import streamlit as sApp
import os
import google.generativeai as gemini
from langchain_community.document_loaders import WebBaseLoader

gemini.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = gemini.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text
def get_jobDescription(url):
    loader = WebBaseLoader(url)
    page_data = loader.load().pop().page_content
    return page_data

sApp.set_page_config(page_title="Gemini AI App")
sApp.header("Gemini AI app")

input = sApp.text_input("Input:", key="input")
submit = sApp.button("Ask Gemini")

if submit:
    
    
    jobDes = get_jobDescription(input)
    prompt = f"Give me the Job title, description and key skils by reading the following text from a job posting {jobDes}"
    job = get_gemini_response(prompt)
    prompt = f"You are a software Engineer named Varun having 4 plus years of expirience in software development. You have seen the followinf job description {job}. Create a cold email to send to the recruiter"
    email = get_gemini_response(prompt)
    sApp.subheader("Here is a cold email for the given Job:")
    sApp.write(email)

