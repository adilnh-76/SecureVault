import os
import secrets

class Config:
    # Flask Configuration
    SECRET_KEY = secrets.token_hex(32)

    # Maximum upload size (20 MB)
    MAX_CONTENT_LENGTH = 20 * 1024 * 1024

    # Upload folder (optional - if you decide to save files temporarily)
    UPLOAD_FOLDER = "uploads"

    # Allowed file extensions
    ALLOWED_EXTENSIONS = {
        "txt",
        "pdf",
        "png",
        "jpg",
        "jpeg",
        "gif",
        "doc",
        "docx",
        "xls",
        "xlsx",
        "ppt",
        "pptx",
        "csv",
        "zip"
    }

    # Cryptography Configuration
    PBKDF2_ITERATIONS = 600000
    SALT_SIZE = 16
    KEY_LENGTH = 32

    # Logging
    LOG_FILE = "logs/audit.log"

    # Security
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"

    # Set to True after deploying with HTTPS
    SESSION_COOKIE_SECURE = False