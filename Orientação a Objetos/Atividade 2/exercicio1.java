import java.util.Scanner;

class Exercicio1 {
	public static void main(String[] args) {

		Scanner entradas = new Scanner(System.in);

		System.out.println("Distancia percorrida: ");
		int distancia = entradas.nextInt();
		
		System.out.println("Combustivel gasto: ");
		float combustivel = entradas.nextFloat();

		float consumo = distancia / combustivel;

		System.out.println(String.format("Consumo medio: %.3f km/l",consumo));
	}
	
}