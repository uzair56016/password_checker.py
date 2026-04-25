# password_checker.py
Python password strength checker with hidden input, regex validation, and security scoring.

A simple but powerful cybersecurity project that checks the strength of a password using security rules, provides a scoring system, and hides user input using `*` characters in the terminal.

---

## 🚀 Project Overview

This project is built using Python and focuses on basic cybersecurity principles such as password security, input handling, and validation using regular expressions.

It evaluates a password based on multiple security conditions and gives a final strength rating along with a security score and protection level.

---

## ✨ Features

- 🔒 Hidden password input using `*`
- 🧠 Real-time secure input handling
- 📏 Checks password length (8+ characters)
- 🔠 Detects uppercase letters
- 🔡 Detects lowercase letters
- 🔢 Detects numbers
- 🔣 Detects special characters
- 📊 Security scoring system (out of 5)
- 📈 Protection level in percentage
- ⚠️ Strength classification:
  - Weak ❌
  - Medium ⚠️
  - Strong ✅

---

## 🧠 How It Works

1. User is prompted to enter a password securely.
2. As the user types, characters are hidden and replaced with `*`.
3. The password is analyzed using rules:
   - Length check
   - Character type checks (upper, lower, digits, symbols)
4. Each rule adds to the score.
5. Final output shows:
   - Strength level
   - Score out of 5
   - Protection percentage

---

## 📊 Example Output
=== Password Strength Checker ===
Enter your password: ***********

Password Strength: Strong ✅
Security Score: 5 / 5
Protection Level: 100%


---

## 💻 Technologies Used

- Python 🐍
- Regular Expressions (`re`)
- Windows API (`msvcrt`) for hidden input

---

## ⚙️ Installation & Usage

### 1. Install Python
Make sure Python is installed on your system.

### 2. Save the file
Save the script as:
password_checker.py


### 3. Run the program
Open terminal or CMD and run:

```bash
python password_checker.py

Project Structure
password-strength-checker/
│
├── password_checker.py
├── README.md
