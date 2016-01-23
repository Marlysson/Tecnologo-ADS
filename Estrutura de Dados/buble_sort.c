#include <stdlib.h>
#include <stdio.h>

void bolha(int quant,int *v){
	int i,j;
	int troca;
	
	for(i=quant-1 ; i >= 1 ; i--){ //anterior: i = quant-1)
		troca = 0;
		
		for(j = 0; j < i; j++){
			if (v[j] > v[j+1]){
				int temp = v[j];
				v[j] = v[j+1];
				v[j + 1] = temp;
				
				troca = 1;				
			}
		}
		
		if(troca == 0){
			break;
		}
	}
}

void mostrar(int quant,int *v){
	int i;
	
	for(i = 0; i < quant; i++){
		printf("Valor: %d\n",v[i]);
	}
}
main(){
	int v[] = {9,7,3,1,3,9,3,5,1};

	bolha(9,v);
	mostrar(9,v);		
}