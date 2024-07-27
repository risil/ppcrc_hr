# api :-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


import os
import csv
from io import BytesIO
import PyPDF2
from werkzeug.datastructures import FileStorage
import requests

class ResumeParser:
    def _init_(self, resume):
        self.__details = {
            'Name': None,
            'Email': None,
            'Mobile_Number': None,
            'Skills': None,
            'Education': None,
            'Experience': None
        }
        self.__resume = resume
        self._text = self.extract_text_from_pdf(self._resume)
        self.parse_resume()

    def extract_text_from_pdf(self, file_storage):
        if not isinstance(file_storage, FileStorage):
            raise ValueError("file_storage should be a FileStorage object")

        pdf_data = file_storage.read()
        pdf_reader = PyPDF2.PdfReader(BytesIO(pdf_data))
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

    def parse_resume(self):
        # Replace this with your actual Groq AI API endpoint and key
        GROQ_API_ENDPOINT = "https://api.groq.com/v1/chat/completions"
        GROQ_API_KEY = "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"

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        prompt = f"""
        Extract the following information from the given resume text:
        1. Name
        2. Email
        3. Mobile Number
        4. Skills (as a comma-separated list)
        5. Education (as a list of degrees)
        6. Years of Experience

        Resume text:
        {self.__text}

        Provide the output in JSON format.
        """

        data = {
            "model": "mixtral-8x7b-32768",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2
        }

        response = requests.post(GROQ_API_ENDPOINT, headers=headers, json=data)
        if response.status_code == 200:
            result = response.json()['choices'][0]['message']['content']
            parsed_result = eval(result)  # Convert string to dictionary
            self.__details.update(parsed_result)
        else:
            print(f"Error: {response.status_code}")
            print(response.text)

    def get_parsed_details(self):
        return self.__details

    def save_to_csv(self, csv_filename):
        script_dir = os.path.dirname(os.path.abspath(_file_))
        full_path = os.path.join(script_dir, csv_filename)

        if not os.path.exists(full_path):
            with open(full_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.__details.keys())
                writer.writeheader()

        with open(full_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=self.__details.keys())
            writer.writerow(self.__details)

# Example usage
# resume_path = 'path_to_your_resume.pdf'
# resume_parser = ResumeParser(resume_path)
# parsed_details = resume_parser.get_parsed_details()
# resume_parser.save_to_csv("resumes.csv")
# print(parsed_details)