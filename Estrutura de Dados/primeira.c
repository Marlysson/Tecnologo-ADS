#include <stdio.h>
#include <stdlib.h>

/*
	Pegar entradas do usuário até um número negativo;
	Informar o maior valor digitado
*/ 

void main(){
	
	int numero;
	int maior = 0;
	
	while( numero >= 0){

	   	printf("Digite um numero:");
	   	scanf("%d",&numero);
	   	
 	    if ( numero >= maior){
			maior = numero;
        }		
	}
		
	printf("Maior numero %d",maior);

}