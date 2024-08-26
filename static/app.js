let tablerow = document.getElementsByTagName('tr')

let tabletd = document.querySelectorAll('tr td')
let notes = document.getElementById("notes")
tabletd.forEach((e , id)=>{        
    e.style.cursor = 'pointer'
    e.addEventListener("click" , ()=>{
        notes.style.display = 'flex'
    })
})