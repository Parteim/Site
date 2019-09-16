
let arrowRight = document.getElementById('arrow_right');
let arrowLeft = document.getElementById('arrow_left');
let winnersSlider = document.getElementById('winners__box');
let item = document.querySelectorAll('.winners__item');
let count = 0;
let countTwo = 0;
let indicate = false;

function startSlide(){
    if (item.length  > 3 && indicate == false){
        let callSlideFunc = setInterval(function  slideWinners(){
            console.log(count);
            let itemWinners = winnersSlider.children[0];
            count += 5;
            winnersSlider.style.transform = 'translateX(' + -count + 'px)';
            if (count >= ((item.length -3) * 390)) {
                count = 0;
            }
            if (indicate == true){
                clearInterval(callSlideFunc);
            }
        }, 80);
    }
}

startSlide();


winnersSlider.onmouseover = function(event){
    indicate = true;
}

winnersSlider.onmouseout = function(event){
    indicate = false;
    startSlide();
}

arrowRight.onclick = function () {
    let upcomingContestItem = document.querySelectorAll('.contests__body__box');
    let sliderUpcomingContest = document.getElementsByClassName('slider_upcoming_contests')[0];
    if (countTwo >= 0) {
        countTwo = -(upcomingContestItem.length -1) * 1260;
        sliderUpcomingContest.style.left = countTwo + 'px'; 
    }
    else {
        countTwo += 1260;
        sliderUpcomingContest.style.left = countTwo + 'px'; 
    }
}

arrowLeft.onclick = function () {
    let upcomingContestItem = document.querySelectorAll('.contests__body__box');
    let sliderUpcomingContest = document.getElementsByClassName('slider_upcoming_contests')[0];
    countTwo -= 1260;
    if (countTwo <= -(upcomingContestItem.length) * 1260 ) {
        countTwo = 0;
        sliderUpcomingContest.style.left = countTwo + 'px'; 
    }
    else {
        sliderUpcomingContest.style.left = countTwo + 'px';
    }
}


