package br.edu.ifpi.restaurante.modelo;

public class Restaurante {
	private String nome;
	private Mesa[] mesas;
	
	public Restaurante(String nome,int quantMesas){
		//Constructor,starts the quantity of tables and inicializes them 
		this.nome = nome;
		this.mesas = new Mesa[quantMesas];
		
		for(int i = 0; i < mesas.length; i++){
			mesas[i] = new Mesa(i+1);
		}
	}

	public String getNome(){
		return this.nome;
	}
	
	public Mesa abrirMesa(int numeroMesa){
		//opens the set table and define your status to "OCUPADO".
		
		Mesa mesaEscolhida = mesas[numeroMesa-1];
		
		if (!mesaEscolhida.isDisponivel()){
			System.out.println("Mesa "+ mesaEscolhida.getIdentificador() +" ocupada, escolha outra mesa.");
		}else{
			mesaEscolhida.setStatus(Mesa.OCUPADA);	
		}
		
		
		return mesaEscolhida;
	}
	
	public Mesa[] getMesas(){
		//Return all tables of restaurant
		return mesas;
	}
	
	public String verMovimento(){
		int mesasDisponiveis = 0;
		int mesasOcupadas = 0;
		int mesasReservadas = 0;
		double valorTotal = 0;
		String retorno = "";
		
		boolean taxa = false;
		
		for(Mesa mesa: getMesas()){
			valorTotal += mesa.checarConta(taxa);
			
			if (mesa.getStatus() == Mesa.DISPONIVEL){
				mesasDisponiveis += 1;
			}else if (mesa.getStatus() == Mesa.OCUPADA){
				mesasOcupadas += 1;
			}else{
				mesasReservadas += 1;
			}
		}
		
		retorno += "Movimento do Restaurante "+this.getNome()+"\n";
		retorno += "Mesas Disponiveis: "+mesasDisponiveis+"\n";
		retorno += "Mesas Ocupadas: "+mesasOcupadas+"\n";
		retorno += "Mesas Reservadas: "+mesasReservadas+"\n";
		retorno += "RENDA TOTAL: R$"+valorTotal;
		
		return retorno;
	}
	
	public String toString(){
		String str = "Restaurante: "+nome+"\n \n";
		
		for(Mesa mesa: getMesas()){
			str += mesa+"\n";
		}
		
		return str;
	}
}
