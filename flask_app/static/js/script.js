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

const sizeChart = () => {
    chart = document.getElementById("size-chart");
    if (chart.style.display == "none") {
        chart.style.display = "block"
    } else {
        chart.style.display = "none"
    }
}

function magnify(imgID, zoom) {
    var img, glass, w, h, bw;
    img = document.getElementById(imgID);
    /*create magnifier glass:*/
    glass = document.createElement("DIV");
    glass.setAttribute("class", "img-magnifier-glass");
    /*insert magnifier glass:*/
    img.parentElement.insertBefore(glass, img);
    /*set background properties for the magnifier glass:*/
    glass.style.backgroundImage = "url('" + main.src + "')";
    glass.style.backgroundRepeat = "no-repeat";
    glass.style.backgroundSize = (img.width * zoom) + "px " + (img.height * zoom) + "px";
    glass.style.backgroundColor = "white";
    bw = 3;
    w = glass.offsetWidth / 2;
    h = glass.offsetHeight / 2;
    glass.style.display = "none"
    /*execute a function when someone moves the magnifier glass over the image:*/
    glass.addEventListener("mousemove", moveMagnifier);
    img.addEventListener("mousemove", moveMagnifier);
    /*and also for touch screens:*/
    glass.addEventListener("touchmove", moveMagnifier);
    img.addEventListener("touchmove", moveMagnifier);
    function moveMagnifier(e) {
    glass.style.backgroundImage = "url('" + main.src + "')";
      var pos, x, y;
      /*prevent any other actions that may occur when moving over the image*/
      e.preventDefault();
      /*get the cursor's x and y positions:*/
      pos = getCursorPos(e);
      x = pos.x;
      y = pos.y;
      /*prevent the magnifier glass from being positioned outside the image:*/
      if (x > img.width - (w / zoom)) glass.style.display = "none"
      if (x < w / zoom) glass.style.display = "none"
      if (y > img.height - (h / zoom)) glass.style.display = "none"
      if (y < h / zoom) glass.style.display = "none"
      if (x < img.width - (w / zoom) && x > w / zoom && y < img.height - (h / zoom) && y > h / zoom) glass.style.display = "block"
      /*set the position of the magnifier glass:*/
      glass.style.left = (e.pageX - w) + 'px';
      glass.style.top = (e.pageY - h) + 'px';
      /*display what the magnifier glass "sees":*/
      glass.style.backgroundPosition = "-" + ((x * zoom) - w + bw) + "px -" + ((y * zoom) - h + bw) + "px";
    }
    function getCursorPos(e) {
      var a, x = 0, y = 0;
      e = e || window.event;
      /*get the x and y positions of the image:*/
      a = img.getBoundingClientRect();
      /*calculate the cursor's x and y coordinates, relative to the image:*/
      x = e.pageX - a.left;
      y = e.pageY - a.top;
      /*consider any page scrolling:*/
      x = x - window.pageXOffset;
      y = y - window.pageYOffset;
      return {x : x, y : y};
    }
  }