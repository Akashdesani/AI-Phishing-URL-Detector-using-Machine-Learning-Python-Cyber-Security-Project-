🛡️ AI Phishing URL Detector

An AI-powered cybersecurity tool built with Python that detects phishing URLs using machine learning and URL feature analysis. This project helps identify potentially dangerous websites by analyzing patterns commonly used in phishing attacks.

📌 Overview

Phishing attacks are one of the most common cybersecurity threats. Attackers create fake websites that look similar to legitimate platforms to steal sensitive information such as passwords, banking details, and personal data.

This project uses Machine Learning + URL feature extraction to classify whether a given URL is Safe or Phishing.

The system analyzes multiple security indicators such as:

URL length

HTTPS presence

Suspicious keywords

Number of subdomains

URL structure patterns

Based on these features, the model predicts the probability of phishing.

🚀 Features

✔ Machine Learning based detection
✔ URL structure analysis
✔ Suspicious keyword detection
✔ HTTPS security check
✔ Fast prediction system
✔ Lightweight Python implementation

🧠 Technologies Used

Python

Scikit-Learn

Pandas

Machine Learning

Cybersecurity Concepts

⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/yourusername/AI-Phishing-URL-Detector.git
2️⃣ Navigate to the project directory
cd AI-Phishing-URL-Detector
3️⃣ Install dependencies
pip install -r requirements.txt
▶️ Usage

Run the main Python script:

python main.py

Enter a URL when prompted.

Example:

Enter URL to check: https://secure-login-bank.com

Output:

⚠️ Warning: This URL is likely PHISHING!

or

✅ This URL appears SAFE.
📊 How It Works

1️⃣ User enters a URL
2️⃣ System extracts security-related features
3️⃣ Machine Learning model analyzes patterns
4️⃣ The model predicts whether the URL is phishing or safe

🔒 Cybersecurity Importance

Phishing attacks are responsible for:

Identity theft

Banking fraud

Data breaches

Tools like this help detect malicious URLs early and improve online security awareness.

🧪 Future Improvements

Deep Learning model integration

Real-time phishing detection API

Browser extension integration

Large phishing dataset training

Website content analysis

🤝 Contributing

Contributions are welcome!

If you want to improve this project:

Fork the repository

Create a new branch

Commit your changes

Submit a Pull Request

⭐ Support

If you like this project, please consider giving it a ⭐ star on GitHub to support the work.

👨‍💻 Author

Aakash Desani

BCA Student

Cyber Security Enthusiast

Python Developer

📜 License


This project is licensed under the MIT License.
