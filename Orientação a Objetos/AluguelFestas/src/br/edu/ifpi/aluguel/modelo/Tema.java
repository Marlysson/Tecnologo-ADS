package br.edu.ifpi.aluguel.modelo;

import java.util.ArrayList;
import br.edu.ifpi.aluguel.modelo.Item;

public class Tema {
	
	private String nomeTema;
	private ArrayList<Item> itens = new ArrayList<Item>();
	private String corToalha;
	
	public Tema(String nome){
		this.nomeTema = nome;
	}
	
	public void setCorToalha(String cor){
		this.corToalha = cor;
	}
	
	public String getNome(){
		return this.nomeTema;
	}
	
	public void AdicionarItem(String nome,double valor){
		this.itens.add(new Item(nome,valor));
	}
	
	public ArrayList<Item> getItens(){
		return this.itens;
	}
	
	public double getValor(){
		double valorTotal = 0;
		
		for(Item item : itens){
			valorTotal += item.getValor();	
		}
		
		return valorTotal;
	}
		
	public String toString(){
		
		String str = "";
		
		str += "Cor da Toalha: "+this.corToalha+"\n";
		str += "Itens: "+this.itens.size()+"\n";
		
		for( Item item : itens){
				str += "- "+item.getNome()+" - "+String.format("R$ %.2f",item.getValor())+"\n";
		}
		 
		return str;
	}
	
	
}