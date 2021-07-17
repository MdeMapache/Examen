const galeria = document.querySelectorAll(".galeria .imagen"),
    vistaCaja = document.querySelector(".vista-caja"),
    vistaImg = vistaCaja.querySelector("img"),
    closeIcon = vistaCaja.querySelector(".icon"),
    imgCompleta = vistaCaja.querySelector(".img-completa"),
    totalImg = vistaCaja.querySelector(".total-img");
    


    window.onload = ()=>{
        for (let i = 0; i < galeria.length; i++){
            totalImg.textContent = galeria.length
            let newIndex = i;
            galeria[i].onclick = ()=>{
                console.log(i);
                function preview(){
                    imgCompleta.textContent = newIndex +1;
                    let selectedImgUrl = galeria[newIndex].querySelector("img").src;
                    vistaImg.src = selectedImgUrl;
                 
                }
                const prevBtn = document.querySelector(".prev");
                const nextBtn = document.querySelector(".next");
                if (newIndex == 0) { //if index value is equal to 0 then hide prevBtn
                    prevBtn.style.display = "none";
                }
                if (newIndex >= galeria.length -1) { //if index value is greater and equal to gallery length by -1 then hide nextBtn
                    nextBtn.style.display = "none";
                }
                prevBtn.onclick = () => {
                    newIndex--; //decrement index
                    if (newIndex == 0) {
                        preview();
                        prevBtn.style.display = "none";
                    } else {
                        preview();
                        nextBtn.style.display = "block";
                    }
                }
                nextBtn.onclick = () => {
                    newIndex++; //increment index
                    if (newIndex >= galeria.length - 2) {
                        preview();
                        nextBtn.style.display = "none";
                    } else {
                        preview();
                        prevBtn.style.display = "block";
                    }
                }
                vistaCaja.classList.add("show");
                






                preview()
                vistaCaja.classList.add("show");

                closeIcon.onclick = ()=>{
                    vistaCaja.classList.remove("show");
                }

            }

        }
    
    }
        