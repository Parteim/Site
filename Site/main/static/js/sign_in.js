

let emailLabel = document.getElementsByTagName('label')


// emailLabel.innerHTML ='E-mail'
for (let i= 0; i < emailLabel.length; i++) {
    if (emailLabel[i].innerHTML == 'Username:') {
        emailLabel[i].innerHTML = 'E-mail';
    }
    else if (emailLabel[i].innerHTML == 'Who is:') {
        emailLabel[i].innerHTML = 'Вы:';
    }
}