main = document.getElementById("main_image");
front = document.getElementById("Front");
back = document.getElementById("Back");
design = document.getElementById("Design");
modelback = document.getElementById("ModelBack");
modelfront = document.getElementById("ModelFront");
xsbutton = document.getElementById("xs");
sbutton = document.getElementById("s");
mbutton = document.getElementById("m");
lbutton = document.getElementById("l");
xlbutton = document.getElementById("xl");
addcart = document.getElementById("AddCartButton");
menu = document.getElementById("side-menu");
quantity = document.getElementById("quantity");

const updateQuantity = (amount) => {
    var i, L = quantity.options.length - 1;
    for(i = L; i >= 0; i--) {
        quantity.remove(i);
    }
    if (amount>0) {
        for (let j = 1; j<=amount; j++){
            var opt = document.createElement('option');
            opt.value = j;
            opt.innerHTML = j;
            quantity.appendChild(opt);
        }
        addcart.value = "Add To Cart"
        addcart.disabled = false
    } else {
        var opt = document.createElement('option');
        opt.value = 0;
        opt.innerHTML = 0;
        quantity.appendChild(opt);
        addcart.value = "Size Sold Out"
        addcart.disabled = true
    }
}

const changeView = (element, img) => {
    element.src = img;
}

const changeMain = (element) => {
    main.src = element.src;
}

const changeColor = (xs, s, m, l, xl, back_img, front_img, design_img, modelback_img=null, modelfront_img=null) =>{
    main.src = back_img;
    front.src = front_img;
    back.src = back_img;
    design.src = design_img;
    if (modelback_img == null){
        modelback.src = null
        modelback.style.display = "none"
    } else {
        modelback.src = modelback_img
        modelback.style.display = "block"
    }
    if (modelfront_img == null){
        modelfront.src = null
        modelfront.style.display = "none"
    } else {
        modelfront.src = modelfront_img
        modelfront.style.display = "block"
    }
    xsbutton.onclick = function() {updateQuantity(xs)}
    if (xsbutton.checked) {
        updateQuantity(xs)
    }
    sbutton.onclick = function() {updateQuantity(s)}
    if (sbutton.checked) {
        updateQuantity(s)
    }
    mbutton.onclick = function() {updateQuantity(m)}
    if (mbutton.checked) {
        updateQuantity(m)
    }
    lbutton.onclick = function() {updateQuantity(l)}
    if (lbutton.checked) {
        updateQuantity(l)
    }
    xlbutton.onclick = function() {updateQuantity(xl)}
    if (xlbutton.checked) {
        updateQuantity(xl)
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

const openmenu = () => {
    menu.classList.add("menu-open")
}

const closemenu = () => {
    menu.classList.remove("menu-open")
}