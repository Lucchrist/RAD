import streamlit as st
import PyPDF2
import pptx
from docx import Document
from io import StringIO

# Fonction pour lire un fichier PDF
def read_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Fonction pour lire un fichier Word
def read_word(file):
    doc = Document(file)
    text = [paragraph.text for paragraph in doc.paragraphs]
    return '\n'.join(text)

# Fonction pour lire un fichier PowerPoint
def read_ppt(file):
    prs = pptx.Presentation(file)
    text = []
    for slide in prs.slides:
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                text.append(shape.text)
    return '\n'.join(text)

# Interface Streamlit
st.title("Téléverser et visualiser un document")

# Téléversement du fichier
uploaded_file = st.file_uploader("Choisissez un fichier (PDF, Word, PowerPoint)", type=["pdf", "docx", "pptx"])

# Afficher le contenu du fichier téléversé
if uploaded_file is not None:
    file_type = uploaded_file.name.split('.')[-1]
    
    # Lire et afficher le fichier en fonction de son type
    if file_type == "pdf":
        st.subheader("Visualisation du contenu PDF")
        content = read_pdf(uploaded_file)
        st.text(content)
    
    elif file_type == "docx":
        st.subheader("Visualisation du contenu Word")
        content = read_word(uploaded_file)
        st.text(content)
    
    elif file_type == "pptx":
        st.subheader("Visualisation du contenu PowerPoint")
        content = read_ppt(uploaded_file)
        st.text(content)

