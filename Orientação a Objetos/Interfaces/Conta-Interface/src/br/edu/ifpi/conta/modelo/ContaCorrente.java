package br.edu.ifpi.conta.modelo;

public class ContaCorrente extends Conta implements Tributavel{

	public void atualiza(double taxa){
		taxa *= 2;
		super.atualiza(taxa);
	}
	
	public void deposita(double valor){
		valor -= 0.10;
		super.deposita(valor);
	}

	public double calculaTributos() {
		return this.getSaldo() * 0.01;
	}
}
