package br.edu.ifpi.conta.principal;

import br.edu.ifpi.conta.modelo.AtualizaContas;
import br.edu.ifpi.conta.modelo.Conta;
import br.edu.ifpi.conta.modelo.ContaCorrente;
import br.edu.ifpi.conta.modelo.ContaPoupanca;
import br.edu.ifpi.conta.modelo.Banco;


public class TestaContas {

	public static void main(String args[]){
		
		Conta c = new Conta();
		ContaCorrente cc = new ContaCorrente();
		ContaPoupanca cp = new ContaPoupanca();
		
		Banco banco = new Banco();
		
		banco.adiciona(c);
		banco.adiciona(cc);
		banco.adiciona(cp);
		
		c.deposita(1000);
		cc.deposita(2000);
		cp.deposita(2500);
		
		AtualizaContas verificador = new AtualizaContas(0.01);
		
		for(int i=0;i < banco.totalContas(); i++){
			if(banco.pegaConta(i) == null) break;
			
			verificador.roda(banco.pegaConta(i));
		}
		
		
		System.out.println(banco);
		System.out.print("Saldo Total: R$ "+verificador.getSaldoBanco());
				
	}
	
}
