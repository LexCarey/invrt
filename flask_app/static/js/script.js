main = document.getElementById("main_image");
front = document.getElementById("front-img");
back = document.getElementById("back-img");
patch = document.getElementById("patch-img");

function changeView(element, img) {
    element.src = img;
}

function changeMain(element) {
    main.src = element.src;
}

function changeColor(front_img, back_img, patch_img){
    main.src = back_img;
    front.src = front_img;
    back.src = back_img;
    patch.src = patch_img;
}

function swapColor(productid, back, front){
    product = document.getElementById(productid);
    product.src = back;
    product.onmouseover = function() {changeView(this, front)}
    product.onmouseout = function() {changeView(this, back)}
}