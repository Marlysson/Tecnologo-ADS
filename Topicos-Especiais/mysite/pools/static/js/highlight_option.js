
var option_radio = document.querySelectorAll(".option_item");

function limpar_highlight(){
	ativa = document.querySelector(".option_active");
	
	if (ativa != null){
		ativa.classList.remove('option_active')
	}
}

option_radio.forEach(function(value,index){

	value.addEventListener("click",function(event){

		limpar_highlight();

		parent = this.parentNode;
		parent.classList.add("option_active");
	});

	
	
});