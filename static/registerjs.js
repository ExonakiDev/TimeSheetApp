const inputs = document.querySelectorAll(".input");


function addcl(){
	let parent = this.parentNode.parentNode;
	parent.classList.add("focus");
}

function remcl(){
	let parent = this.parentNode.parentNode;
	if(this.value == ""){
		parent.classList.remove("focus");
	}
}


inputs.forEach(input => {
	input.addEventListener("focus", addcl);
	input.addEventListener("blur", remcl);
})

function myFunction() {
  var x = document.getElementById("myInput");
  var y =document.getElementById("myInput2");
  if ((x.type === "password")&&(y.type === "password")) {
    x.type = "text";
	y.type="text";
  } else {
    x.type = "password";
	y.type = "password";
  }
};