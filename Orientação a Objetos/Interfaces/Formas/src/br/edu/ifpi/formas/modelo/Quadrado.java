package br.edu.ifpi.formas.modelo;

public class Quadrado implements AreaCalculavel{
	
	private int lado;
	
	public Quadrado(int lado){
		this.lado = lado;
	}
	
	public double calculaArea(){
		return this.lado * this.lado;
	}
	
	public String toString(){
		return "Área do Quadrado "+this.calculaArea();
	}
}
