let nav = document.getElementById('all_link_in_menu');
let nav_box = this.document.querySelectorAll('.adaptive_nav_box')[0];
let navBar = document.getElementById('nav__bar');

window.addEventListener('scroll', function() {
    
    let link = document.getElementsByClassName('item__main__nav__link');
    let main__bloc__nav = document.getElementById('main__nav__bar');
    let buttonSignIn = document.getElementsByClassName('btn__sign__in');
    if (window.scrollY >= 30) {
        // console.log('main__bloc__nav', main__bloc__nav.style.height)
        navBar.style.height = '50px';
        main__bloc__nav.style.height = '50px';
        navBar.style.background = '#252424';
        if (window.innerWidth <= 1024) {
            nav_box.style.height = '40px';
            nav_box.style.width = '40px';
            nav.style.display = 'none';
            
        }
        else {
            nav.style.display = 'block';
        }
        // buttonSignIn.style.fontSize = '12px';
        for (let k = 0; k <  buttonSignIn.length; k++) {
            buttonSignIn[k].style.fontSize = '12px';
        }
        for (let i = 0; i < link.length ; i++) {
            link[i].style.color = '#f8f8f8';
            link[i].style.fontSize = '12px';
        }
    }
    else {
        navBar.style.height = "80px";
        main__bloc__nav.style.height = '80px';
        navBar.style.background = '#f8f8f8';
        // buttonSignIn.style.fontSize = '14px';
        if (window.innerWidth <= 415) {
            nav_box.style.height = '50px';
            nav_box.style.width = '50px';
            
        }
        for (let k = 0; k <  buttonSignIn.length; k++) {
            buttonSignIn[k].style.fontSize = '14px';
        }
        for (let i = 0; i < link.length; i++) {
            link[i].style.color = '#252424';
            link[i].style.fontSize = '14px';
        }
    }

})



nav_box.onclick = function(){

    if (nav.style.display == 'block'){
        nav.style.display = 'none';
    }
    else {
        nav.style.display = 'block';
    }

    if (navBar.style.height == '50px'){
        nav.style.backgroundColor = '#252424';
    }
    else {
        nav.style.backgroundColor = '#f8f8f8';
    }

    nav.style.top = navBar.style.height;
}




// console.log(window.innerWidth)



// activImgGallery.addEventListener('scroll', function(){
//     console.log('aaaa')
// })

// newsImgBox.addEventListener('mouseover', function(){
//     let description = document.getElementById('news__img__description');
//     console.log('ffff')
//     setTimeout(description.style.display = 'block', 1000);
    
// })
// newsImgBox.addEventListener('mouseout', function(){
//     let description = document.getElementById('news__img__description');
//     setTimeout(description.style.display = 'none', 1000);
// })
