package br.edu.ifpi.aluguel.aplicacao;

import br.edu.ifpi.aluguel.modelo.Item;
import br.edu.ifpi.aluguel.modelo.Tema;

public class TestaTema {
	
	public static void main(String[] args){
		
		Tema tema = new Tema("Tema de teste");
		tema.setCorToalha("Azul");
		
		tema.AdicionarItem("Doces",12);
		tema.AdicionarItem("Boneca",12);
		tema.AdicionarItem("Bruxa",12);
		tema.AdicionarItem("Balão",12);
		tema.AdicionarItem("Balão",12);
		
		System.out.println(tema);
		
		for(Item item : tema.getItens()){
			System.out.println(item.getNome()+" "+item.getValor());
		}
		

	}
}
