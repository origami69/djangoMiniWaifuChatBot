document.querySelector(".switcherL").addEventListener("click", (e)=>{
document.querySelector(".createAccount").style.display = "flex"
document.querySelector(".signIn").style.display = "none"
})
document.querySelector(".switcherC").addEventListener("click", (j)=>{
document.querySelector(".createAccount").style.display = "none"
document.querySelector(".signIn").style.display = "flex"
})
 function pass(e){
        const regex=/^[a-zA-Z0-9]*$/
        if(regex.test(e.target.value) && e.target.value.length>=3){
            e.target.style.border='1px solid green'
            e.target.style.outlineColor='green'
        }else{
            e.target.style.border='1px solid red'
            e.target.style.outlineColor='red'
        }
    }
    function check(e){
        const regex=/^[a-zA-Z0-9]*$/
        if(regex.test(e.target.value) && e.target.value.length>=8 && /(?=.*[A-Za-z])(?=.*[0-9])[A-Za-z0-9]+/.test(e.target.value)){
            e.target.style.border='1px solid green'
            e.target.style.outlineColor='green'
        }else{
            e.target.style.border='1px solid red'
            e.target.style.outlineColor='red'
        }
    }