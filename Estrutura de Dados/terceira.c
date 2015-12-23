#include <stdio.h>
#include <stdlib.h>

/*
	Ler 10 números e verificar quantos números da lista
	foram maiores que um dados número informado.
*/

int maiores(int numeros[],int num){
    int	i , cont = 0;
	 
    for(i = 0;i < 10;i++){
		if (numeros[i] > num){
			cont++;
		}
	}
	return cont;
}

main(){
	int i , numero , numeros[10] = {};
	
	for(i = 0;i < 10;i++){
		printf("Numero %d: ",i+1);
		scanf("%d",&numeros[i]);
	}

	printf("\nNumero para verificar: ");
	scanf("%d",&numero);
	
	printf("\nQuantidade de numeros maiores que %d: %d", numero , maiores(numeros,numero));		
}