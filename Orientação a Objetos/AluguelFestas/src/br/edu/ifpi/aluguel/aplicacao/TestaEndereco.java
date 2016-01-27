package br.edu.ifpi.aluguel.aplicacao;

import br.edu.ifpi.aluguel.modelo.Endereco;

public class TestaEndereco {

	public static void main( String[] args){
		
		Endereco end = new Endereco("Av. Frei Serafim",1232,"Centro");
		
		System.out.println(end.getNomeDaRua());
		System.out.println(end.getNumeroCasa());
		System.out.println(end.getBairro());
		
		System.out.println(end);
	}
	
}
