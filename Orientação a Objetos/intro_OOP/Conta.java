class Conta{
	int numero;
	String titular;
	String cpf;
	double saldo;

	public String toString(){
		return "Conta: " + numero + " Saldo " + saldo;
	}

	public void sacar( double valor ){
		saldo = saldo - valor;
	}

	public void deposito( double valor ){

	}

	public void transferir( double valor , Conta destino){
		if(this.sacar(valor)){
			destino.deposito(valor);
		}
	}
}