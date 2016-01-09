package br.edu.ifpi.banco.modelo;

class Funcionario{

	private String nome;
	private String departamento;
	private double salario;
	private Data dataDeEntrada;
	private String rg;
 	private int identificador;

 	public void setNome(String nome){
 		this.nome = nome;
 	}

 	public String getNome(){
 		return this.nome;
 	}

 	public void setDepartamento(String departamento){
 		this.departamento = departamento;
 	}

 	public String getDepartamento(){
 		return this.departamento;
 	}

	public void setDataEntrada(Data data){
 		this.dataDeEntrada = data;
 	}

 	public String getDataEntrada(){
 		return this.dataDeEntrada;
 	} 	

 	public void setRG(String rg){
 		this.rg = rg;
 	}

 	public String getRG(){
 		return this.rg;
 	}

 	public static getIdentificador(){
 		return this.identificador;
 	}
	public void recebeAumento(double aumento){
		this.salario += aumento;
	}

	public double getGanhoAnual(){
		return this.salario * 12;
	}

	public String toString(){
		return "Nome: " + this.nome + " Salario: " + this.salario;
	}

	public void mostra(){
		System.out.println("Nome: " + this.nome);
		System.out.println("Departamento: " + this.departamento);
		System.out.println("Salario: " + this.salario);
		System.out.println("RG: " + this.rg);
		System.out.println("Data de inicio: " + this.dataDeEntrada.formatada());
		System.out.println("Ganho anual: " + this.getGanhoAnual());

	}

	public Funcionario(){
		Funcionario.identificador = getIdentificador();
	}

	public Funcionario(String nome){
		this.nome = nome;
		Funcionario.identificador = this.getIdentificador();
	}

}