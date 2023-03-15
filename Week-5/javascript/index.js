let age = 0
msg = ""
function add_number(num1,num2)
{
    return num1 + num2
}
console.log("Javascript console.testing")
document.getElementById("confirm-btn").onclick=function check_age(){
    age = document.getElementById("age ").value
    if(age<=18){
       msg = "you are not allowed"
       console.log("you are not allowed")
      document.getElementById("get in").innerHTML=msg
} else{
    msg = "welcome to the club"
    console.log("welcome to the club")
    
    document.getElementById("get_in").innerHTML.msg
 }

}
