const divs = document.querySelectorAll("div");
const btn = document.querySelector("button");

function logText(e){
    console.log(this.classList.value);
    //e.stopPropagation(); // bubble 방지
}

divs.forEach(div => div.addEventListener("click", logText, {
    capture: true, //default attribut is false ->top down 
    once: true // click을 한번으로 막음 
})) ;

btn.addEventListener("click", () => {
    console.log("clicked")
    , { once: true}
});
