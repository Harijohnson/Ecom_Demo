let signupBtn= document.querySelector('#signupBtn');
let signinBtn= document.querySelector('#signinBtn');
let title= document.querySelector('#title');
let nameField=document.querySelector('#nameField');
let forgotPass=document.querySelector('.forgotPass');
let conBtn = document.querySelector('#con-btn');


    // let username= document.querySelector('#username').value;
    // let email = document.querySelector('#email').value;
    // let password = document.querySelector('#password').value;
    // let cPass = document.querySelector('#c-password').value;

    
//     if (username !== "" && email!== "" && password !== "" && cPass !== "" )
//     {
//         signinBtn.type='button';
//     }    
//     else{
//     signupBtn.type='submit';
//     }



// function credChec(){
//     const email = document.querySelector('#email').value;
//     const password = document.querySelector('#password').value;
//     console.log('SIGIN IN ', email);
//     console.log('SIGIN IN ',password);
//     if (email!== "" && password !== "")
//     {
//         signupBtn.type='buttton';
//     }    
//     else{
//         signinBtn.type='submit';
//     }


// }


// second executes

signinBtn.onclick = function() {
    let email = document.querySelector('#email').value;
    let password = document.querySelector('#password').value;
    
    console.log('SIGIN IN ', email);
    console.log('SIGIN IN ',password);
    nameField.style.maxHeight='0';
    title.innerHTML = 'Sign In';
    signupBtn.classList.add('disable');
    signinBtn.classList.remove('disable');
    forgotPass.style.display = 'block';
    conBtn.style.display="none";
    if (email!== "" && password !== "")
    {
        signinBtn.type='submit';
    }    
    else{
        signupBtn.type='button';
        // location.reload()
    }
}


// first execute
signupBtn.onclick = function() {
    let username= document.querySelector('#username').value;
    let email = document.querySelector('#email').value;
    let password = document.querySelector('#password').value;
    let cPass = document.querySelector('#c-password').value;

    console.log('sign up',username, email, password, cPass)
    nameField.style.maxHeight='60px';
    title.innerHTML = 'Sign Up';
    signinBtn.classList.add('disable');
    signupBtn.classList.remove('disable');
    forgotPass.style.display = 'none';
    conBtn.style.display="flex";
    
    if (username !== "" && email!== "" && password !== "" && cPass !== "" )
    {
        signupBtn.type='submit';
    }    
    else{
      
    signinBtn.type='button';
    
    }
    }
   
    

