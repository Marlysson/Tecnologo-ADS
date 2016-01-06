#include <stdio.h>
#include <stdlib.h>

int conta(char string[],char caracter){
	if(string[0] == "\0"){
		return 0;
	}
	if(string[0] == caracter){
		return (1 + conta(caracter,++string));
	}
	return conta(caracter,++string);
}


main(){
	char s[30],caracter;
	int cont;
	
	printf("Digite a palavra: ");
	gets(s);
	fflush(stdin);
	
	printf("Digite o caracter:");
	scanf(&caracter);
	
	cont = conta(s,caracter);
	
	printf("Encontrados %d letras",cont);
	
}