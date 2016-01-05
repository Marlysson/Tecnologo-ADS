import java.util.Scanner;

class Exercicio2 {
	public static void main(String[] args) {
		Scanner entradas = new Scanner(System.in);

		System.out.println("Nome do vendedor: ");
		String nome = entradas.nextLine();

		System.out.println("Salario do vendedor: ");
		double salario = entradas.nextDouble();

		System.out.println("Total de vendas: ");
		double vendas = entradas.nextDouble();

		double novo_salario = (vendas * 0.15) + salario;

		System.out.println(novo_salario);
	}
}