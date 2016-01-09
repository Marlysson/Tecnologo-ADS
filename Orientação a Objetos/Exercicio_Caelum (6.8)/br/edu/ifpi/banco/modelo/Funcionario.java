package br.edu.ifpi.banco.modelo;

class Funcionario{

	private String nome;
	private String departamento;
	private double salario;
	private Data dataDeEntrada;
	private String rg;
	private static int identificador;
 

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

 	public Data getDataEntrada(){
 		return this.dataDeEntrada;
 	} 	

 	public void setRG(String rg){
 		this.rg = rg;
 	}

 	public String getRG(){
 		return this.rg;
 	}

	public void recebeAumento(double aumento){
		this.salario += aumento;
	}

	public void setSalario(double salario){
		this.salario = salario;
	}
	
	public static int getIdentificador(){
		return Funcionario.identificador;
	}

	public static int setIdentificador(){
		Funcionario.identificador = identificador++;
	}
	
	public double getSalario(){
		return this.salario;
	}

	public double getGanhoAnual(){
		return this.getSalario() * 12;
	}

	public String toString(){
		return "Nome: " + this.nome + " Salario: " + this.salario;
	}

	public void mostra(){
		System.out.println("Identificador: " + Funcionario.getIdentificador());
		System.out.println("Nome: " + this.nome);
		System.out.println("Departamento: " + this.departamento);
		System.out.println("Salario: " + this.salario);
		System.out.println("RG: " + this.rg);
		System.out.println("Data de inicio: " + this.dataDeEntrada.formatada());
		System.out.println("Ganho anual: " + this.getGanhoAnual());

	}

	public Funcionario(){
		Funcionario.identificador = Funcionario.setIdentificador();
	}

	public Funcionario(String nome){
		Funcionario.setIdentificador();
		this.nome = nome;
	}

}