package br.edu.ifpi.formas.modelo;

public class Retangulo implements AreaCalculavel {
	
	private int base;
	private int altura;
	
	public Retangulo(int base, int altura){
		this.base = base;
		this.altura = altura;
	}
	
	public double calculaArea(){
		return this.base * this.altura;
	}
	
	public String toString(){
		return "Área do Retangulo "+this.calculaArea();
	}
}
