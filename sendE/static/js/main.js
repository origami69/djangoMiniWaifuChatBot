let global = ""
document.querySelector("form").addEventListener("submit", async (e)=>{
e.preventDefault()
let getText = document.querySelector(".mess").value
let getR = ''
let formS= new FormData()
formS.append('mess', getText)
const response = await fetch('mess/', {
    method: 'POST',
    body: formS
  })
getR = await response.json()

  const human = document.createElement("div")
  human.className ="holdHuman"
 const para = document.createElement("p");
 para.className = "holdText"
 let bro = (global + ": " + getText)
const node = document.createTextNode(bro);
para.appendChild(node);
human.appendChild(para)

 const robot = document.createElement("div")
 robot.className ="holdRobot"
 const rTex = document.createElement("p");
 rTex.className = "holdR"
 let robotM= ("WaChan: " + getR.rMessage)
const rNode = document.createTextNode(robotM);
rTex.appendChild(rNode);
robot.appendChild(rTex)

document.querySelector(".messageShow").appendChild(human)
document.querySelector(".messageShow").appendChild(robot)

document.querySelector(".mess").value=""
})
async function come(){
const response = await fetch('getUse/', {
    method: 'GET'
  })
getR = await response.json()
global=getR.get
document.querySelector(".greet").innerText = ("Hello " + getR.get + ", I am WaChan");
}
come()
document.querySelector(".logOut").addEventListener("dblclick", async (j)=>{
const response = await fetch('logOut/', {
    method: 'POST'
  }).then(response=> location.reload())
})
