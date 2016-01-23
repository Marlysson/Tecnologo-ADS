package br.edu.ifpi.formas.aplicacao;

import br.edu.ifpi.formas.modelo.AreaCalculavel;
import br.edu.ifpi.formas.modelo.Circulo;
import br.edu.ifpi.formas.modelo.Quadrado;
import br.edu.ifpi.formas.modelo.Retangulo;

public class TestaFormas {
	
	public static void main(String args[]){
		
		AreaCalculavel square = new Quadrado(2);
		AreaCalculavel rect = new Retangulo(2,3);
		AreaCalculavel circle = new Circulo(3);
		
		System.out.println(square);
		System.out.println(rect);	
		System.out.println(circle);
	}
	
}
