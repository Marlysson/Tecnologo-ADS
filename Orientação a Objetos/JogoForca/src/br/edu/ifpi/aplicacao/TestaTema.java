package br.edu.ifpi.aplicacao;
import br.edu.ifpi.modelo.*;
public class TestaTema {

	public static void main(String[] args) {
		
		Tema animais = new Tema("Animais");
		animais.addPalavra("Cachorro");
		animais.addPalavra("Gato");
		animais.addPalavra("Coelho");
		
		Tema cidades = new Tema("Cidades");
		cidades.addPalavra("Teresina");
		cidades.addPalavra("São Paulo");
		cidades.addPalavra("Rio de Janeiro");

		Tema times = new Tema("Times de Futebol");
		times.addPalavra("São Paulo");
		times.addPalavra("Flamengo");
		times.addPalavra("vasCo");
		
		System.out.println(animais.getPalavras());
		System.out.println(animais.getPalavraAleatorio());
		
		System.out.println(cidades.getPalavras());
		System.out.println(cidades.getPalavraAleatorio());
		
		System.out.println(times.getPalavras());
		System.out.println(times.getPalavraAleatorio());
		
	}

}
