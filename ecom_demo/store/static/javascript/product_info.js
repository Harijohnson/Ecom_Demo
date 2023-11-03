let productImg =document.querySelector('#productImg');
let btn = document.getElementsByClassName('btnCng');





// http://127.0.0.1:8000/static/images/product3.png


console.log(btn)


btn[0].onclick = function (){
    // productImg.src ="{% static 'static/images/product1.png' %}";  this is not working in js
    productImg.src ="../static/images/products/product1.png";  // this is working in js 
    for (bt of btn) {
        bt.classList.remove('active');
    }
    this.classList.add('active');

}
btn[1].onclick = function (){
    productImg.src ="../static/images/products/product2.png";
    for (bt of btn) {
        bt.classList.remove('active');
    }
    this.classList.add('active');
}

btn[2].onclick = function (){
    console.log('3 but clicked')
    productImg.src ="../static/images/products/product3.png";
    for (bt of btn) {
        bt.classList.remove('active');
    }
    this.classList.add('active');
}



























































