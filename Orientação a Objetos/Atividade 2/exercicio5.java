import java.util.Scanner;

class Exercicio5 {
	public static void main(String[] args) {
		
		String senha = getSenha();
		int cont = 0;

		while( true ){
			if ( verifyPassword(senha) ){
				System.out.print("Acesso permitido.");
				break;
			}else {

				cont += 1;

				if (cont == 3){
					System.out.print("Acesso Negado.");
					break;	
				}else{
					System.out.println("Senha invalida.");
					senha = getSenha();
				}
			}
		}
	}

	public static String getSenha(){
		Scanner entrada = new Scanner(System.in);

		System.out.print("Digite a senha > ");
		String senha = entrada.nextLine();

		return senha;
	}

	public static boolean verifyPassword(String senha){
		String password = "2002";

		if(senha.equals(password)){
			return true;
		}else{
			return false;
		}
	}
}