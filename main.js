let title=document.querySelector("#title");
let header = document.querySelector("header");
let text=["Get The Best Result Out Of Your Effort","Achieve Your Dreams With Us","Register Now","With Us Everything Is Easier"];
let photos = ["course-1","course-2","course-3","course-4"];
let i=0;

function change() {
    i = i+1
    if(i>text.length-1){
        i=0
    }
    title.innerHTML = `${text[i]}`;
    header.style.cssText = `background-image:linear-gradient(rgba(4,9,30,0.45),rgba(4,9,30,0.3)),url(images/${photos[i]}.jpg);`
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

const nav = document.getElementById("nav")
const line = document.getElementById("line")
window.addEventListener('scroll',() =>{
    if (scrollY >= 600){
        line.style.cssText =  "display:block"
        
    }else{
        line.style.cssText =  "display:none"
    }})


const card = document.getElementsByClassName("card")  



