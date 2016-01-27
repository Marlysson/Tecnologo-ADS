package br.edu.ifpi.aluguel.aplicacao;

import br.edu.ifpi.aluguel.modelo.Cliente;

public class TestaCliente {

	public static void main( String[] args){
		
		Cliente c1 = new Cliente("Marlysson","1234-1234");
		Cliente c2 = new Cliente("Marcelo","123-1234");
		
		System.out.println(c1);
		System.out.println(c2);
		
		System.out.println(c1.getNome());
		
		System.out.println(c2.getTelefone());
		
	}
}
