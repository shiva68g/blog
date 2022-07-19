let home = document.getElementById('home');
let blogs = document.getElementById('blogs');
let about = document.getElementById('about');
let sign = document.getElementById('sign');
let logout = document.getElementsByClassName('logout');

let url = window.location.origin
home.addEventListener("click" , (a)=>{
     window.location.replace(url);
});
blogs.addEventListener("click" , (a)=>{
    window.location.replace(url+'/blogs')
});
about.addEventListener("click", (a)=>{
    window.location.replace(url+'/about')
});
if(sign != null){
sign.addEventListener("click" , (a)=>{
    window.location.replace(url+'/login')
});
}

function logouts(){
    window.location.replace(url+'/logout')
}