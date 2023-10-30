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










































