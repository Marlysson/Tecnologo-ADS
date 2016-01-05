import java.util.Scanner;

class Exercicio7 {
	public static void main(String[] args) {
		Scanner entradas = new Scanner(System.in);

		System.out.print("Quantidade de lesmas: ");
		int quant_lesmas = entradas.nextInt();

		entradas.nextLine(); // Esvaziar buffer

		System.out.println("Velocidades separadas por espaco: ");
		String valores = entradas.nextLine();
		String velocidades[] = valores.split(" ");

		int maior_velocidade = maior(velocidades);

		if (maior_velocidade < 10){
			System.out.print("Nivel 1");
		}else if (maior_velocidade < 20){
			System.out.print("Nivel 2");
		}else{
			System.out.print("Nivel 3");
		}
	}

	public static int maior(String valores[]){
		int maior = 0;

		for(String i : valores){
			int num = Integer.parseInt(i);

			if (num >= maior){
				maior = num;
			}
		}

		return maior;
	}
}