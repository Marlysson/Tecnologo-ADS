#include <stdlib.h>
#include <stdio.h>

int divisoes;

int busca_bin(int n,int *vet, int elem){
	int init=0, fim = n-1;
	
	while (init <= fim){
		int meio = (init + fim) / 2;
		
		if (elem < vet[meio]){
			fim = meio - 1;
		}else if (elem > vet[meio]){
			init = meio + 1;
		}else{
			return meio;
		}
	}
	
	return -1;
}

void mostrar(int quant,int *v){
	int i;
	
	for(i = 0; i < quant; i++){
		printf("Valor: %d\n",v[i]);
	}
}

void main(){

	int v[] = {1,2,3,4,5,6,7,8,9};

	int posicao = busca_bin(9,v,2);
	
	if (posicao != -1){
		printf("O elemento esta na posicao: %d",posicao);
		printf("Quantidade de divisoes :%d",divisoes);		
	}else{
		printf("Elemento nao encontrado.");
	}
		
}