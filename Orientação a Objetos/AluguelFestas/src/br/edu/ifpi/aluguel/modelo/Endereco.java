package br.edu.ifpi.aluguel.modelo;

public class Endereco {

	private String NomeDaRua;
	private int numero;
	private String bairro;
	
	public Endereco(String nome,int numero, String bairro){
		this.NomeDaRua = nome;
		this.numero = numero;
		this.bairro = bairro;
	}
	
	public String getNomeDaRua(){
		return this.NomeDaRua;
	}
	
	public int getNumeroCasa(){
		return this.numero;
	}
	
	public String getBairro(){
		return this.bairro;
	}
	
	public String toString(){
		return "Endereço: "+this.NomeDaRua+"\nNumero: "+this.numero+"\nBairro: "+this.bairro;
	}
}
