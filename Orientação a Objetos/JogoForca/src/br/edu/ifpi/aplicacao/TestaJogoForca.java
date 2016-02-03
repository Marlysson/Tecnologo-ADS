package br.edu.ifpi.aplicacao;
import br.edu.ifpi.modelo.*;
import java.util.Scanner;

public class TestaJogoForca {
	
	public static void main(String[] args) {
		
		JogoForca jogo = JogoForca.getInstancia();
		
		Tema animais = new Tema("Animal");
		Tema cidades = new Tema("Cidade");
		Tema times = new Tema("Times");
		
		jogo.addPalavra(animais,"Macaco");
		jogo.addPalavra(times,"Fluminense");
		jogo.addPalavra(cidades,"Teresina");
		jogo.addPalavra(times,"River");
		jogo.addPalavra(animais,"Leao");
		jogo.addPalavra(animais,"Tigre");
		jogo.addPalavra(cidades,"Fortaleza");
		jogo.addPalavra(cidades,"Altos");
		jogo.addPalavra(times,"Manchester");
		
		Jogador jogador = new Jogador("Marlysson",19);
		
		Rodada rodada = jogo.novaRodada(jogador);
		
		System.out.println("Dica: "+rodada.getTema()+"\n");
			
		while(true){			
			
			System.out.println("Digite uma letra: ");
			Scanner entrada = new Scanner(System.in);
			
			System.out.println(rodada.mostraPalavra());
			
			char letra = entrada.next().charAt(0);
			
			if(rodada.testaLetra(letra)){
				System.out.println("Letra correta");
				//rodada.verificaEstadoRodada();
			}else{
				System.out.println("Letra errada.");
				System.out.println("Quantidade letras erradas "+rodada.getLetrasErradas().size());
			}
			

			if ( rodada.getStatus() == "TERMINOU"){
				System.out.println("Você perdeu.");
				break;
			}else if (rodada.getStatus() == "GANHOU"){
				System.out.println("Parabéns, você ganhou");
				System.out.println("Pontuação: "+rodada.getPontuacao());
				break;
			}
		}
		
		
	}
}
