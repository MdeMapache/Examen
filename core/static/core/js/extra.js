const btnSwitch = document.querySelector('#switch');

btnSwitch.addEventListener('click',() =>{
    document.body.classList.toggle('dark');
    btnSwitch.classList.toggle('active');

    //guardar el modo
    if(document.body.classList.contains('dark')){

        localStorage.setItem('dark-modo','true');
    }else{
        localStorage.setItem('dark-modo','false');

    }
});

//obtenermos el modo en el que estamos
if(localStorage.getItem('dark-modo') === 'true'){
    document.body.classList.add('dark');
    btnSwitch.classList.add('active');
}else{
    document.body.classList.remove('dark');
    btnSwitch.classList.remove('active');
}