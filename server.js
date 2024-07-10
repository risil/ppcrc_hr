const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");
const nodemailer = require("nodemailer");
const path = require("path");
const session = require("express-session");
require("dotenv").config();

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.static("public"));
app.use(bodyParser.json());
app.use(
  session({
    secret: "your_session_secret",
    resave: false,
    saveUninitialized: true,
    cookie: { secure: false }, // set to true if using https
  })
);

// MongoDB connection
mongoose
  .connect(process.env.MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => {
    console.log("Connected to MongoDB");
  })
  .catch((err) => {
    console.error("Error connecting to MongoDB", err);
  });

// User model
const UserSchema = new mongoose.Schema({
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  isVerified: { type: Boolean, default: false },
  resetToken: { type: String, default: null },
  resetTokenExpires: { type: Date, default: null },
});

const User = mongoose.model("User", UserSchema);

// Email transporter
const transporter = nodemailer.createTransport({
  host: "smtp-mail.outlook.com",
  port: 587,
  secure: false,
  auth: {
    user: process.env.EMAIL_USER,
    pass: process.env.EMAIL_PASS,
  },
});

function generateMathCaptcha() {
  const num1 = Math.floor(Math.random() * 10) + 1;
  const num2 = Math.floor(Math.random() * 10) + 1;
  const operation = Math.random() < 0.5 ? "+" : "-";
  const question = `${num1} ${operation} ${num2}`;
  const answer = operation === "+" ? num1 + num2 : num1 - num2;
  return { question, answer };
}

function generateOTP() {
  return Math.floor(100000 + Math.random() * 900000).toString();
}

// Routes
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "login.html"));
});

app.get("/login", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "login.html"));
});

app.get("/register", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "register.html"));
});

app.get("/home", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "home.html"));
});

app.get("/verify-otp", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "verify-otp.html"));
});

app.get("/forgot-password", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "forgot-password.html"));
});

app.get("/reset-password", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "reset-password.html"));
});

app.get("/new-password", (req, res) => {
  res.sendFile(path.join(__dirname, "views", "new-password.html"));
});

app.get("/api/captcha", (req, res) => {
  const captcha = generateMathCaptcha();
  req.session.captchaAnswer = captcha.answer;
  res.json({ question: captcha.question });
});

app.post("/api/logout", (req, res) => {
  req.session.destroy((err) => {
    if (err) {
      return res.status(500).json({ message: "Error logging out" });
    }
    res.status(200).json({ message: "Logged out successfully" });
  });
});

app.post("/api/register", async (req, res) => {
  const { email, password, captcha } = req.body;

  if (parseInt(captcha) !== req.session.captchaAnswer) {
    return res.status(400).json({ message: "Invalid CAPTCHA" });
  }

  try {
    const existingUser = await User.findOne({ email });
    console.log("Existing user check result:", existingUser); // Logging the result of user check

    if (existingUser) {
      if (existingUser.isVerified) {
        return res
          .status(400)
          .json({ message: "User already exists and is verified" });
      } else {
        // If user exists but is not verified, we can allow re-registration
        await User.deleteOne({ email }); // Delete the unverified user
        console.log("Deleted unverified user:", email);
      }
    }

    const otp = generateOTP();
    req.session.registrationOTP = otp;
    req.session.pendingRegistration = { email, password };

    await transporter.sendMail({
      from: process.env.EMAIL_USER,
      to: email,
      subject: "Verify your email",
      text: `Your OTP for email verification is: ${otp}`,
    });

    res.status(200).json({
      message:
        "OTP sent to your email. Please verify to complete registration.",
    });
  } catch (error) {
    console.error("Error in registration process:", error);
    res.status(500).json({ message: "Error in registration process" });
  }
});

app.post("/api/verify-otp", async (req, res) => {
  const { otp } = req.body;

  if (otp !== req.session.registrationOTP) {
    return res.status(400).json({ message: "Invalid OTP" });
  }

  try {
    const { email, password } = req.session.pendingRegistration;
    const newUser = new User({ email, password, isVerified: true });
    await newUser.save();

    console.log("New user created:", newUser); // Logging the newly created user

    delete req.session.registrationOTP;
    delete req.session.pendingRegistration;

    res.status(201).json({ message: "User registered successfully." });
  } catch (error) {
    console.error("Error verifying OTP:", error);
    res.status(500).json({ message: "Error verifying OTP" });
  }
});

app.post("/api/login", async (req, res) => {
  const { email, password, captcha } = req.body;
  if (parseInt(captcha) !== req.session.captchaAnswer) {
    return res.status(400).json({ message: "Invalid CAPTCHA" });
  }

  try {
    const user = await User.findOne({ email, password });
    if (!user) {
      return res.status(401).json({ message: "Invalid credentials" });
    }

    if (!user.isVerified) {
      return res
        .status(401)
        .json({ message: "Please verify your email first" });
    }

    // Set user information in the session
    req.session.user = {
      id: user._id,
      email: user.email,
    };

    res
      .status(200)
      .json({ message: "Login successful", user: { email: user.email } });
  } catch (error) {
    console.error("Error logging in:", error);
    res.status(500).json({ message: "Error logging in" });
  }
});

app.post("/api/forgot-password", async (req, res) => {
  const { email } = req.body;
  try {
    const user = await User.findOne({ email });
    if (!user) {
      return res.status(404).json({ message: "User not found" });
    }

    const resetToken = generateOTP();
    const resetTokenExpires = Date.now() + 3600000; // 1 hour

    user.resetToken = resetToken;
    user.resetTokenExpires = resetTokenExpires;
    await user.save();

    await transporter.sendMail({
      from: process.env.EMAIL_USER,
      to: email,
      subject: "Reset your password",
      text: `Your OTP for password reset is: ${resetToken}`,
    });

    res.status(200).json({ message: "Password reset OTP sent to your email" });
  } catch (error) {
    console.error("Error processing forgot password request:", error);
    res.status(500).json({ message: "Error processing request" });
  }
});

app.post("/api/verify-reset-otp", async (req, res) => {
  const { email, otp } = req.body;
  try {
    const user = await User.findOne({
      email,
      resetToken: otp,
      resetTokenExpires: { $gt: Date.now() },
    });

    if (!user) {
      return res.status(400).json({ message: "Invalid or expired OTP" });
    }

    res.status(200).json({ message: "OTP verified successfully" });
  } catch (error) {
    console.error("Error verifying reset OTP:", error);
    res.status(500).json({ message: "Error verifying OTP" });
  }
});

app.post("/api/reset-password", async (req, res) => {
  const { email, otp, newPassword } = req.body;
  try {
    const user = await User.findOne({
      email,
      resetToken: otp,
      resetTokenExpires: { $gt: Date.now() },
    });

    if (!user) {
      return res.status(400).json({ message: "Invalid or expired OTP" });
    }

    user.password = newPassword;
    user.resetToken = null;
    user.resetTokenExpires = null;
    await user.save();

    res.status(200).json({ message: "Password reset successfully" });
  } catch (error) {
    console.error("Error resetting password:", error);
    res.status(500).json({ message: "Error resetting password" });
  }
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
