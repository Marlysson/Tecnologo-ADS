package br.edu.ifpi.formas.modelo;

public class Circulo implements AreaCalculavel {

	private double raio;
	
	public Circulo(double raio){
		this.raio = raio;
	}
	
	public double calculaArea() {
		return Math.PI * this.raio * this.raio; 
	}
	
	public String toString(){
		return "Área do Circulo "+this.calculaArea();
	}

}
