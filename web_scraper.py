import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_pdf_link(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    pdf_tag = soup.find('a', type="application/pdf")
    #if pdf_tag (type and tag) and href tag ATTRIBUTES in pdf_tag, combine url with pdf_tag in a new var
    
    if pdf_tag and 'href' in pdf_tag.attrs:
        pdf_url = urljoin(url, pdf_tag['href'])
        return pdf_url
    
    raise Exception("PDF is not found on the page.")


#for testing purposes
if __name__ == "__main__":
    base_url = "https://www.iit.edu/registrar/academic-calendar/final-exam-schedule"
    print(get_pdf_link(base_url))

