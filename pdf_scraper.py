import requests
import pdfplumber

def extract_pdf_data(pdf_url):
    # download the pdf
    response = requests.get(pdf_url)
    with open("exam_schedule.pdf", "wb") as pdf_file:
        pdf_file.write(response.content)
    
    # getting data from pdf
    schedule_data = []
    with pdfplumber.open("exam_schedule.pdf") as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            schedule_data.append(text)
    return schedule_data
