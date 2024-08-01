system_prompt_candidate = f"""
Let's think step by step.
CV details might be out of order or incomplete.
Analyze the CV concerning the candidate's experience and career. Derive logical conclusions about their technical skills, experience, and soft skills.
Ensure that educational qualifications are detailed as: Degree - School/University/Organization - GPA - Year of Graduation. Some details might be missing.
Experience should include time and job name, and field of work based on projects and experiences.
Technical skills should be listed explicitly, avoiding broad categories.
Responsibilities should be derived from projects and experiences of the candidate.
Use singular pronouns such as "he", "she", "the candidate", or the candidate's name for comments.
If any information is ambiguous or incomplete, provide reasonable assumptions or note the missing details.
"""

fn_candidate_analysis = [
    {
        "name": "AnalyzeCV",
        "description": "Analyze the candidate's resume to extract detailed information.",
        "parameters": {
            "type": "object",
            "properties": {
                "candidate_name": {
                    "type": "string",
                    "description": "Name of the candidate.",
                },
                "phone_number": {
                    "type": "string",
                    "description": "Phone number of the candidate.",
                },
                "email": {
                    "type": "string",
                    "description": "Email of the candidate. e.g., jackey@gmail.com, hinata@outlook.com",
                },
                "degree": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "Educational qualifications. e.g., Bachelor's degree in Computer Science - FPT University - 2024",
                },
                "experience": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "Summary of experiences in each field the candidate worked.",
                },
                "technical_skill": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "Specific technical skills and proficiencies. e.g., Java, Python, Linux, SQL.",
                },
                "responsibility": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "Summary of responsibilities the candidate had. e.g., Developed a fitness application for bodybuilding exercises on Android using Room Database, RxJava 2, and Retrofit 2.",
                },
                "certificate": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Certificates achieved. e.g., Advanced Data Analysis, Basic SQL.",
                },
                "soft_skill": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Soft skills inferred from the resume. Special attention to language and leadership skills. e.g., Language skill, Leadership skills, critical thinking, problem-solving.",
                },
                "comment": {
                    "type": "string",
                    "description": "Summary about the candidate, highlighting strong points and special features. e.g., The candidate has strong Python skills and excels in AI model tuning. Suitable for AI Engineer roles.",
                },
                "job_recommended": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Recommended job roles for the candidate. e.g., Fullstack Web Developer, Python Developer, AI Engineer, Data Analyst.",
                },
                "office": {
                    "type": "integer",
                    "description": "Years of experience in office-related skills. For example: 0, 1, 2, 3, etc.",
                },
                "sql": {
                    "type": "integer",
                    "description": "Years of experience in SQL skills. For example: 0, 1, 2, 3, etc.",
                },
            },
            "required": [
                "candidate_name",
                "phone_number",
                "email",
                "degree",
                "experience",
                "technical_skill",
                "responsibility",
                "certificate",
                "soft_skill",
                "comment",
                "job_recommended",
                "office",
                "sql",
            ],
        },
    }
]
