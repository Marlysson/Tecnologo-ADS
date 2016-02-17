package br.edu.ifpi.conta.principal;

import br.edu.ifpi.conta.modelo.*;


public class TestaDeposita {
	public static void main(String[] args) {
		Conta cp = new ContaPoupanca();
		
		try{
			cp.deposita(-100);	
		}catch(ValorInvalidoException e){
			System.out.println(e.getMessage());
		}
		
		
	}
}
