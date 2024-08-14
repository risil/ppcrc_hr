import os
import re
import csv
import json
import requests
from io import BytesIO
from werkzeug.datastructures import FileStorage
import PyPDF2
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words('english'))

EDUCATION = [
    'BE', 'B.E.', 'B.E', 'BS', 'B.S',
    'ME', 'M.E', 'M.E', 'M.S',
    'BTECH', 'B.TECH', 'M.TECH', 'MTECH',
    'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII'
]

script_dir = os.path.dirname(os.path.abspath(_file_))
skills_filename = os.path.join(script_dir, "../res/parser/Skills/all_skills.txt")

def read_skills_file(filename, encoding='utf-8'):
    try:
        with open(filename, 'r', encoding=encoding) as file:
            skills_list = [line.strip().lower() for line in file]
        return list(set(remove_numbers(skills_list)))
    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError: {e}")
        return []

def remove_numbers(skills_list):
    pattern = r'^[\'"]?\d+(\.\d+)?[\'"]?$'
    return [skill for skill in skills_list if not re.match(pattern, skill)]

skills_list = read_skills_file(skills_filename)

def extract_text_from_pdf(file_storage):
    if not isinstance(file_storage, FileStorage):
        raise ValueError("file_storage should be a FileStorage object")

    try:
        pdf_data = file_storage.read()
        pdf_reader = PyPDF2.PdfReader(BytesIO(pdf_data))
        return " ".join(page.extract_text() for page in pdf_reader.pages)
    except Exception as e:
        raise RuntimeError(f"Failed to extract text from PDF: {e}")

def get_email_addresses(string):
    return re.findall(r'[\w\.-]+@[\w\.-]+', string)

def get_phone_numbers(string):
    phone_numbers = re.findall(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', string)
    return [re.sub(r'\D', "", num) for num in phone_numbers]

class ResumeParser:
    def _init_(self, file_storage):
        self.__details = {
            'Name': None,
            'Email': None,
            'Mobile_Number': None,
            'Skills': None,
            'Education': None,
            'Experience': None
        }
        self.__resume = file_storage
        self._text = extract_text_from_pdf(self._resume)
        self.parse_resume()

    def parse_resume(self):
        try:
            self._details["Email"] = get_email_addresses(self._text)
            self._details["Mobile_Number"] = get_phone_numbers(self._text)
            self.extract_details_using_groq()
        except Exception as e:
            print(f"Error while parsing resume: {e}")

    def extract_details_using_groq(self):
        GROQ_API_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"
        GROQ_API_KEY = os.environ.get("GROQ_API_KEY")  # Use environment variable for API key

        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY environment variable is not set")

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        prompt = f"""
        Extract the following information from this resume and return as json:
        Name:
        Email:
        Phone:
        Skills (as a comma-separated list):
        Education:
        Experience:

        Resume:
        {self.__text}
        """

        data = {
            "model": "mixtral-8x7b-32768",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.5,
            "max_tokens": 10000
        }

        try:
            response = requests.post(GROQ_API_ENDPOINT, headers=headers, json=data)
            response.raise_for_status()
            
            # Print response text for debugging
            # print("API Response:", response.text)
            
            # Attempt to parse JSON
            result = response.json()['choices'][0]['message']['content']
            parsed_result = json.loads(result)
            print(json.dumps(parsed_result, indent=4))
            self.__details.update(parsed_result)
        except requests.exceptions.RequestException as e:
            print(f"Error making request to Groq API: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON response: {e}")
            print("Response content:", response.text)  # Added debug info
        except KeyError as e:
            print(f"Unexpected response structure: {e}")

    def get_parsed_details(self):
        return self.__details

    def mobile_number_exists_in_csv(self, csv_filename):
        if not os.path.exists(csv_filename):
            return False

        try:
            with open(csv_filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return any(row['Mobile_Number'] == str(self.__details['Mobile_Number']) for row in reader)
        except Exception as e:
            print(f"Error checking mobile number in CSV: {e}")
            return False

# Example usage in a Flask app
from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route('/upload', methods=['POST'])
def upload_resume():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        resume_parser = ResumeParser(file)
        parsed_details = resume_parser.get_parsed_details()
        save_to_csv(parsed_details)
        return jsonify(parsed_details), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if _name_ == '_main_':
    app.run(debug=True)



def save_to_csv(json_response, csv_filename='output.csv'):
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write headers and single-row fields
        writer.writerow(['Name:', json_response.get('Name', 'N/A')])
        writer.writerow(['Email:', json_response.get('Email', 'N/A')])
        writer.writerow(['Phone:', json_response.get('Phone', 'N/A')])
        writer.writerow(['Skills (as a comma-separated list):', json_response.get('Skills', 'N/A')])
        
        # Write Education
        education = json_response.get('Education', {})
        education_details = f"{education.get('Degree', 'N/A')} from {education.get('Institution', 'N/A')} ({education.get('Location', 'N/A')}, {education.get('Graduation Year', 'N/A')})"
        writer.writerow(['Education:', education_details])
        
        # Write Experience
        writer.writerow(['Experience:'])
        experience_list = json_response.get('Experience', [])
        for experience in experience_list:
            writer.writerow([f"Company: {experience.get('Company', 'N/A')}"])
            writer.writerow([f"Position: {experience.get('Position', 'N/A')}"])
            writer.writerow([f"Location: {experience.get('Location', 'N/A')}"])
            writer.writerow([f"Duration: {experience.get('Duration', 'N/A')}"])
            writer.writerow(["Responsibilities:"])
            responsibilities = experience.get('Responsibilities', [])
            for responsibility in responsibilities:
                writer.writerow([responsibility])
            writer.writerow([])  # Blank line for separation
        
        # Write Projects
        writer.writerow(['Projects:'])
        project_list = json_response.get('Projects', [])
        for project in project_list:
            writer.writerow([f"Name: {project.get('Name', 'N/A')}"])
            writer.writerow([f"GitHub: {project.get('GitHub', 'N/A')}"])
            if 'Releases' in project:
                writer.writerow([f"Releases: {project.get('Releases', 'N/A')}"])
            if 'Improvements' in project:
                writer.writerow([f"Improvements: {project.get('Improvements', 'N/A')}"])
            if 'Automation' in project:
                writer.writerow([f"Automation: {project.get('Automation', 'N/A')}"])
            if 'Compilation' in project:
                writer.writerow([f"Compilation: {project.get('Compilation', 'N/A')}"])
            if 'Development' in project:
                writer.writerow([f"Development: {project.get('Development', 'N/A')}"])
            if 'Description' in project:
                writer.writerow([f"Description: {project.get('Description', 'N/A')}"])
            if 'State Management' in project:
                writer.writerow([f"State Management: {project.get('State Management', 'N/A')}"])
            if 'IO Operations' in project:
                writer.writerow([f"IO Operations: {project.get('IO Operations', 'N/A')}"])
            if 'Caching' in project:
                writer.writerow([f"Caching: {project.get('Caching', 'N/A')}"])
            if 'Authentication' in project:
                writer.writerow([f"Authentication: {project.get('Authentication', 'N/A')}"])
            writer.writerow([])