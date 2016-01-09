#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct aluno{
	int mat;
	float nota;
   	char nome[30];
}Aluno;

Aluno aluno[2];
int tam_vetor = 2;

maior_nota(){
	float maior_nota;
	
	

	
}
incluir(){
	int i;
	for(i = 0;i < tam_vetor;i++){
		printf("Aluno %d\n",i+1);
		printf("Digite a matricula: ");
		scanf("%d",&aluno[i].mat);
  	    fflush(stdin);
		
 	    printf("Digite o nome: ");
	 	fgets(aluno[i].nome,30,stdin);
		
		printf("Digite a nota: ");
		scanf("%f",&aluno[i].nota);
		
		system("cls");
	}	
}

void mostrar(){
	int i;
	for(i = 0; i < tam_vetor; i++){
		printf("\nAluno %d\n",i+1);
		printf("- Nome: %s",aluno[i].nome);
		printf("- Matricula : %d\n",aluno[i].mat);
		printf("- Nota : %.1f\n",aluno[i].nota);
	}
}

main(){
	int opc;
	printf("O que deseja fazer:");
	printf("\n1 - Inserir.\n2 - Mostrar\n");
	scanf("%d",&opc);
	
	system("cls");
	switch(opc){
		case 1:incluir();break;
		case 2:mostrar();break;
		default:"Opçao inválida.";
	}
	
};

