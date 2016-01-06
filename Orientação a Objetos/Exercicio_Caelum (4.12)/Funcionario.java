class Funcionario{

	String nome;
	String departamento;
	double salario;
	Data dataDeEntrada;
	String rg;

	public void recebeAumento(double aumento){
		this.salario += aumento;
	}

	public double calculaGanhoAnual(){
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
		System.out.println("Ganho anual: " + this.calculaGanhoAnual());

	}

}