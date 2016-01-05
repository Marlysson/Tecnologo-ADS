import java.util.Scanner;

class Exercicio4 {
	public static void main(String[] args) {
		Scanner entrada = new Scanner(System.in);

		System.out.println("Digite um numero: ");
		int numero = entrada.nextInt();

		int atual = 1;
		while (atual <= numero*4){
			if ( atual % 4 == 0){
				System.out.print("IFPI"+'\n');
				atual += 1;
			}else{
				System.out.print(atual+" ");
				atual += 1;
			}
		}
	}
}