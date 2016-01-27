package br.edu.ifpi.aluguel.aplicacao;

import br.edu.ifpi.aluguel.modelo.Aluguel;
import br.edu.ifpi.aluguel.modelo.Cliente;
import br.edu.ifpi.aluguel.modelo.Endereco;
import br.edu.ifpi.aluguel.modelo.Festa;
import br.edu.ifpi.aluguel.modelo.Tema;

public class TestaAluguel {
	
	public static void main( String[] args){
		
		Cliente cliente = new Cliente("Marlysson","1234-1111");
		
		Endereco endereco = new Endereco("Rua Tal",21,"Bairro");
		
		Festa festa = new Festa(cliente,endereco);
		
		Tema tema = new Tema("Super Herói","Azul");
		
		tema.AdicionarItem("Doces",100);
		tema.AdicionarItem("Boneca",120);
		tema.AdicionarItem("Bruxa",50);
		tema.AdicionarItem("Balão",30);
		
		Aluguel aluguel = new Aluguel(festa,tema,2500);
		aluguel.setDataFesta("26/01/2016");
		aluguel.setHoraInicio("19:00");
		aluguel.setHoraFinal("24:00");
		
		
		System.out.println(aluguel);
		
	}
}
