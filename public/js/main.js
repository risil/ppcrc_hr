async function generateCaptcha() {
  try {
    const response = await fetch("/api/captcha");
    const data = await response.json();
    document.getElementById("captcha").textContent = `Solve: ${data.question}`;
  } catch (error) {
    console.error("Error generating CAPTCHA:", error);
  }
}

document.addEventListener("DOMContentLoaded", () => {
  generateCaptcha();

  const loginForm = document.getElementById("loginForm");
  if (loginForm) {
    loginForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;
      const captchaInput = document.getElementById("captchaInput").value;
      try {
        const response = await fetch("/api/login", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email, password, captcha: captchaInput }),
        });
        const data = await response.json();
        if (response.ok) {
          // Store user email in localStorage
          localStorage.setItem("userEmail", data.user.email);
          window.location.href = "/home";
        } else {
          alert(data.message);
          generateCaptcha();
        }
      } catch (error) {
        console.error("Error:", error);
      }
    });
  }

  const registerForm = document.getElementById("registerForm");
  if (registerForm) {
    registerForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const email = document.getElementById("email").value;
      const password = document.getElementById("password").value;
      const captchaInput = document.getElementById("captchaInput").value;

      try {
        const response = await fetch("/api/register", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email, password, captcha: captchaInput }),
        });
        const data = await response.json();
        alert(data.message);
        if (response.ok) {
          window.location.href = "/verify-otp";
        } else {
          generateCaptcha();
        }
      } catch (error) {
        console.error("Error:", error);
      }
    });
  }

  const verifyOTPForm = document.getElementById("verifyOTPForm");
  if (verifyOTPForm) {
    verifyOTPForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const otp = document.getElementById("otp").value;

      try {
        const response = await fetch("/api/verify-otp", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ otp }),
        });
        const data = await response.json();
        alert(data.message);
        if (response.ok) {
          window.location.href = "/login";
        }
      } catch (error) {
        console.error("Error:", error);
      }
    });
  }

  const forgotPasswordForm = document.getElementById("forgotPasswordForm");
  if (forgotPasswordForm) {
    forgotPasswordForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const email = document.getElementById("email").value;
      try {
        const response = await fetch("/api/forgot-password", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email }),
        });
        const data = await response.json();
        alert(data.message);
        if (response.ok) {
          window.location.href = "/reset-password";
        }
      } catch (error) {
        console.error("Error:", error);
      }
    });
  }

  const resetPasswordForm = document.getElementById("resetPasswordForm");
  if (resetPasswordForm) {
    resetPasswordForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const email = document.getElementById("email").value;
      const otp = document.getElementById("otp").value;
      try {
        const response = await fetch("/api/verify-reset-otp", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email, otp }),
        });
        const data = await response.json();
        alert(data.message);
        if (response.ok) {
          window.location.href = `/new-password?email=${encodeURIComponent(
            email
          )}&otp=${encodeURIComponent(otp)}`;
        }
      } catch (error) {
        console.error("Error:", error);
      }
    });
  }

  const newPasswordForm = document.getElementById("newPasswordForm");
  if (newPasswordForm) {
    // Pre-fill email and OTP if available in URL parameters
    const urlParams = new URLSearchParams(window.location.search);
    const email = urlParams.get("email");
    const otp = urlParams.get("otp");
    if (email) document.getElementById("email").value = email;
    if (otp) document.getElementById("otp").value = otp;

    newPasswordForm.addEventListener("submit", async (e) => {
      e.preventDefault();
      const email = document.getElementById("email").value;
      const otp = document.getElementById("otp").value;
      const newPassword = document.getElementById("newPassword").value;
      const confirmPassword = document.getElementById("confirmPassword").value;

      if (newPassword !== confirmPassword) {
        alert("Passwords do not match");
        return;
      }

      try {
        const response = await fetch("/api/reset-password", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email, otp, newPassword }),
        });
        const data = await response.json();
        alert(data.message);
        if (response.ok) {
          window.location.href = "/login";
        }
      } catch (error) {
        console.error("Error:", error);
      }
    });
  }

  const logoutButton = document.getElementById("logoutButton");
  if (logoutButton) {
    logoutButton.addEventListener("click", async () => {
      try {
        const response = await fetch("/api/logout", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
        });
        const data = await response.json();
        alert(data.message);
        localStorage.removeItem("userEmail");
        window.location.href = "/login";
      } catch (error) {
        console.error("Error:", error);
      }
    });
  }
});
