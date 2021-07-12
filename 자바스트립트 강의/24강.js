const nav = document.querySelector("nav")
const navTop = nav.offsetTop
//navTop cosnt로 안받고 if  문에서 바로 nav.offsetTop 사용하면 계속 유동적으로 값이 변해서 else 작동 안함 주의!
window.addEventListener("scroll", fixedNav);

function fixedNav(){
    if(window.scrollY >= navTop ){
        document.body.style.paddingTop = nav.offsetHeight;
        document.body.classList.add("fixedNav");
    }
    else{
        document.body.classList.remove("fixedNav");
        document.body.paddingTop = 0;
    }
}
