class TestaConta {
	public static void main( String[] args){
		
		Conta conta1 = new Conta();
		conta1.titular = "Marlysson";
		conta1.numero  = 001;
		conta1.saldo   = 1300;

		Conta conta2 = new Conta();
		conta2.titular = "Marcelo";
		conta2.numero  = 002;
		conta2.saldo   = 1000;

		conta1.sacar(500);
		conta2.sacar(500);

		System.out.println(conta1);
		System.out.println(conta2);
	}
}