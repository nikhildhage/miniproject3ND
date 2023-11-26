const modal=document.getElementsByClassName("loginModal");
const loginModal= new bootstrap.Modal("#loginModal");
const closeModalBtn=document.getElementById("modalBtn");

const showModal=function(){
     console.log("add modal css class")
     console.log("Showing Modal")
     loginModal.className="modal";
     loginModal.show()

}

window.onload=showModal;
closeModalBtn.addEventListener("click", (e)=>{
     console.log("Hide login Modal");
     $('#modalDialog').hide()
})









