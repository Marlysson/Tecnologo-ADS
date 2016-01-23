package br.edu.ifpi.conta.modelo;

public class GerenciadorDeImpostoDeRenda {
	public double total;
	
	public void adiciona(Tributavel conta){
		System.out.println("Adiconando tributavel "+ conta);
		
		this.total += conta.calculaTributos();
		
	}
	
	public double getTotal(){
		return this.total;
	}
}
