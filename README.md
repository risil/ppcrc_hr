# Analysis Service

Welcome to the Analysis Service repository. This project provides a comprehensive analysis service for candidate CVs and job descriptions using advanced AI techniques.

## Table of Contents

- [Analysis Service](#analysis-service)
  - [Table of Contents](#table-of-contents)
  - [Development Environment](#development-environment)
    - [ Create Environment and Install Packages](#1-create-environment-and-install-packages)
    - [Run the Application](#2-run-the-application)
  - [Project Structure](#project-structure)
  - [Configuration](#configuration)
  - [Logging](#logging)

## Development Environment

### 1. Create Environment and Install Packages

First, create a new conda environment and install the required packages.

 ```shell
conda create -n analysis_service python=3.10
```

Activate the newly created environment.

```shell
conda activate analysis_service
```

Install the dependencies listed in the requirements.txt file.

```shell
pip install -r requirements.txt
```

### 2. Run the Application

Use the following command to run the application using Uvicorn.

```shell
uvicorn app:app --port 7000
```

## Project Structure

The project is organized as follows:

```arduino
analysis_service/
├── candidate_cv/
├── job_description/
├── logs/
├── src/
│   ├── candidate/
│   ├── job/
│   ├── matching/
│   └── utils.py
├── .env.example
├── .gitignore
├── app.py
├── config.py
├── Dockerfile
├── entrypoint.sh
└── requirements.txt
```

- **candidate_cv/**: Directory for candidate CV files.
- **job_description/**: Directory for job description files.
- **logs/**: Directory for log files.
- **src/**: Source code for the project.
   - candidate/: Candidate-related functionalities.
   - job/: Job-related functionalities.
   - matching/: Matching logic for candidates and jobs.
   - utils.py: Utility functions, including logging setup.
- **.env.example**: Example environment configuration file.
- **.gitignore**: Git ignore file.
- **app.py**: Main application file.
- **config.py**: Configuration settings for the project.
- **Dockerfile**: Docker configuration file.
- **entrypoint.sh**: Entrypoint script for Docker.
- **requirements.txt**: List of dependencies.

## Configuration
Ensure to create a '.env file' in the root directory based on the '.env.example' file. This file should contain all necessary environment variables required by the application.


## Logging
The application uses a logging system to track and debug issues. Logs are stored in the 'logs/' directory. The logging configuration can be found in 'src/utils.py'.


