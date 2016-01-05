import java.util.Scanner;

class Exercicio6 {

	public static void main(String[] args) {
		Scanner entradas = new Scanner(System.in);

		System.out.print("Quantidade de bichos: ");
		int quantidade = entradas.nextInt();

		entradas.nextLine(); // Esvazia o buffer do teclado

		int all_cobaias = 0, ratos = 0, coelhos = 0, sapos = 0;

		for(int i = 0;i < quantidade; i++){

			String bicho = entradas.nextLine();
			String[] dados = bicho.split(" ");

			all_cobaias += Integer.parseInt(dados[0]);
			int quant_bicho = Integer.parseInt(dados[0]);

			switch (dados[1].toUpperCase()){
				case "S":
					sapos += quant_bicho;
					break;
				case "C":
					coelhos += quant_bicho;
					break;
				case "R":
					ratos += quant_bicho;
					break;
			}
		}

		System.out.println(String.format("Total de cobaias: %d",all_cobaias));
		System.out.println(String.format("Total de Coelhos: %d",coelhos));
		System.out.println(String.format("Total de Ratos: %d",ratos));
		System.out.println(String.format("Total de Sapos: %d",sapos));
		System.out.println(String.format("Porcentagem de Coelhos : %.2f",porcentagem(all_cobaias,coelhos))+"%");
		System.out.println(String.format("Porcentagem de Ratos : %.2f",porcentagem(all_cobaias,ratos))+"%");
		System.out.println(String.format("Porcentagem de Sapos : %.2f",porcentagem(all_cobaias,sapos))+"%");

	}

	public static float porcentagem( int total, int parte){
		return (parte / (float)total ) * 100;
	}
}