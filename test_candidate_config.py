from pydantic_settings import BaseSettings

class TestCandidateConfig(BaseSettings):
    MODEL_NAME: str = "gpt-3.5-turbo"  # Specify the OpenAI model you are using
    CV_UPLOAD_DIR: str = "./upload/"  # Directory where PDFs are located
    API_KEY: str = ""  # Ensure this is set from environment variables
    API_BASE_URL: str = "https://api.openai.com/v1"  # OpenAI API base URL
    SYSTEM_PROMPT: str = "Extract the following information from the resume: candidate_name, phone_number, email, comment, degree, experience, technical_skill, responsibility, certificate, soft_skill, job_recommended."

# Create an instance of the test configuration
test_candidate_config = TestCandidateConfig()
