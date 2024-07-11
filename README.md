# Authentication System with OTP & CAPTCHA

Welcome to the Authentication System project! This simple app handles user login, registration, password resets, and more. Follow these easy steps to get started!

## What’s This All About?

This project helps you:
- **Sign Up**: Register with email verification.
- **Log In**: Access the system using your email and password.
- **Reset Password**: Recover your password if you forget it.
- **Verify Your Email**: Ensure your email is valid.
- **CAPTCHA**: Prove you're human and protect against automated sign-ups.

## Tools We Use

- **Node.js**: Runs JavaScript on the server.
- **Express**: Manages web requests and responses.
- **MongoDB**: Stores user data.
- **Nodemailer**: Sends OTPs and password reset emails.
- **body-parser**: Parses incoming data.
- **express-session**: Manages user sessions.

## How to Get Started

1. **Clone the Project**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git

2. **Navigate to the Project Folder**

   ```bash
   cd your-repo-name

3. **Install Dependencies:**

   Make sure Node.js is installed. Then run:
    ```bash 
   npm install

4. **Set Up Your Configuration**

   Create a .env file in the main folder with:
    ```plain text
    MONGODB_URI=mongodb://localhost:27017/testy
   EMAIL_USER="your-email@example.com"
   EMAIL_PASS="your-email-password"   
Replace your-email@example.com and your-email-password with your email and password.

5. **Start the Server**
    ```bash 
      npm install
Open your browser and go to http://localhost:3000 to see the app.





## Project Structure

- **public/:** Contains styles and scripts.
   -  css/: Website styling.
   -  js/: Interactive scripts.
- **views/:** HTML files for different pages.
   - 'login.html', 'register.html', 'home.html', etc.
- **main/:** Core server files.
   - 'server.js': Contains the server logic.
   - 'package.json': Lists dependencies and scripts.
   - '.env': Configuration file (set this up yourself).


## How It Works

- Registration: Sign up with your email and verify it using an OTP.
- Login: Log in with your email and password.
- Forgot Password: Request an OTP to reset your password.
- CAPTCHA: Solve a math problem to prove you're not a bot.

## Need Help?

If you have questions or issues, open an issue on this GitHub repository, and we'll help you out!


## Contributing
**Want to contribute? Here’s how:**

- Fork the repo.
- Make your changes.
- Submit a pull request.