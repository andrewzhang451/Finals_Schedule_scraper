from flask import Flask, jsonify
from utils.web_scraper import get_pdf_link
from utils.pdf_scraper import extract_pdf_data

#scan the rest of the dir and see where other files are, relative to this file
app = Flask(__name__)

url = "https://www.iit.edu/registrar/academic-calendar/final-exam-schedule"

@app.route('/get-exam-schedule', methods=['GET'])
def get_exam_schedule():
    try:
        pdf_link = get_pdf_link(url)
        schedule_data = extract_pdf_data('https://www.iit.edu/sites/default/files/2024-11/final_exam_schedule_3.pdf')
        return jsonify({"schedule": schedule_data})
    except Exception as e:
        return jsonify({"error":str(e)})
        
if __name__ == '__main__':
    app.run(debug=True)
    