main = document.getElementById("main_image");
front = document.getElementById("Front");
back = document.getElementById("Back");
design = document.getElementById("Design");

function changeView(element, img) {
    element.src = img;
}

function changeMain(element) {
    main.src = element.src;
}

function changeColor(back_img, front_img, design_img){
    main.src = back_img;
    front.src = front_img;
    back.src = back_img;
    design.src = design_img;
}

// function changeColor(pictures){
//     console.log(pictures)
//     for (const picture in pictures) {
//         const element = document.getElementById(pictures[picture].name);
//     }
// }

function swapColor(productid, back, front){
    product = document.getElementById(productid);
    product.src = back;
    product.onmouseover = function() {changeView(this, front)}
    product.onmouseout = function() {changeView(this, back)}
}