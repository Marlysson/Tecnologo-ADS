package br.edu.ifpi.aluguel.modelo;

public class Festa {

	private Endereco endereco;
	private Cliente contratante;
	
	public Festa(Cliente cliente, Endereco endereco){
		this.contratante = cliente;
		this.endereco = endereco;
	}
	
	public Cliente getContratante(){
		return this.contratante;
	}
	
	public String getEndereco() {
		return endereco.getNomeDaRua()+" "+endereco.getNumeroCasa()+" "+endereco.getBairro(); 
	}
	
	public String toString(){
		String str = "";
		
		str += "Contratante: "+this.contratante.getNome()+"\n";
		str += this.endereco;
		
		return str;
		
	}
}
