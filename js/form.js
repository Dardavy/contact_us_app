let id = (id) => document.getElementById(id);
let classes = (classes) => document.getElementsByClassName(classes);


let userName = id('username'),

email = id('email'),

password = id('password'),

password2 = id('password2'),

errorMsg = classes('error'),

success = classes('success'),

failure = classes('failure'),

form = id("form");


// add eventlister to form
form.addEventListener('submit', (e) => {
    e.preventDefault();

logic(userName, 0, 'username can not be empty')

logic(email, 1, 'email can not be empty')

logic(password, 2, 'password can not be empty')

logic(password2, 3, 'password can not be empty')

}
)

let logic = (id, serial, message) => {

    if (id.value.trim() === "") {
        errorMsg[serial].innerHTML = message;
        id.style.border = "3px solid red";
        failure[serial].style.opacity = '1';
        success[serial].style.opacity ='0';
    }
    
    else {
        errorMsg[serial].innerHTML = "";
        id.style.border = " 3px solid green";
        failure[serial].style.opacity = '0'
        success[serial].style.opacity ='1';
    }

}




