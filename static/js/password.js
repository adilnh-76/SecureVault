const password = document.getElementById("password");
const strength = document.getElementById("strength-text");

password.addEventListener("input", function () {

    const value = password.value;

    let score = 0;

    if (value.length >= 12)
        score++;

    if (/[A-Z]/.test(value))
        score++;

    if (/[a-z]/.test(value))
        score++;

    if (/[0-9]/.test(value))
        score++;

    if (/[^A-Za-z0-9]/.test(value))
        score++;

    if (score <= 2) {

        strength.innerHTML = "🔴 Weak Password";
        strength.style.color = "red";

    }
    else if (score == 3 || score == 4) {

        strength.innerHTML = "🟡 Medium Password";
        strength.style.color = "orange";

    }
    else {

        strength.innerHTML = "🟢 Strong Password";
        strength.style.color = "lightgreen";

    }

});

function togglePassword() {

    const password = document.getElementById("password");
    const eye = document.getElementById("eyeIcon");

    if (password.type === "password") {

        password.type = "text";

        eye.classList.remove("fa-eye");
        eye.classList.add("fa-eye-slash");

    } else {

        password.type = "password";

        eye.classList.remove("fa-eye-slash");
        eye.classList.add("fa-eye");

    }

}
const uploadBox = document.querySelector(".upload-box");
const fileInput = document.getElementById("file-upload");

uploadBox.addEventListener("dragover", function(e){
    e.preventDefault();
    uploadBox.classList.add("drag-active");
});

uploadBox.addEventListener("dragleave", function(){
    uploadBox.classList.remove("drag-active");
});

uploadBox.addEventListener("drop", function(e){

    e.preventDefault();

    uploadBox.classList.remove("drag-active");

    fileInput.files = e.dataTransfer.files;

    showFileName();

});
function showDecryptFileName(){

    const input = document.getElementById("decrypt-file-upload");

    const fileName = document.getElementById("decrypt-file-name");

    if(input.files.length > 0){

        fileName.innerHTML="✅ "+input.files[0].name;

    }
    else{

        fileName.innerHTML = "No encrypted file selected";

    }

}
const decryptUploadBox = document.querySelector("#decrypt-file-upload")?.previousElementSibling;
const decryptFileInput = document.getElementById("decrypt-file-upload");

if (decryptUploadBox && decryptFileInput) {

    decryptUploadBox.addEventListener("dragover", function(e){
        e.preventDefault();
        decryptUploadBox.classList.add("drag-active");
    });

    decryptUploadBox.addEventListener("dragleave", function(){
        decryptUploadBox.classList.remove("drag-active");
    });

    decryptUploadBox.addEventListener("drop", function(e){

        e.preventDefault();

        decryptUploadBox.classList.remove("drag-active");

        decryptFileInput.files = e.dataTransfer.files;

        showDecryptFileName();

    });

}
function showFileName() {

    const input = document.getElementById("file-upload");
    const fileName = document.getElementById("file-name");

    if (input.files.length > 0) {
        fileName.textContent = input.files[0].name;
    } else {
        fileName.textContent = "No file selected";
    }

}
function showFileName(){

    const input=document.getElementById("file-upload");
    const fileName=document.getElementById("file-name");
    const uploadBox=document.querySelector(".upload-box");

    if(input.files.length>0){

        fileName.textContent=input.files[0].name;

        uploadBox.classList.add("upload-success");

    }
}