import java.util.Scanner;

class Exercicio10{
	public static void main(String[] args) {
		int pares = 0;

		Scanner entradas = new Scanner(System.in);

		for(int i = 1;i < 6;i++){
			System.out.print("Digite o numero " + i + ": ");
			int num = entradas.nextInt();

			if (num % 2 == 0){
				pares += 1;
			}
		}

		System.out.println("Ha " + pares+ " numero pares.");

	}
}