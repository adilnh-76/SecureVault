import os
import io
import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

from config import Config


def derive_key(password, salt):
    """
    Generate a secure encryption key from the user's password.
    """

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=Config.KEY_LENGTH,
        salt=salt,
        iterations=Config.PBKDF2_ITERATIONS,
        backend=default_backend()
    )

    key = base64.urlsafe_b64encode(
        kdf.derive(password.encode())
    )

    return key


def encrypt_file(uploaded_file, password):
    """
    Encrypt the uploaded file.
    """

    # Generate random salt
    salt = os.urandom(Config.SALT_SIZE)

    # Generate encryption key
    key = derive_key(password, salt)

    # Create Fernet object
    fernet = Fernet(key)

    # Read file data
    data = uploaded_file.read()

    # Encrypt file
    encrypted_data = fernet.encrypt(data)

    # Save salt + encrypted data
    final_data = salt + encrypted_data

    output = io.BytesIO(final_data)
    output.seek(0)

    filename = uploaded_file.filename + ".enc"

    return output, filename


def decrypt_file(enc_file, password):
    """
    Decrypt an encrypted file.
    """

    encrypted_content = enc_file.read()

    salt = encrypted_content[:Config.SALT_SIZE]

    encrypted_data = encrypted_content[Config.SALT_SIZE:]

    key = derive_key(password, salt)

    fernet = Fernet(key)

    decrypted_data = fernet.decrypt(encrypted_data)

    output = io.BytesIO(decrypted_data)
    output.seek(0)

    filename = enc_file.filename.replace(".enc", "")

    return output, filename