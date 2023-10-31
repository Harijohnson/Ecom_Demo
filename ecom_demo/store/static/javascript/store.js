let signupBtn= document.querySelector('#signupBtn');
let signinBtn= document.querySelector('#signinBtn');
let title= document.querySelector('#title');
let nameField=document.querySelector('#nameField');
let forgotPass=document.querySelector('.forgotPass');
let conBtn = document.querySelector('#con-btn');

const username= document.querySelector('#username').value;
const email = document.querySelector('#email').value;
const password = document.querySelector('#password').value;
const cPass = document.querySelector('#c-password').value;


console.log(username);
console.log( email);
console.log(password);
console.log(cPass);

signinBtn.onclick = function() {
    nameField.style.maxHeight='0';
    title.innerHTML = 'Sign In';
    signupBtn.classList.add('disable');
    signinBtn.classList.remove('disable');
    forgotPass.style.display = 'block';
    conBtn.style.display="none";

    // condition for button and submit
    if (username !== "" && email!== "" && password !== "" && cPassword !== "" )
    {
        signinBtn.type='submit';
    }    
    else{
    signupBtn.type='button';
    }
}
signupBtn.onclick = function() {
    nameField.style.maxHeight='60px';
    title.innerHTML = 'Sign Up';
    signinBtn.classList.add('disable');
    signupBtn.classList.remove('disable');
    forgotPass.style.display = 'none';
    conBtn.style.display="flex";
    if (email!== "" && password !== "")
    {
        signupBtn.type='submit';
    }    
    else{
        signinBtn.type='button';
    }
    }
   
    

