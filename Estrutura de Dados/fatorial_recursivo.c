#include <stdio.h>
#include <stdlib.h>

long fatorial(long n){
	if( n == 0){
		return 1;
	}else{
		return n * fatorial(n - 1);
	}
}

main(){
    int numero;
	 
	printf("Digite um numero: ");
	scanf("%d",&numero);
	
	printf("%d",fatorial(numero));
}