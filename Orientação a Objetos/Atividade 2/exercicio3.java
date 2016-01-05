import java.util.Scanner;

class Exercicio3 {
	public static void main(String[] args){
		Scanner entrada = new Scanner(System.in);

		System.out.println("Digite os numeros: ");
		String numeros = entrada.nextLine();
		String n[] = numeros.split(" ");

		int n1 = Integer.parseInt(n[0]);
		int n2 = Integer.parseInt(n[1]);
		int n3 = Integer.parseInt(n[2]);
		int n4 = Integer.parseInt(n[3]);

		if ( 
			(n2 > n3) && (n4 > n2) && 
			( (n3 + n4) > (n1 + n2) ) &&
			(n3 > 0 && n4 > 0) &&
			(n1 % 2 == 0 ) 
		){
			System.out.println("Valores aceitos.");
		}else{
			System.out.println("Valores nao aceitos.");
		}
		
	}
}