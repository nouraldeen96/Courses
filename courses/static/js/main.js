let title=document.querySelector("#title");
let header = document.querySelector("header");
let text=["Get The Best Result Out Of Your Effort","Achieve Your Dreams With Us","Register Now","With Us Everything Is Easier"]
let photos = ["course-5","course-2","course-3","course-1"];
let i=0;

function change() {
    i = i+1
    if(i>text.length-1){
        i=0
    }
    title.innerHTML = `${text[i]}`;
    header.style.cssText = `background-image:linear-gradient(rgba(4,9,30,0.45),rgba(4,9,30,0.3)),url("./static/images/${photos[i]}.jpg");`
};

setInterval(change,4500)



const up = document.getElementById("up")
window.addEventListener('scroll',() =>{
    if (scrollY >= 600){
        up.style.display = "block"
 
    }else{
        up.style.display = "none"
     
    }
})

up.onclick = function(){
    window.scrollTo(0,0)
}

// Register
function checkInputs(){
    
}
const form = document.getElementById('register_form');
const username = document.getElementById('register_name');
const email = document.getElementById('register_email');
const phone = document.getElementById('register_phone');
const password = document.getElementById('register_password');
const password2 = document.getElementById('register_password2');
const reg_btn= document.getElementById('register_password2');

form.addEventListener('submit', e => {
    e.preventDefault();})


const setError = (element, message) => {
  const inputControl = element.parentElement;
  const errorDisplay = inputControl.querySelector('.error');

  errorDisplay.innerText = message;
  inputControl.classList.add('error');
  inputControl.classList.remove('success')
}

const setSuccess = element => {
  const inputControl = element.parentElement;
  const errorDisplay = inputControl.querySelector('.error');

  errorDisplay.innerText = '';
  inputControl.classList.add('success');
  inputControl.classList.remove('error');
};

let check=[]
const isValidName = username => {
  const re = /[^\w+\s]/g;
  return re.test(String(username))
}

const isValidEmail = email => {
  const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(String(email).toLowerCase());
}

const isValidPhone = phone => {
const re = /[^0-9]/g;
return re.test(String(phone))
}

const isValidPassword = password => {
const re = /[^\w]/g;
return re.test(String(password))
}
let status1 = "false"
let status2 = "false"
let status3 = "false"
let status4 = "false"
let status5 = "false"


function validateInputs(){
  const usernameValue = username.value.trim();
  const emailValue = email.value.trim();
  const phoneValue = phone.value;
  const passwordValue = password.value.trim();
  const password2Value = password2.value.trim();
 

  if(usernameValue === '') {
      setError(username, 'Username is required');
      status1 = "false"
  } else if (isValidName(usernameValue)){
      setError(username, 'Provide a valid username');
      status1 = "false"
  }
  else {
      setSuccess(username);
      status1 = "true"
     
  }

  if(emailValue === '') {
      setError(email, 'Email is required');
      status2 = "false"
  } else if (!isValidEmail(emailValue)) {
      setError(email, 'Provide a valid email address');
      status2 = "false"
  } else {
      setSuccess(email);
      status2 = "true"
     
  }

  if(phoneValue === '') {
    setError(phone, 'Phone is required');
    status3 = "false"
  } else if (isValidPhone(phoneValue)){
      setError(phone, 'Provide a valid phone number');
      status3 = "false"
  } else if (phoneValue.length != 10){
    setError(phone, 'Provide a valid phone number');
    status3 = "false"
  }
  else {
      setSuccess(phone);
      status3 = "true"
  }


  if(passwordValue === '') {
      setError(password, 'Password is required');
      status4 = "false"
  } else if (passwordValue.length < 8 ) {
      setError(password, 'Password must be at least 8 character.')
      status4 = "false"
  }else if (isValidPassword(passwordValue)){
    setError(password, 'Provide a valid phone number');
    status4 = "false"
  }  
   else {
      setSuccess(password);
      status4 = "true"
  }

  if(password2Value === '') {
      setError(password2, 'Please confirm your password');
      status5 = "false"
  } else if (password2Value !== passwordValue) {
      setError(password2, "Passwords doesn't match");
      status5 = "false"
  } else {
      setSuccess(password2);
      status5 = "true"
  }
  

};


function Register(){
    validateInputs()
    if(status1=="true" && status2=="true" && status3=="true"&& status4=="true"&& status5=="true"){
        let registerModel = document.getElementById("register") 
        const modalInstance = bootstrap.Modal.getInstance(registerModel)
        let name = document.getElementById("register_name").value
        let password = document.getElementById("register_password").value
        let email = document.getElementById("register_email").value
        let phone = document.getElementById("register_phone").value
        const params = {
          "name":name,
          "password":password,
          "email":email,
          "phone":phone
        }
      
        axios.post(`/newuser`,params)
        .then(function (response) {
        console.log(response.request.response)
        modalInstance.hide()
        Swal.fire(response.request.response, '', 'success')
        setTimeout(function(){
          const params = {
            "name":name,
            "password":password
          }
          axios.post(`/login`,params)
          .then(function (response) {
            Swal.fire("Logged in Successfuly", '', 'success')
            localStorage.setItem('token',response.data.token)
            localStorage.setItem('text_user',response.data.text_name)
            localStorage.setItem('photo',response.data.photo)
            localStorage.setItem('email',response.data.email)
            localStorage.setItem('phone',response.data.phone)
            modalInstance.hide()
            setTimeout(function(){
                window.location.reload()
              } ,2000)
              return 
            
          })
        } ,2500)

        
   
       
        
        
        }).catch(function (response) {
          Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: response.request.response,
          })
         })
    }
  
  }


