import java.util.Scanner;

class Exercicio8{
	public static void main(String[] args) {
		
		Scanner entradas = new Scanner(System.in);
		int soma = 0,cont = 0;

		while(true){
			int numero = entradas.nextInt();

			if (numero >= 0){
				soma += numero;
				cont += 1;
			}else{
				break;
			}

		}

		System.out.println(String.format("Média dos valores %.2f",soma / (float)cont));

	}
} 