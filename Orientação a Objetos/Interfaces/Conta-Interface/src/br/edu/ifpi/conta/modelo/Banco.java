package br.edu.ifpi.conta.modelo;

public class Banco {
	
	private Conta[] contas;
	private int contContas;
	
	public Banco(){
		this.contas = new Conta[10];
	}
	
	public void adiciona(Conta c){
		this.contas[contContas++] = c;
	}
	
	public Conta pegaConta(int posicao){
		return this.contas[posicao];
	}
	
	public int totalContas(){
		return this.contas.length;
	}
	
	public String toString(){
		String retorno = "";
		
		for(int i = 0; i < contas.length; i++){
			if(contas[i] == null) break;
			
			retorno += "Conta "+(i+1)+"\nSaldo atual: "+contas[i].getSaldo()+"\n \n";
		}
		
		return retorno;
	}
	
}
