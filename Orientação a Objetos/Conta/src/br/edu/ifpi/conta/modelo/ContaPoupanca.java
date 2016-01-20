package br.edu.ifpi.conta.modelo;

public class ContaPoupanca extends Conta{
	
	public void atualiza(double taxa){
		taxa *= 3;
		super.atualiza(taxa);
	}

}
