
const fileInput = document.querySelector('input[id="fileUpload"]');
const reader = new FileReader();
document.getElementById("uploadButton").style.display = 'none';


fileInput.addEventListener('change', (e) => {
    const selectedFile = fileInput.files[0];
    if (selectedFile) {
        console.log(selectedFile.name);
        reader.readAsDataURL(selectedFile);
        document.querySelector('.fileName').textContent = selectedFile.name;
        document.getElementById("uploadButton").style.display = 'block';
    }
});


function uploadFile() {
    console.log(reader);
}