const slideImages = document.querySelectorAll(".slide-in");
window.addEventListener("scroll", debounce(slideAction));

function slideAction(){
  slideImages.forEach(slideImage => {
    // https://stackoverflow.com/questions/41576287/why-window-scrolly-element-getboundingclientrect-top-is-not-equal-to-element
    // https://developer.mozilla.org/en-US/docs/Web/API/Window/innerHeight
    // slikdeIn은 현재 사용자의 view 위치를 Y값으로 받은 뒤(innerheightrk view에서 보이는 Y길이) 이미지의 크기의 50%를 뺀값, 
    //이 값이 이미지의 Top까지의 Y값 보다 크면(offsetTop) 충분히 지나감으로 확인 
    //sldieOut의 경우 scrollY가 viewport까지 거리임으로 그 거리가 이미지 전체 거리보다 멀어지면 remove하는 것 
    const slideIn = window.scrollY + window.innerHeight - slideImage.height /2 ;
    const slideOut = slideImage.offsetTop + slideImage.height;

    const isHalfShown = slideIn > slideImage.offsetTop;
    const isNotScolledPast =  window.scrollY < slideOut;
    
    if(isHalfShown && isNotScolledPast){
      slideImage.classList.add("active");
    }
    else{
      slideImage.classList.remove("active");
    }
  })
} 



//thorttle 일정한 시간 주기마다 발생하도록 하는 기술 
// debounce : 이벤트를 제한하는 역할 js의 성능 제한 , 연이어 호출되는 함수 중 마지막(혹은 처음만) 호출하도록 하는것  
function debounce(func, wait = 20, immediate = true) {
    var timeout;
    return function() {
      var context = this, args = arguments;
      var later = function() {
        timeout = null;
        if (!immediate) func.apply(context, args);
      };
      var callNow = immediate && !timeout;
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
      if (callNow) func.apply(context, args);
    };
  }

