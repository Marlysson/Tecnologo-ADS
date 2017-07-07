
btn_show = document.querySelector(".btn-result");
resultados = document.querySelector(".results");

btn_show.addEventListener("click",function(event){
	resultados.classList.toggle("activate-results");
})