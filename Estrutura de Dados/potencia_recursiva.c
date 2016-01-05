#include <stdio.h>
#include <stdlib.h>

int potencia(base,expoente){
	if (expoente == 1){
		return base;	
	}else{
		return base * potencia(base, expoente - 1 );
	}
}
main(){
	int base,expoente;
	
	printf("Base: ");
	scanf("%d",&base);
	
    printf("Expoente: ");
	scanf("%d",&expoente);
	
	int resultado = potencia(base,expoente);
	
	printf("%d elevado a %d e : %d",base,expoente,resultado);
}

