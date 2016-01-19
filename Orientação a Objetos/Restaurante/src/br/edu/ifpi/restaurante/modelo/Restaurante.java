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
	
	public String toString(){
		String str = "Restaurante: "+nome+"\n \n";
		
		for(Mesa mesa: getMesas()){
			str += mesa+"\n";
		}
		
		return str;
	}
}
