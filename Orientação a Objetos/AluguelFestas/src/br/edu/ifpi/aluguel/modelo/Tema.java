package br.edu.ifpi.aluguel.modelo;

import br.edu.ifpi.aluguel.modelo.Item;

public class Tema {
	
	private String nomeTema;
	private Item[] itens;
	private String corToalha;
	private int contItens;
	
	public Tema(String nome,String corDaToalha){
		this.nomeTema = nome;
		this.corToalha = corDaToalha;
		
		this.itens = new Item[5];
		
	}
	
	public void AdicionarItem(String nome,int valor){
		if (this.contItens == 5){
			System.out.println("Quantidade máxima de itens atingido.");
		}else{
			this.itens[contItens++] = new Item(nome,valor);
		}
		
	}
	
	public Item[] getItens(){
		
		/*int contItens = 1;
		Item[] itensValidos = new Item[contItens];
		
		int i = 0;
		while(true){
			if (itens[i] != null){
				itensValidos[i] = itens[i];
			}
			
			if (itens[i] == null){
				break;
			}
			
			i += 1;
		}
		
		return itensValidos;
	}*/
	return this.itens;

	}
	
	public double getValor(){
		double valorTotal = 0;
		
		for(Item item : itens){
			if (item != null){
				valorTotal += item.getValor();	
			}
		}
		
		return valorTotal;
	}
	
	
	public String toString(){
		
		String str = "";
		
		str += "Cor da Toalha: "+this.corToalha+"\n";
		str += "Itens: \n";
		
		for(int i = 0; i < itens.length; i++){
			if (itens[i] != null){
				str += "- "+itens[i].getNome()+" - "+"R$ "+itens[i].getValor()+"\n";
			}
		}
		 
		return str;
	}
	
	
}