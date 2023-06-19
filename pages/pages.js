document.addEventListener("DOMContentLoaded", function() {
    var modal = document.createElement("div");
    modal.classList.add("modal");

    var modalContent = document.createElement("img");
    modalContent.classList.add("modal-content");
    modal.appendChild(modalContent);

    var closeModal = document.createElement("span");
    closeModal.innerHTML = "&times;";
    closeModal.classList.add("close");
    modal.appendChild(closeModal);

    var leftArrow = document.createElement("span");
    leftArrow.innerHTML = "&#10094;";
    leftArrow.classList.add("arrow", "left");
    modal.appendChild(leftArrow);

    var rightArrow = document.createElement("span");
    rightArrow.innerHTML = "&#10095;";
    rightArrow.classList.add("arrow", "right");
    modal.appendChild(rightArrow);

    document.body.appendChild(modal);

    var images = document.querySelectorAll(".card");
    var currentImageIndex;

    images.forEach(function(img, index) {
        img.addEventListener("click", function() {
            currentImageIndex = index;
            modalContent.src = this.src;
            modal.style.display = "block";
        });
    });

    closeModal.addEventListener("click", function() {
        modal.style.display = "none";
    });

    window.addEventListener("click", function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    });

    leftArrow.addEventListener("click", function() {
        if (currentImageIndex > 0) {
            currentImageIndex--;
        } else {
            currentImageIndex = images.length - 1;
        }
        modalContent.src = images[currentImageIndex].src;
    });

    rightArrow.addEventListener("click", function() {
        if (currentImageIndex < images.length - 1) {
            currentImageIndex++;
        } else {
            currentImageIndex = 0;
        }
        modalContent.src = images[currentImageIndex].src;
    });
});
