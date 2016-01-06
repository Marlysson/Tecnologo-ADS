import java.util.Scanner;

class Exercicio10{

	public static void main(String[] args) {
		int alcool=0,gasolina=0,diesel=0;

		Scanner entradas = new Scanner(System.in);

		System.out.print("Codigo do combustivel: ");
		int codigo = entradas.nextInt();

		while(true){
			if(validaEntrada(codigo)){
				switch (codigo){
					case 1:
						alcool += 1;
						break;
					case 2:
						gasolina += 1;
						break;
					case 3:
						diesel += 1;
						break;
					case 4:
						break;
					}
			}else{

				System.out.print("Codigo do combustivel: ");
				codigo = entradas.nextInt();

			}
		}

		System.out.println("Alcool :" + alcool);
		System.out.println("Gasolina :" + gasolina);
		System.out.println("Diesel :" + diesel);
	}

	public static boolean validaEntrada(int into){
		int valores[] = {1,2,3,4};

		for(int i=0;i < valores.length;i++){
			if(into == valores[i]){
				return true;
			}else{
				return false;
			}
		}
	}

}