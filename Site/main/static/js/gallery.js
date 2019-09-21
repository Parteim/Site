let photos = document.querySelectorAll('.gallery__item');
let htmlBody = document.body;
let revealImgBox = document.getElementById('reveal__img');
let revealImg = document.querySelectorAll('.img_gallery__reveal')[0]
// let indicate = false;

// function resize(revealImg){
//     if (indicate == true){
//         window.onscroll = function(event){
//             console.log('event');
//             console.log(event);
//         }
//     }
// }

photos.forEach(function(photo, key, photos) {
    photo.onclick = function() {
        revealImgBox.className = 'reveal__img';
        revealImg.src = photo.children[0].src;

        // revealImg.onmouseover = function(){
        //     indicate = true;
        //     resize(revealImg);
        // }

        // revealImg.onmouseout = function(){
        //     indicate = false;
        // }

        revealImgBox.onclick = function() {
            revealImgBox.className = '';
            revealImg.src = '';  
            htmlBody.style.overflowY = '';
        }
    }
})

