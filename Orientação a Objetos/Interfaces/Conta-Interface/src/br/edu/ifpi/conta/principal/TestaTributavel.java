package br.edu.ifpi.conta.principal;

import br.edu.ifpi.conta.modelo.Conta;
import br.edu.ifpi.conta.modelo.ContaCorrente;
import br.edu.ifpi.conta.modelo.Tributavel;

class TestaTributavel {

	  public static void main(String[] args) {
	    
		ContaCorrente cc = new ContaCorrente();
	    cc.deposita(100);
	    
	    System.out.println(cc.calculaTributos());

	    Tributavel t = cc;
	    System.out.println(t.calculaTributos());
	    
	  }
	}