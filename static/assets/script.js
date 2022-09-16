const dropArea = document.querySelector(".drag-area");
const result = document.querySelector(".prediction-result");
const dragText = dropArea.querySelector("header");
const button = dropArea.querySelector("button");
const input = dropArea.querySelector("input");

let file;

input.addEventListener("change", handleFiles);
function handleFiles() {
  file = this.files[0];
  dropArea.classList.add("active");
  showFile();
}

dropArea.addEventListener("dragover", (e) => {
  e.preventDefault();
  dragText.textContent = "Drop to Upload File";
  dropArea.classList.add("active");
});

dropArea.addEventListener("dragleave", (e) => {
  dragText.textContent = "Drag & Drop to Upload File";
  dropArea.classList.remove("active");
});

dropArea.addEventListener("drop", (e) => {
  e.preventDefault();
  file = e.dataTransfer.files[0];
  showFile();
});

function showFile() {
  let fileType = file.type;
  let validation = ["image/jpeg", "image/jpg", "image/png"];
  if (validation.includes(fileType)) {
    let fileReader = new FileReader();
    fileReader.onload = () => {
      let fileUrl = fileReader.result;
      let imgTag = `<img src="${fileUrl}" alt="user-image">`;
      document.getElementById("imgcontainer").innerHTML = imgTag;
      dropArea.style.display = "none";
    };
    fileReader.readAsDataURL(file);
  } else {
    alert("This is not an Image File!");
    dropArea.classList.remove("active");
    dragText.textContent = "Drag & Drop to Upload File";
  }
}

setTimeout(function () {
  result.classList.add("vanish");
}, 5000);
