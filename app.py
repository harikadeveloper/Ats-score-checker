import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
import docx
import pypandoc
from bs4 import BeautifulSoup
from odf.opendocument import load
from odf.text import P
from striprtf.striprtf import rtf_to_text
from dotenv import load_dotenv
from job_roles import get_job_description  # Import the function from job_roles.py

# Load environment variables
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get response from Gemini API
def get_gemini_response(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

# Function to extract text from PDF
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Function to extract text from Word document (.docx)
def input_word_text(uploaded_file):
    doc = docx.Document(uploaded_file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

# Function to extract text from older Word document (.doc)
def input_doc_text(uploaded_file):
    # You will need to convert .doc to .docx first using unoconv or pywin32
    # This function assumes the file has been converted to .docx or .txt
    st.warning("The .doc file needs to be converted to .docx first.")
    return ""

# Function to extract text from RTF files
def input_rtf_text(uploaded_file):
    text = uploaded_file.read().decode("utf-8")
    return rtf_to_text(text)

# Function to extract text from HTML files
def input_html_text(uploaded_file):
    soup = BeautifulSoup(uploaded_file, "html.parser")
    return soup.get_text()

# Function to extract text from ODT files
def input_odt_text(uploaded_file):
    doc = load(uploaded_file)
    text = ""
    for paragraph in doc.getElementsByType(P):
        text += paragraph.firstChild.data + "\n"
    return text

# Prompts for each button
prompts = {
    "Tell Me About the Resume": """
        Act as a skilled ATS system with expertise in evaluating resumes.
        Based on the following resume and job description, provide a detailed profile summary.
        Resume: {text}
        Job Description: {jd}
    """,
    "How Can I Improve My Skills": """
        You are an expert in resume analysis and skill enhancement.
        Based on the resume and job description, identify the key missing skills and provide
        actionable suggestions for improvement.
        Resume: {text}
        Job Description: {jd}
    """,
    "Percentage Match": """
        Assume you are an advanced ATS tool. Calculate the percentage match between the following
        resume and job description. Consider relevance, keywords, and role requirements.
        Resume: {text}
        Job Description: {jd}
    """,
    "Missing Keywords": """
        You are a skilled ATS evaluator. Based on the resume and job description, identify
        the specific keywords missing from the resume that are crucial for this job.
        Resume: {text}
        Job Description: {jd}
    """
}

# Streamlit App
st.title("ATS Tracking System")
st.text("")

# Job Role Selection
st.sidebar.title("Job Role Selector")
selected_role = st.sidebar.selectbox("Choose a job role:", ["Select a role"] + list(get_job_description().keys()), key="job_role")

# Get job description based on selected role
job_description = ""
if selected_role != "Select a role":
    job_description = get_job_description()[selected_role]  # Get job description dynamically

# Job Description Text Area (Initially empty, filled after role selection)
jd = st.text_area("Job Description:", job_description)

# File Upload
uploaded_file = st.file_uploader("Upload your resume (PDF, DOC, DOCX, RTF, HTML, ODT)...", type=["pdf", "doc", "docx", "rtf", "html", "odt"], help="Limit 200MB per file")

# Initialize response variable
response = None

# Check file type and extract text
if uploaded_file is not None:
    file_extension = uploaded_file.name.split('.')[-1].lower()
    if file_extension == "pdf":
        text = input_pdf_text(uploaded_file)
    elif file_extension == "docx":
        text = input_word_text(uploaded_file)
    elif file_extension == "doc":
        text = input_doc_text(uploaded_file)
    elif file_extension == "rtf":
        text = input_rtf_text(uploaded_file)
    elif file_extension == "html":
        text = input_html_text(uploaded_file)
    elif file_extension == "odt":
        text = input_odt_text(uploaded_file)
    else:
        st.error("Unsupported file format. Please upload a valid file.")
else:
    text = ""

# Buttons in Vertical Layout
if st.button("Tell Me About the Resume"):
    if text and jd:
        prompt = prompts["Tell Me About the Resume"].format(text=text, jd=jd)
        response = get_gemini_response(prompt)
        st.session_state["response_type"] = "Profile Summary"
        st.session_state["response"] = response
    else:
        st.error("Please upload a resume and provide a job description!")

if st.button("How Can I Improve My Skills"):
    if text and jd:
        prompt = prompts["How Can I Improve My Skills"].format(text=text, jd=jd)
        response = get_gemini_response(prompt)
        st.session_state["response_type"] = "Skill Improvement Suggestions"
        st.session_state["response"] = response
    else:
        st.error("Please upload a resume and provide a job description!")

if st.button("Percentage Match"):
    if text and jd:
        prompt = prompts["Percentage Match"].format(text=text, jd=jd)
        response = get_gemini_response(prompt)
        st.session_state["response_type"] = "Match Percentage"
        st.session_state["response"] = response
    else:
        st.error("Please upload a resume and provide a job description!")

if st.button("Missing Keywords"):
    if text and jd:
        prompt = prompts["Missing Keywords"].format(text=text, jd=jd)
        response = get_gemini_response(prompt)
        st.session_state["response_type"] = "Missing Keywords"
        st.session_state["response"] = response
    else:
        st.error("Please upload a resume and provide a job description!")

# Display the response below all buttons
if "response" in st.session_state:
    st.subheader(st.session_state["response_type"])
    st.write(st.session_state["response"])
