#include <stdio.h>
#include <stdlib.h>

typedef struct livro{
	int cod;
	char nome_livro[30];
	char nome_autor[30];
	int num_pag;
}Livro;

Livro livro[5];
int indice = 0;

incluir(){
	int continuar = 1;
	
	while(continuar == 1){
		printf("Código do livro:");
		scanf("%d",&livro[indice].cod);
		fflush(stdin);
				
		printf("Nome do livro:");
		gets(livro[indice].nome_livro);

		
		printf("Nome autor: ");
		gets(livro[indice].nome_autor);
		
		printf("Número de páginas: ");
		scanf("%d",&livro[indice].num_pag);
		
		indice++;
		
		
		if (indice == 5){
			printf("Vetor cheio");
		}else{
			printf("\nDeseja inserir mais um? (1-sim / 2-não)");		
			scanf("%d",&continuar);
			
			system("cls"); //limpar tela			
		}
	}
}

mostrar(){
	
	system("cls");
	
	int i;
	
	for(i = 0;i < indice;i++){
		printf("Código do livro: %d\n",livro[i].cod);
	   	printf("Nome do livro: %s\n",livro[i].nome_livro);
		printf("Autor do livro: %s\n",livro[i].nome_autor);
		printf("Número de páginas: %d\ \n \n",livro[i].num_pag);
	}
}
main(){
	incluir();	
	mostrar();
}