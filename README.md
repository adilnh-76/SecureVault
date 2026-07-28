# 🔒 SecureVault

A modern **Flask-based File Encryption & Decryption Web Application** that enables users to securely encrypt and decrypt files using password-based encryption. SecureVault uses **PBKDF2-HMAC-SHA256** for secure key derivation and **Fernet (AES-based authenticated encryption)** to protect file confidentiality and integrity.

---

## ✨ Features

- 🔐 Secure password-based file encryption
- 🔓 File decryption with password verification
- 🔑 PBKDF2-HMAC-SHA256 key derivation
- 🧂 Random salt generation for every encryption
- 🛡️ Fernet authenticated encryption
- 📂 Drag & Drop file upload
- 👁️ Show/Hide password
- 📊 Password strength indicator
- 📝 Audit logging for encryption/decryption events
- 🎨 Modern responsive user interface
- ⚠️ Input validation and error handling

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Backend | Flask, Python |
| Frontend | HTML5, CSS3, JavaScript |
| Security | Cryptography (Fernet), PBKDF2-HMAC-SHA256 |
| Icons | Font Awesome |
| Logging | Python Logging Module |

---

## 📂 Project Structure

```text
SecureVault/
│
├── app.py
├── config.py
├── logger.py
├── requirements.txt
├── README.md
│
├── utils/
│   ├── crypto.py
│   └── validator.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── encrypt.html
│   └── decrypt.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── password.js
│
├── uploads/
└── logs/
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/adilnh-76/SecureVault.git
cd SecureVault
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🔐 Encryption Workflow

```text
User
   │
   ▼
Upload File
   │
   ▼
Password Validation
   │
   ▼
Generate Random Salt
   │
   ▼
PBKDF2-HMAC-SHA256
   │
   ▼
Generate Encryption Key
   │
   ▼
Fernet Encryption
   │
   ▼
Download .enc File
```

## 🎯 Future Improvements

- Authentication & User Accounts
- AES-256-GCM Encryption Option
- File Integrity Verification (SHA-256)
- Rate Limiting
- CSRF Protection
- Security Headers (Flask-Talisman)
- Cloud Storage Integration
- Docker Support

---

## 👨‍💻 Author

**Adil N H**

- GitHub: https://github.com/adilnh-76

---

## 📄 License

This project is licensed under the **MIT License**.

---

⭐ If you found this project useful, consider giving it a **star** on GitHub.
