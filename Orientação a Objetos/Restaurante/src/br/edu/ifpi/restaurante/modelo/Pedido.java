package br.edu.ifpi.restaurante.modelo;

public class Pedido {
	private String item;
	private double valor;
	
	
	public Pedido(String item,double valor){
		this.item = item;
		this.valor = valor;
	}
	
	public Pedido(){
		
	}
	
	public double getValor(){
		return valor;
	}
	
	public String getItem(){
		return item;
	}
	
	public String toString(){
		return "Item: "+item+"\n"+" Preço: "+valor;
	}
}
