package br.edu.ifpi.modelo;
import br.edu.ifpi.modelo.*;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class JogoForca {
	
	private static JogoForca instancia;
	private Rodada rodada;
	private static ArrayList<Tema> temas = new ArrayList<Tema>();
	
	
	public static JogoForca getInstancia(){
		
		if (instancia == null){
			instancia = new JogoForca();
		}
		
		return instancia;
		
	}
	
	public Rodada novaRodada(Jogador jogador){
		Rodada rodada = new Rodada(jogador);
		return rodada;
	}
	
	public void addPalavra(Tema tema,String palavra){
		
		if (!temas.contains(tema)){
			temas.add(tema);
		}		
		
		tema.addPalavra(palavra);
	}
	
	public ArrayList<Tema> getTemasAll(){
		return temas;
	}
	
	public String toString(){
		String str = "";
		
		for(Tema tema : temas){
			str += tema.getNome()+"\n";
			
			for(String palavra : tema.getPalavras()){
				str += palavra+"\n";
			}
			
			str += "\n";
		}
		
		return str;
	}
		
}
