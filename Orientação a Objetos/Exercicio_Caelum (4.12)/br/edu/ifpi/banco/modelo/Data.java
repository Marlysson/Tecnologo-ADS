package br.edu.ifpi.banco.modelo;

class Data{
	int dia;
	int mes;
	int ano;

	public String formatada(){
		return dia+"/"+mes+"/"+ano;
	}
}