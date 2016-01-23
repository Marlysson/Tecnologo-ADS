package br.edu.ifpi.conta.principal;

import br.edu.ifpi.conta.modelo.ContaCorrente;
import br.edu.ifpi.conta.modelo.GerenciadorDeImpostoDeRenda;
import br.edu.ifpi.conta.modelo.SeguroDeVida;

public class TestaGerenciadorDeImpostoDeRenda {
	  public static void main(String[] args) {
	  
	    GerenciadorDeImpostoDeRenda gerenciador = new GerenciadorDeImpostoDeRenda();
	    
	    SeguroDeVida seguro = new SeguroDeVida();
	    gerenciador.adiciona(seguro);
	  
	    ContaCorrente cc = new ContaCorrente();
	    cc.deposita(1000);
	    gerenciador.adiciona(cc);
	  
	    System.out.println(gerenciador.getTotal());
	    
	    System.out.printf("O Saldo é %.2f ",cc.getSaldo());
	  }
	}
