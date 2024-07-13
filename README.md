# Authentication System with OTP & CAPTCHA

Welcome to the Authentication System repository! This project implements a comprehensive user authentication solution using Node.js, Express, MongoDB, and Nodemailer. It includes features like user registration, OTP verification, password reset, and CAPTCHA protection. Follow these easy steps to get started!

## Overview

This project provides a robust authentication system with the following key features:
- **User Registration**: Register with email verification.
- **Log In**: Access the system using your email and password.
- **Reset Password**: Recover your password if you forget it.
- **Verify Your Email**: Ensure your email is valid.
- **CAPTCHA**: Prove you're human and protect against automated sign-ups.

## Table of Contents
1. [Features](#features)
2. [Technology Stack](#technology-stack)
3. [Getting Started](#getting-started)
4. [Folder Structure](#folder-structure)
5. [Configuration](#configuration)
6. [Running the Application](#running-the-application)
7. [API Endpoints](#api-endpoints)
8. [Contributing](#contributing)
9. [License](#license)

## Features
- **Secure User Registration**: Register users with email confirmation using a one-time password (OTP).
- **Login System**: Users can log in using their credentials.
- **Password Management**: Users can reset their passwords via email with OTP verification.
- **CAPTCHA Integration**: Ensures that registration and login attempts are made by humans, not bots.
- **Email Functionality**: Sends OTPs and password reset links through email.

## Technology Stack
- **Node.js**: JavaScript runtime for server-side logic.
- **Express**: Web framework for Node.js to handle routing and middleware.
- **MongoDB**: NoSQL database for storing user data and authentication details.
- **Mongoose**: ODM library for MongoDB, providing schema-based solutions.
- **Nodemailer**: Module for sending emails from Node.js applications.
- **body-parser**: Middleware to handle JSON requests.
- **express-session**: Middleware to manage user sessions.
- **dotenv**: Loads environment variables from a `.env` file.

## Getting Started

1. **Clone the Project**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git

2. **Navigate to the Project Directory**

   ```bash
   cd your-repo-name

3. **Install Dependencies:**

   Make sure Node.js is installed. Then run and install the required packages:
    ```bash 
   npm install

4. **Set Up Your Configuration**

   Create a .env file in the main folder with following content:
    ```plain text
    MONGODB_URI=mongodb://localhost:27017/testy
   EMAIL_USER="your-email@example.com"
   EMAIL_PASS="your-email-password"   
Replace the placeholders with your actual MongoDB URI and email credentials

5. **Start the Server**
    ```bash 
      npm install
Open your browser and go to http://localhost:3000 to see the app.





## Folder Structure

- **public/:** Contains styles and scripts.
   -  css/: Stylesheets for the application.
   -  js/: JavaScript files for client-side functionality.
- **views/**: HTML templates for various pages.
  - forgot-password.html
  - home.html
  - login.html
  - new-password.html
  - register.html
  - reset-password.html
  - verify-otp.html

- **main/**: Contains server and configuration files.
  - .env: Environment variables for configuration.
  - package.json: Project dependencies and scripts.
  - package-lock.json: Lock file for exact dependency versions.
  - server.js: Main server file handling routing, authentication, and email functionality.
  - node_modules/: Project dependencies.

## Configuration

- **Server Configuration**:
  The application runs on port 3000 by default. Modify the PORT environment variable in the `.env` file if needed.

- **Database Configuration**:
  MongoDB connection string is specified in the `MONGODB_URI` environment variable.

- **Email Configuration**:
  SMTP server details are set in the `.env` file. Ensure you have a valid email account for sending notifications.
## Running the Application

To start the application, execute:
   
    
      npm start

Visit http://localhost:3000 in your browser to access the application.


## API Endpoints

Here’s a summary of the available API endpoints:

- **GET /**
  - Serve the login page.
- **GET /login**
  - Serve the login page.
- **GET /register**
  - Serve the registration page.
- **GET /home**
  - Serve the home page.
- **GET /verify-otp**
  - Serve the OTP verification page.
- **GET /forgot-password**
  - Serve the forgot password page.
- **GET /reset-password**
  - Serve the reset password page.
- **GET /new-password**
  - Serve the new password page.
- **GET /api/captcha**
  - Retrieve a CAPTCHA challenge.
- **POST /api/logout**
  - Log out the user and destroy the session.
- **POST /api/register**
  - Register a new user with email and password.
- **POST /api/verify-otp**
  - Verify the OTP for registration.
- **POST /api/login**
  - Authenticate a user with email and password.
- **POST /api/forgot-password**
  - Request password reset with email.
- **POST /api/verify-reset-otp**
  - Verify OTP for password reset.
- **POST /api/reset-password**
  - Set a new password after OTP verification.



## Contributing

We welcome contributions! To contribute:

- Fork the repository.
- Create a new branch for your changes.
- Commit your changes and push to your forked repository.
- Open a pull request to merge your changes into the main repository.


