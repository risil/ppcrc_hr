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

script_dir = os.path.dirname(os.path.abspath(__file__))
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
    def __init__(self, file_storage):
        self.__details = {
            'Name': None,
            'Email': None,
            'Mobile_Number': None,
            'Skills': None,
            'Education': None,
            'Experience': None
        }
        self.__resume = file_storage
        self.__text = extract_text_from_pdf(self.__resume)
        self.parse_resume()

    def parse_resume(self):
        try:
            self.__details["Email"] = get_email_addresses(self.__text)
            self.__details["Mobile_Number"] = get_phone_numbers(self.__text)
            self.extract_details_using_groq()
        except Exception as e:
            print(f"Error while parsing resume: {e}")

    def extract_details_using_groq(self):
        #GROQ_API_ENDPOINT = "https://api.groq.com/v1/models/completions"
        GROQ_API_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"
        GROQ_API_KEY = os.environ.get("GROQ_API_KEY")  # Use environment variable for API key

        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY environment variable is not set")

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

        try:
            response = requests.post(GROQ_API_ENDPOINT, headers=headers, json=data)
            response.raise_for_status()
            result = response.json()['choices'][0]['message']['content']
            parsed_result = json.loads(result)
            self.__details.update(parsed_result)
        except requests.exceptions.RequestException as e:
            print(f"Error making request to Groq API: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON response: {e}")
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

    def save_to_csv(self, csv_filename):
        if self.mobile_number_exists_in_csv(csv_filename):
            print("Mobile number already exists in the CSV file.")
            return

        fieldnames = ['Name', 'Email', 'Mobile_Number', 'Skills', 'Education', 'Experience']
        file_exists = os.path.exists(csv_filename)

        try:
            with open(csv_filename, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                if not file_exists:
                    writer.writeheader()
                writer.writerow(self.__details)
        except Exception as e:
            print(f"Error saving to CSV: {e}")

# Example usage
# if __name__ == "__main__":
#     resume_path = 'path_to_your_resume.pdf'
#     with open(resume_path, 'rb') as file:
#         file_storage = FileStorage(file)
#         resume_parser = ResumeParser(file_storage)
#         parsed_details = resume_parser.get_parsed_details()
#         resume_parser.save_to_csv("resumes.csv")
#         print(parsed_details)