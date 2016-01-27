package br.edu.ifpi.aluguel.modelo;

public class Aluguel {

	private Tema tema;
	private Festa festa;
	private double valorLocacao; 
	private String dataFesta;
	private String horaInicio;
	private String horaFinal;
	
	public Aluguel(Festa festa,Tema tema,double valor){
		this.festa = festa;
		this.tema = tema;
		this.valorLocacao = valor;
	}
	
	public double getValorTotal(){
		return this.valorLocacao + tema.getValor();
	}
	
	public void setDataFesta(String data){
		this.dataFesta = data;
	}
	
	public void setHoraInicio(String hora){
		this.horaInicio = hora;
	}
	
	public void setHoraFinal(String hora){
		this.horaFinal = hora;
	}
	
	public String toString(){
		String str = "";
		
		str += "CONTRATANTE: \n";
		str += festa.getContratante()+"\n \n";
		
		str += "HORÁRIO: \n";
		str += "Data: "+this.dataFesta+"\n";
		str += "Hora de inicio: "+this.horaFinal+"\n";
		str += "Hora término: "+this.horaFinal+"\n \n"; 
		
		str += "TEMA: \n";
		str += "Itens: \n";
		
		for( Item item : tema.getItens()){
			if (item != null){
				str += "- "+item.getNome();
				str += " - R$ "+item.getValor()+"\n";	
			}
		}

		str += "\nVALOR TOTAL(Locação + Tema)\n";
		str += "R$ "+this.getValorTotal();
		
		
		return str;
	}
	
}
