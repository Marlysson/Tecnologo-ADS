
var option_itens = document.querySelectorAll(".option_item");

function limpar_highlight(){
	ativa = document.querySelector(".option_active");
	
	if (ativa != null){
		ativa.classList.remove('option_active')
	}
}

option_itens.forEach(function(value,index){

	value.addEventListener("click",function(event){

		input = value.querySelector("input");
		type_input = input.getAttribute("type");

		if (type_input != "checkbox"){
			limpar_highlight();

			parent = this.parentNode;
			parent.classList.add("option_active");

		}else{

			parent = this.parentNode;
			parent.classList.add("option_active");

		}


	});

	
	
});