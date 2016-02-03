package br.edu.ifpi.modelo;
import java.util.ArrayList;
import java.util.Random;

public class Tema{
	
	private ArrayList<String> palavras = new ArrayList<String>();
	private String nomeTema;
	
	public Tema(String nome){
		this.nomeTema = nome;
	}
	
	public void addPalavra(String palavra){
		palavras.add(palavra.toUpperCase());
	}
	
	public String getPalavraAleatorio(){
		Random random = new Random();
		int posicao = random.nextInt(palavras.size());
		
		return palavras.get(posicao);
	}
	
	public String getNome(){
		return nomeTema;
	}
	
	public ArrayList<String> getPalavras(){
		return palavras;
	}
	
	public String toString(){
		return nomeTema;
	}
}

