let productImg =document.querySelector('#productImg');
let btn = document.getElementsByClassName('btn');


btn[0].onclick = function (){
    productImg.src ="{% static 'images/product1.png' %}";
    // for (bt of btn) {
    //     bt.classList.remove('active');
    // }
    // this.classList.add('active');

}
btn[1].onclick = function (){
    productImg.src ="{% static 'images/product2.png' %}";
    // for (bt of btn) {
    //     bt.classList.remove('active');
    // }
    // this.classList.add('active');
}

btn[2].onclick = function (){
    productImg.src ="{% static 'images/product2.png' %}";
    // for (bt of btn) {
    //     bt.classList.remove('active');
    // }
    // this.classList.add('active');
}



























































