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

function check_pass() {
    if (document.getElementById('myInput').value ==
            document.getElementById('myInput2').value) {
        document.getElementById('submit').disabled = false;
    } else {
        document.getElementById('submit').disabled = true;
    myInput2.setCustomValidity("Password mismatch");
		document.getElementById("submit").click()
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
