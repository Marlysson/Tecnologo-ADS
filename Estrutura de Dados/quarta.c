#include <stdio.h>
#include <stdlib.h>

/*
	Mostrar a soma e a média dos números divisíveis por 3
	entre 50 e 80.
*/

main(){
	int soma = 0, i , quantidade = 0;
	
	for ( i = 30; i < 51; i++){
		if (i % 3 == 0){
			soma += i;
		 	quantidade += 1;		
		}
	}
	
	printf("Soma divisiveis por 3: %d\n",soma);
	printf("Quantidade: %d\n",quantidade);
	printf("Media aritmetica divisiveis por 3: %d\n",(soma / quantidade ));
	
}