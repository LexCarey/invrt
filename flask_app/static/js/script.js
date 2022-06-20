main = document.getElementById("main_image");
front = document.getElementById("Front");
back = document.getElementById("Back");
design = document.getElementById("Design");
xsbutton = document.getElementById("xs");
sbutton = document.getElementById("s");
mbutton = document.getElementById("m");
lbutton = document.getElementById("l");
xlbutton = document.getElementById("xl");
addcart = document.getElementById("AddCartButton");

const changeView = (element, img) => {
    element.src = img;
}

const changeMain = (element) => {
    main.src = element.src;
}

const changeColor = (xs, s, m, l, xl, back_img, front_img, design_img) =>{
    main.src = back_img;
    front.src = front_img;
    back.src = back_img;
    design.src = design_img;
    xsbutton.onclick = function() {changeSize(xs)}
    if (xsbutton.checked) {
        changeSize(xs)
    }
    sbutton.onclick = function() {changeSize(s)}
    if (sbutton.checked) {
        changeSize(s)
    }
    mbutton.onclick = function() {changeSize(m)}
    if (mbutton.checked) {
        changeSize(m)
    }
    lbutton.onclick = function() {changeSize(l)}
    if (lbutton.checked) {
        changeSize(l)
    }
    xlbutton.onclick = function() {changeSize(xl)}
    if (xlbutton.checked) {
        changeSize(xl)
    }

}

// function changeColor(pictures){
//     console.log(pictures)
//     for (const picture in pictures) {
//         const element = document.getElementById(pictures[picture].name);
//     }
// }

const swapColor = (productid, back, front) => {
    product = document.getElementById(productid);
    product.src = back;
    product.onmouseover = function() {changeView(this, front)}
    product.onmouseout = function() {changeView(this, back)}
}

const changeSize = (stock) => {
    quantity = document.getElementById("quantity");
    quantity.max = stock
    if (stock>0) {
        quantity.value = 1
        quantity.min = 1
        addcart.value = "Add To Cart"
        addcart.disabled = false
    } else {
        quantity.value = 0
        quantity.min = 0
        addcart.value = "Size Sold Out"
        addcart.disabled = true
    }
}