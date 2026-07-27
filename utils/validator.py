import re
from config import Config


def allowed_file(filename):
    """
    Check whether the uploaded file has an allowed extension.
    """

    if "." not in filename:
        return False

    extension = filename.rsplit(".", 1)[1].lower()

    return extension in Config.ALLOWED_EXTENSIONS


def validate_password(password):
    """
    Validate password strength.
    Returns (True, "") if valid,
    otherwise (False, error_message)
    """

    if len(password) < 12:
        return False, "Password must contain at least 12 characters."

    if not re.search(r"[A-Z]", password):
        return False, "Password must contain an uppercase letter."

    if not re.search(r"[a-z]", password):
        return False, "Password must contain a lowercase letter."

    if not re.search(r"\d", password):
        return False, "Password must contain a number."

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=/\\[\];'`~]", password):
        return False, "Password must contain a special character."

    return True, ""


def validate_uploaded_file(uploaded_file):
    """
    Validate uploaded file.
    Returns (True, "") if valid.
    """

    if uploaded_file.filename == "":
        return False, "No file selected."

    if not allowed_file(uploaded_file.filename):
        return False, "Unsupported file type."

    return True, ""