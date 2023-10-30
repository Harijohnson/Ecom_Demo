let signupBtn= document.querySelector('#signupBtn');
let signinBtn= document.querySelector('#signinBtn');
let title= document.querySelector('#title');
let nameField=document.querySelector('#nameField');
let forgotPass=document.querySelector('.forgotPass');


console.log(forgotPass);

signinBtn.onclick = function() {
    nameField.style.maxHeight='0';
    title.innerHTML = 'Sign In';
    signupBtn.classList.add('disable');
    signinBtn.classList.remove('disable');
    forgotPass.style.display = 'block';
}
signupBtn.onclick = function() {
    nameField.style.maxHeight='60px';
    title.innerHTML = 'Sign Up';
    signinBtn.classList.add('disable');
    signupBtn.classList.remove('disable');
    forgotPass.style.display = 'none';
}