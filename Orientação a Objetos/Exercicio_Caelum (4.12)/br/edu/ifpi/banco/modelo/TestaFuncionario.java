package br.edu.ifpi.banco.modelo;

class TestaFuncionario{

	public static void main(String[] args) {
		
		Funcionario func1 = new Funcionario();
		func1.setNome("Marlysson");
		func1.setDepartamento("Tecnologia da informação");
		func1.setSalario(1200);

		Data data = new Data();
		data.dia = 6;
		data.mes = 1;
		data.ano = 2016;
		
		func1.setDataEntrada(data);
		func1.setRG("1.111.111");

		func1.mostra();

	}

}