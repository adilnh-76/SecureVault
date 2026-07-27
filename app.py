from flask import Flask, render_template,request,send_file
from config import Config
from utils.crypto import encrypt_file, decrypt_file
from utils.validator import (
    validate_password,
    validate_uploaded_file
)
from cryptography.fernet import InvalidToken
from logger import logger


app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/encrypt", methods=["GET", "POST"])
def encrypt():

    if request.method == "POST":

        uploaded_file = request.files.get("file")
        password = request.form.get("password")

        # Validate file
        valid, message = validate_uploaded_file(uploaded_file)

        if not valid:
            return render_template(
                "encrypt.html",
                error=message
            )

        # Validate password
        valid, message = validate_password(password)

        if not valid:
            return render_template(
                "encrypt.html",
                error=message
            )

        output, filename = encrypt_file(
            uploaded_file,
            password
        )
        logger.info(
            f"ENCRYPT SUCCESS | File={uploaded_file.filename}"
        )

        return send_file(
            output,
            as_attachment=True,
            download_name=filename
        )

    return render_template("encrypt.html")

@app.route("/decrypt", methods=["GET", "POST"])
def decrypt():

    if request.method == "POST":

        enc_file = request.files.get("enc_file")
        password = request.form.get("password")

        if not enc_file:
            return render_template(
                "decrypt.html",
                error="Please select an encrypted file."
            )

        try:

            output, filename = decrypt_file(
                enc_file,
                password
            )
            
            logger.info(
               f"DECRYPT SUCCESS | File={filename}"
            )

            return send_file(
                output,
                as_attachment=True,
                download_name="decrypted_" + filename
            )

       
        except InvalidToken:

            logger.warning(
                f"DECRYPT FAILED | File={enc_file.filename}"
            )

            return render_template(
                "decrypt.html",
                error="Invalid password or corrupted encrypted file."
            )

            

        except Exception:
            
            logger.error(
                f"DECRYPT ERROR | File={enc_file.filename} | Error={e}"
            )
            

            return render_template(
                "decrypt.html",
                error="Unable to decrypt the selected file."
            )

    return render_template("decrypt.html")

if __name__ == "__main__":
    app.run(debug=True)
    