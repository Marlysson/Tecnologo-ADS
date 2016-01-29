#include <stdlib.h>
#include <stdio.h>
#include <math.h>

/*
	Complexidade: LogN base 2
	Pois precisará fazer a quantidade de interações com base no valor do expoente
	da base que foi passada, assim precisará descobrir o expoente com base no resultado.
	
	2^n = 15
	2^logNbase2 < ( 15 < (2^4) )
	logNbase2 <= 15
	2^n <= 15
	
	2^n <= 2^3 (Valor ainda menor que o valor procurado (15))
	2^4 > 2^4 (Valor acima do procurado (15), assim usa-se o valor anterior menor).
	
	n = 3
	
*/


int calcula_lg(int n){
	int i = 1, piso;

	while (pow(2,i) <= n){	
       i += 1;		   	   
	   
	   if (pow(2,i) > n){
		   piso = i-1;
       }
	}
	
	return piso;
}

main(){
	int n;
	
	printf("Digite um valor: ");
	scanf("%d",&n);
	
	int resultado = calcula_lg(n);
	
	printf("lg de %d e : %d",n,resultado);
}