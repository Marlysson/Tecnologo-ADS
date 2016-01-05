#include <stdio.h>
#include <stdlib.h>

char nome[20], caracter[1];

char conta_caracter(char nome[], char letra[10]){
	//int cont = 0;
	return (letra);
	//if ( ++nome[0] == '/0'){
	//	return cont;
	//}else{
	//	printf(++nome);
		//l = nome[0];
	    //if(conta_caracter(l,letra)){
		//    cont++;			
		//}
	//	return cont;

	//}
}

main(){
	
	printf("Digite um nome: ");
	fgets(nome,10,stdin);
	fflush(stdin);
	
	printf("Caracter procurado: ");
	scanf("%s",caracter);

	printf("%s",conta_caracter(nome,caracter));

}