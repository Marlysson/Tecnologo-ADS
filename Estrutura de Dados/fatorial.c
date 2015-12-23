#include <stdlib.h>
#include <stdio.h>

main(){
	int num, fatorial = 1;
	
	printf("Digite um número: ");
	scanf("%d",&num);
	
	while (num > 0){
		fatorial *= num;
		num--;
	}
	
	printf("Fatorial de %d é: %d",num,fatorial);
	
}