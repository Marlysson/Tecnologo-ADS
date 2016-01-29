package br.edu.ifpi.aluguel.modelo;

public class Item {

	private String nome;
	private double valor;
	
	public Item(String nome , double valor){
		this.valor = valor;
		this.nome = nome;
	}
	
	public String getNome(){
		return this.nome;
	}
	public double getValor(){
		return this.valor;
	}
	
	public String toString(){
		return "Item: "+this.nome+"\nValor: R$ "+this.valor;
	}
}
