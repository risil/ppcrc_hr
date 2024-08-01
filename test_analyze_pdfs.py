import os
import json
import time
import jsbeautifier
import openai
from pydantic import ValidationError
from schema import ResponseSchema
from test_candidate_config import test_candidate_config as candidate_config

def log_info(message):
    """Simple logging function"""
    print(f"[INFO] {message}")

def output2json(output):
    """Convert GPT Output Object to JSON"""
    opts = jsbeautifier.default_options()
    beautified_output = jsbeautifier.beautify(output["choices"][0]["message"]["content"], opts)
    return json.loads(beautified_output)

def analyze_content(cv_content):
    """Analyze the content of a CV using OpenAI's GPT-3.5-turbo model"""
    start = time.time()
    log_info("Start analyze content")

    try:
        # Create the embedding using the OpenAI model
        response = openai.ChatCompletion.create(
            model=candidate_config.MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": candidate_config.SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": cv_content
                }
            ]
        )
        json_output = output2json(response)
        
        # Validate the response against the schema
        try:
            response_schema = ResponseSchema(**json_output)
        except ValidationError as e:
            log_info(f"Validation Error: {e}")
            return None
        
        log_info("Done analyze content")
        log_info(f"Time analyze content: {time.time() - start}")

        return response_schema.dict()

    except Exception as e:
        log_info(f"Error analyzing content: {e}")
        return None

def read_pdf(file_path):
    """Read the content of a PDF by concatenating the content of all pages"""
    # Add code to read PDF content here
    # This is a placeholder; replace with actual PDF reading code
    return "PDF content here"

def analyze_all_pdfs_in_upload_folder():
    """Analyze all PDFs in the upload folder and store the results"""
    upload_dir = candidate_config.CV_UPLOAD_DIR
    analysis_results = []

    # Iterate through all files in the upload directory
    for file_name in os.listdir(upload_dir):
        # Check if the file is a PDF
        if file_name.lower().endswith('.pdf'):
            file_path = os.path.join(upload_dir, file_name)
            
            # Read and analyze the content of the PDF
            cv_content = read_pdf(file_path)
            analysis_result = analyze_content(cv_content)
            
            # Store the result in the list with the filename as the key
            if analysis_result:
                analysis_results.append({file_name: analysis_result})

    return analysis_results

# Run the analysis and print the results
if __name__ == "__main__":
    openai.api_key = os.getenv("OPENAI_API_KEY")
    results = analyze_all_pdfs_in_upload_folder()
    for result in results:
        print(json.dumps(result, indent=2))
