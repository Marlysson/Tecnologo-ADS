package br.edu.ifpi.restaurante.principal;
import br.edu.ifpi.restaurante.modelo.Restaurante;
import br.edu.ifpi.restaurante.modelo.Mesa;

public class TestaRestaurante {
	public static void main(String args[]){
		Restaurante r1 = new Restaurante("Teste",5);
		
		Mesa m1 = r1.abrirMesa(1);
		Mesa m2 = r1.abrirMesa(2);
		
		m1.adicionarPedido("Produto 1",15.50);
		m1.adicionarPedido("Salgado",5);
		
		m2.adicionarPedido("Refrigerante", 10);
		m2.adicionarPedido("Refrigerante 1", 10);
		m2.adicionarPedido("Refrigerante 2", 10);
		
		Mesa m3 = r1.abrirMesa(3);
		
		m3.adicionarPedido("Refri", 10);
		m3.adicionarPedido("Suco", 10);
		
		
		System.out.println("Mesa "+m1.getIdentificador()+" "+m1.getStatus());
		m1.checarConta(true);
		m1.rateio(2);
		System.out.println(m1);
		
		System.out.println("Mesa "+m2.getIdentificador()+" "+m2.getStatus());
		m2.checarConta(true);
		m2.rateio(3);
		System.out.println(m2);
	}
}
