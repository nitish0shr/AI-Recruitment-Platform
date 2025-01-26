# openai_api.py: Integration with OpenAI API for AI Recruitment Platform

import openai
import os

# Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


def process_job_description(job_description):
    # Use OpenAI API to extract key skills, experience, and responsibilities
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Extract key skills, experience, and responsibilities from the following job description: {job_description}",
        max_tokens=150
    )
    return response.choices[0].text.strip()


def analyze_resume(resume):
    # Use OpenAI API to analyze resume against job criteria
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Analyze the following resume and categorize the candidate into a tier based on relevance to the job criteria: {resume}",
        max_tokens=150
    )
    return response.choices[0].text.strip()


def generate_report(candidate_data):
    # Use OpenAI API to generate a report for the candidate
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate a report for the following candidate data: {candidate_data}",
        max_tokens=150
    )
    return response.choices[0].text.strip()
