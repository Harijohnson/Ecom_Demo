// function showSidebar(){
//     const sidebar= document.querySelector('.sidebar');
//     sidebar.style.display ='flex';

// }

// function closeMenuBar(){
//     const sidebar= document.querySelector('.sidebar');
//     sidebar.style.display ='none';
    
// }

const header=document.querySelector("header");

window.addEventListener('scroll', function(){
    header.classList.toggle('sticky',this.window.scrollY>0);
})

let menu = document.querySelector("#menu-icon");
let navmenu= document.querySelector(".navmenu");

menu.onclick = () =>{
    menu.classList.toggle('bx-x');
    navmenu.classList.toggle('open');
}


function shoeSmallMenu(){
    const samllMenu = document.querySelector('#menu-icon');
    samllMenu.style.display ='flex';

}


function hideSmallMenu(){
    const samllMenu = document.querySelector('#menu-icon');
    samllMenu.style.display ='none';

}







































