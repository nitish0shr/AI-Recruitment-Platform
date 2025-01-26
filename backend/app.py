# app.py: Main application file for AI Recruitment Platform backend

from flask import Flask, request, jsonify
from openai_api import process_job_description, analyze_resume, generate_report

app = Flask(__name__)

@app.route('/upload_job_description', methods=['POST'])
def upload_job_description():
    job_description = request.json.get('job_description')
    criteria = process_job_description(job_description)
    return jsonify(criteria)

@app.route('/upload_resumes', methods=['POST'])
def upload_resumes():
    resumes = request.json.get('resumes')
    results = [analyze_resume(resume) for resume in resumes]
    return jsonify(results)

@app.route('/generate_report', methods=['POST'])
def generate_report_route():
    candidate_data = request.json.get('candidate_data')
    report = generate_report(candidate_data)
    return jsonify(report)

if __name__ == '__main__':
    app.run(debug=True)
