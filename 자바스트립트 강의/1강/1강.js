'use strict'
window.addEventListener("keydown", function(e){
    //audio to make sound, key to make css effect
    const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`)
    const key = document.querySelector(`.key[data-key="${e.keyCode}"]`)
    if(!audio) return; // if auio is null turn off
    audio.currentTime = 0; //rewind audio to start 
    audio.play();
    if(!key) return;
    key.classList.add("playing");
})

const keys = document.querySelectorAll(".key");
keys.forEach(key => key.addEventListener("transitionend", removePlaying));
function removePlaying(e){
    if(e.propertyName !== "transform") return;
    this.classList.remove("playing");
    //this는 자신을 로출한 함수에 바인딩 된다, 
    //내부함수의 경우 that을 사용해 접근 가능하게 한다
}
