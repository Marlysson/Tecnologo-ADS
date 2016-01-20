package br.edu.ifpi.conta.modelo;

public class AtualizaContas {

	private double saldo;
	private double selic;
	
	//Constructor, inicialize with selic (taxa) value
	public AtualizaContas(double selic){
		this.selic = selic;
	}
	
	public void roda(Conta c){
		
		String retorno = "";
		
		retorno += "Saldo anterior: R$" + c.getSaldo()+"\n";
		c.atualiza(this.selic); //Atualiza conta com base na taxa do banco
		retorno += "Saldo atual: R$ "+c.getSaldo()+"\n";
		
		this.saldo += c.getSaldo(); //Acumula o saldo na conta do banco
		
		System.out.println(retorno);;
	}
	
	public double getSaldoBanco(){
		return this.saldo;
	}
}
