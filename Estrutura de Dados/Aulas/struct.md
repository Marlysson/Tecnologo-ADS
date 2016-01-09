## STRUCTS EM C

### Introdução 
Structs são estruturas com um conjunto de tipos definidas em seu escopo pelo programador.
Com isso virará uma estrutura parecida com ```int```, ```float```, ..

Fazendo uma comparação com python, é similar a um dicionário de tipos de dados.

```python
aluno = {
	'nome':'Marlysson',
	'matricula':123;
	'nota':9
}

>>> aluno['nome']
Marlysson
```

### Criação de uma scruct:

```c
struct aluno{
	int mat;
	float nota;
	char nome[30];
};

typedef struct aluno Aluno; 
// Definição do nome da struct
```

```c
typedef struct aluno{
	int matricula;
	float nota;
	char nome[30];
}Aluno;

//Criando e atribuindo o nome da struct.
```

### Uso de uma struct:
Para usar uma ```struct``` é preciso atribuir a uma variavel que será uma struct o tipo dela, que é o nome da ```struct``` que foi definido.

```c
Aluno aluno;

aluno.matricula = 123;
aluno.nota = 9.3;
aluno.nome = "Marlysson";

printf(aluno.nome);
//Marlysson
```

## Exemplo completo:
```c
#include <stdio.h>
#include <stdlib.h>

typedef struct aluno{
	int mat;
	float nota;
   	char nome[30];
}Aluno;

Aluno aluno;

main(){
	printf("Digite a matricula: ");
	scanf("%d",&aluno.mat);
	fflush(stdin);
	
	printf("Digite o nome: ");
	gets(aluno.nome);
	
	printf("Digite a nota: ");
	scanf("%f",&aluno.nota);
	
	printf("Nome: %s\n",aluno.nome);
	printf("Matricula: %d\n",aluno.mat);
	printf("Nota : %.1f",aluno.nota);
}
```
Mas uma struct geralmente é utilizada para vários tipos de estruturas inseridas dentro dela, assim, é usado um vetor do tipo da struct criada, onde cada posição do vetor é uma struct ( estrutura com um conjunto de tipos).

```c
#include <stdio.h>
#include <stdlib.h>

typedef struct aluno{
	int mat;
	float nota;
   	char nome[30];
}Aluno;

Aluno aluno[2];

int main(){
	int i;
	for (i = 0;i < 2;i++){
		printf("Digite a matricula: ");
		scanf("%d",&aluno[i].mat);
		fflush(stdin);
		
		printf("Digite o nome: ");
		gets(aluno[i].nome);
		
		printf("Digite a nota: ");
		scanf("%f",&aluno[i].nota);
	}
	
	for(i= 0; i < 2; i++){
		printf("Aluno[%d]\n",i);
		printf(" Nome[%d]: %s\n",i,aluno[i].nome);
		printf(" Matricula[%d]: %d\n",i,aluno[i].mat);
		printf(" Nota[%d] : %.1f\n\n",i,aluno[i].nota);
	}
}
```