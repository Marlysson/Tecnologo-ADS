#include <stdlib.h>
#include <stdio.h>

/*
	Sequencia de Fibonacci: 1,1,2,3,5,8,13,21,34,55,89...
	
	Se o numero for igual a 0 ou 1
		return 1
	senão
		return fibonacci(numero_atual-1) + fibonacci(numero_atual-2)
*/


//Complexidade: 2^n
int fibonacci(int posicao){
		
	if ( (posicao == 0) | (posicao == 1) ){
		return 1;
	}else{
		return fibonacci(posicao-1) + fibonacci(posicao-2);
	}
}


//Complexidade: "n". Pois precisará fazer "n" interações para retornar o valor correto.
void fibonacci_mostrar(int num_elementos){
	int serie[num_elementos], i;
	
	for(i = 0;i <= num_elementos; i++){
		if(( i == 0)  | (i == 1) ){
			serie[i] = 1;
		}else{
			serie[i] = serie[i-1] + serie[i-2];
		}
	}
	
	for(i = 0;i <= num_elementos; i++){
		printf("%d ",serie[i]);
	}
}


main(){
	int posicao , quantidade , opcao, continuar = 1;
	
	
	do{
		printf("OPERACAO SERIE FIBONACCI: \n");
		printf("1 - Mostrar elementos \n");
	   	printf("2 - Mostrar elemento de uma posicao: \n");
	   	printf("3 - Sair \n \n");
	   	scanf("%d",&opcao);
	   	
	   	switch(opcao){
			case 1:
				printf("Quantidade de elementos da serie: ");
				scanf("%d",&quantidade);

				printf("Serie fibonacci \n");				
				fibonacci_mostrar(quantidade-1);
				
				printf("\n");
				printf("Continuar? 1-Sim/ 2-Nao ");
				scanf("%d",&continuar);  
				
				if (continuar == 1){
					system("cls");
				}
				
				break;
				
			case 2:
				printf("Posicao: ");
			   	scanf("%d",&posicao);
		   
	   	    	int serie_fibo = fibonacci(posicao-1);

			   	printf("Numero fibonacci na posicao %d : %d\n",posicao,serie_fibo);
                
				printf("Continuar? 1-Sim/ 2-Nao ");
				scanf("%d",&continuar);  
				
				if (continuar == 1){
					system("cls");
				}
				
				break;
        }		
	}while(continuar == 1);
}

