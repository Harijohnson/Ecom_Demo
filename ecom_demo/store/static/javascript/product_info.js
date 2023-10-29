let productImg =document.querySelector('#productImg');
let btn = document.getElementsByClassName('btn');



// http://127.0.0.1:8000/static/images/product3.png


// console.log(productImg.src)
btn[0].onclick = function (){
    // productImg.src ="{% static 'static/images/product1.png' %}";  this is not working in js
    productImg.src ="../static/images/product1.png";  // this is working in js 
    for (bt of btn) {
        bt.classList.remove('active');
    }
    this.classList.add('active');

}
btn[1].onclick = function (){
    productImg.src ="../static/images/product2.png";
    for (bt of btn) {
        bt.classList.remove('active');
    }
    this.classList.add('active');
}

btn[2].onclick = function (){
    productImg.src ="../static/images/product3.png";
    for (bt of btn) {
        bt.classList.remove('active');
    }
    this.classList.add('active');
}



























































