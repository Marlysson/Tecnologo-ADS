package br.edu.ifpi.aluguel.modelo;

public class Cliente {

	private String nome;
	private String telefone;
	
	public Cliente(String nome, String telefone){
		this.nome = nome;
		this.telefone = telefone;
	}
	
	public String getNome(){
		return this.nome;
	}
	
	public String getTelefone(){
		return this.telefone;
	}
	
	public String toString(){
		return "Nome: "+this.nome+"\nTelefone: "+this.telefone;
	}
}
