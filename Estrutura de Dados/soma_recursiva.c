#include <stdio.h>
#include <stdlib.h>

int soma_recursiva(int n){
	if (n == 1){
		return 1;
	}else{
		return n + soma_recursiva(n - 1);
	}
}

main(){
    int	num;

	scanf("%d",&num);
	
	printf("%d",soma_recursiva(num));
}