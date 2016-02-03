package br.edu.ifpi.modelo;

import java.util.Set;
import br.edu.ifpi.modelo.*;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Random;

public class Rodada {

	private static final String EM_ANDAMENTO = "Andamento";
	private static final String PERDEU = "Perdeu";
	private static final String GANHOU = "Ganhou";
	
	private Tema temaEscolhido;
	private String palavraEscolhida;	
	private Jogador player;
	private int pontosJogador;
	private int pontuacao;
	private static String status;
	
	private static Set<Character> letrasPalavra = new HashSet<Character>();	
	private static Set<Character> letrasCorretas = new HashSet<Character>();
	private static Set<Character> letrasTentadas = new HashSet<Character>();
	private static Set<Character> letrasErradas = new HashSet<Character>();
	
	public Rodada(Jogador player){
		this.player = player;
		this.temaEscolhido = getTemaAleatorio();
		this.palavraEscolhida = temaEscolhido.getPalavraAleatorio();
		
		for(int i = 0; i < palavraEscolhida.length();i++){
			letrasPalavra.add(palavraEscolhida.charAt(i));
		}
	}
	
	public String getStatus(){
		return status;
	}
	
	public int getPontuacao(){
		return pontuacao;
	}
	
	public Jogador getJogador(){
		return player;
	}
	
	public String getTema(){
		return temaEscolhido.getNome();
	}
	
	public Set<Character> getLetrasErradas(){
		return letrasErradas;
	}

	
	private Tema getTemaAleatorio(){
		
		Random random = new Random();
		
		JogoForca jogo = JogoForca.getInstancia();
		
		int posicao = random.nextInt(jogo.getTemasAll().size());
	
		temaEscolhido =	jogo.getTemasAll().get(posicao);
		
		return temaEscolhido;
		
	}

	public static void verificaEstadoRodada(){
		
		String str = "";
		
		if (letrasErradas.size() == 6){
			status = Rodada.PERDEU;
		}else if (letrasPalavra.containsAll(letrasCorretas)){
			status = Rodada.GANHOU;
		}else{
			status = Rodada.EM_ANDAMENTO;
		}
		
	}
	
	public boolean testaLetra(Character letra){
			
		Character l = letra.toUpperCase(letra);
		
		letrasTentadas.add(l);
			
		if (letrasPalavra.contains(l)){
			letrasCorretas.add(l);
			pontuacao += 100;
			return true;
		}else{
			letrasErradas.add(l);
			return false;
		}
		
	}
	
	public String mostraPalavra(){
		String str = "";
			
		for(int i = 0; i < palavraEscolhida.length(); i ++){
			Character letra =  palavraEscolhida.charAt(i);
			
			if (letrasCorretas.contains(letra)){
				str += letra+" ";
			}else{
				str += "___ ";
			}
			
		}
		
		return str;
	}
	
	
	
	public String toString(){
		String str = "";
		
		str += String.format("Tema da rodada: %s",temaEscolhido)+"\n";
		str += String.format("Palavra escolhida %s",palavraEscolhida)+"\n";
		str += String.format("Letras palavra %s",letrasPalavra)+"\n \n";
		
		str += String.format("Letras corretas %s",letrasCorretas)+"\n";
		str += String.format("Letras tentadas %s",letrasTentadas)+"\n";
		str += String.format("Letras erradas %s",letrasErradas)+"\n";
		
		return str;
	}

}
