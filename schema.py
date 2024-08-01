from pydantic import BaseModel, Field
from typing import List

class ResponseSchema(BaseModel):
    candidate_name: str
    phone_number: str
    email: str
    comment: str
    degree: List[str]
    experience: List[str]
    technical_skill: List[str]
    responsibility: List[str]
    certificate: List[str]
    soft_skill: List[str]
    job_recommended: List[str]
