#include <stdio.h>
#include <stdlib.h>

typedef struct aluno{
	int matricula;
	char nome[30];
	int nota;	
	int idade;
}Aluno;

Aluno aluno[5];
int indice;
int	matricula;

void incluir_teste(){
	
	aluno[0].matricula = 1;
	strcpy(aluno[0].nome,"Marlysson");
	aluno[0].idade     = 19;
	aluno[0].nota      =  6;//[9,8,7,9];
	
	aluno[1].matricula = 2;
	strcpy(aluno[1].nome,"Marcelo");
	aluno[1].idade     = 18;
	aluno[1].nota      =  7;//[9,9,7,10];
	
	aluno[2].matricula = 3;
	strcpy(aluno[2].nome,"Maria");
	aluno[2].idade     = 20;
	aluno[2].nota      =  9;//[5,7,1,10];
	
	aluno[3].matricula = 4;
	strcpy(aluno[3].nome,"Marcos");
	aluno[3].idade     = 21;
	aluno[3].nota      =  6;//[9,5,7,10];
	
	aluno[4].matricula = 5;
	strcpy(aluno[4].nome,"João");
	aluno[4].idade     = 22;
	aluno[4].nota      =  9;//[5,7,8,10];
		
	indice = 4;
	
}
void incluir(){
	int continuar = 1;
	
	while(continuar == 1){
		printf("Matricula do aluno: ");
		scanf("%d",&aluno[indice].matricula);
		fflush(stdin);
		
		printf("Nome do aluno: ");
		fgets(aluno[indice].nome,30,stdin);
		
		printf("Idade do aluno: ");
		scanf("%d",&aluno[indice].idade);
		
		indice++;
		
		if (indice == 5){
			printf("Vetor cheio");
			break;
		}else{
			printf("\nDeseja inserir mais um? (1-sim / 2-não)");		
			scanf("%d",&continuar);
			
			system("cls"); //limpar tela		
		}
	}
}

void mostrar(){
	
	int i;
	
	if(indice == 0){
		printf("Vetor sem dados.");
	}else{
		for(i = 0;i < indice;i++){
			printf("Matricula do aluno: %d\n",aluno[i].matricula);
	   	   	printf("------------------------\n");
			printf("Nome do aluno:      %s\n",aluno[i].nome);
			printf("------------------------\n");
        	printf("Idade do aluno:     %d \n",aluno[i].idade);
       		printf("------------------------\n");
        	printf("Nota:               %d\n \n \n",aluno[i].nota);
		}
	}
}


int obtem_nota(char criterio[5]){
	int i, index;
	
	for(i = 0; i < indice; i ++){
		int maior = 0;
		
		if (criterio == "maior"){
    		if( aluno[i].nota >= maior){
    			
              maior = aluno[i].nota;
			  index = i;
			  
			}
        }else if(criterio == "menor"){
			int menor = aluno[0].nota;
					
			if( aluno[i].nota < menor){
				
				menor = aluno[i].nota;
				index = i;
				
			}
		}	
	}
	
	return index;
}

int buscar(int mat){
    int i,index;
    
	for(i = 0 ; i < indice ; i++){
		if( aluno[i].matricula == mat){
		    index = i;
			break;		
		}else{
			index = -1;
		}
	}
	
	return index;
}

void remover1(int posicao){
	aluno[posicao] = aluno[indice - 1];
	indice--;
}

void remover2(int posicao){
	int i;
	for(i = posicao; i < (indice - 1) ; i++){
		aluno[i] = aluno[i + 1];
	}
	
	indice--;
}


main(){	
   incluir_teste();
   mostrar();
/*  
   printf("Digite a matricula procurada: ");
   scanf("%d",&matricula);

   int posicao = buscar(matricula);
		
   system("cls");
   if(posicao != -1){
   	   printf("Item procurado:\n");
       printf("Matricula: %d\n",aluno[posicao].matricula); 
	   printf("Nome: %s\n",aluno[posicao].nome);
	   printf("Idade: %d",aluno[posicao].idade);
   }else{
   	   printf("Nenhum dado encontrado");
   }
*/
	int i;
	for(i = 0;i < 2;i++){
	int mat;
	printf("Digite a matricula a remover: ");
	scanf("%d",&mat);
		
	int pos_aluno = buscar(mat);
		
	remover2(pos_aluno);
	}
		
	int id_maior = obtem_nota("maior");
	
	printf("  ALUNO COM MAIOR NOTA\n");
	printf("------------------------\n");	
	printf("    Matricula:   %d   \n",aluno[id_maior].matricula);
	printf("------------------------\n");
	printf("    Nome:        %s\n",aluno[id_maior].nome);
	printf("------------------------\n");
	printf("    Idade:       %d\n",aluno[id_maior].idade);
	printf("------------------------\n");
	printf("    Nota:        %d\n",aluno[id_maior].nota);
}