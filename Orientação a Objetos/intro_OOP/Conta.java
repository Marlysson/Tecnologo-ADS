class Conta{
	int numero;
	String titular;
	String cpf;
	double saldo;

	public String toString(){
		return "Conta: " + numero + " Saldo " + saldo;
	}

	public boolean sacar( double valor ){
		if (valor <= this.saldo){
			this.saldo -= valor;
			return true;
		}else{
			System.out.println("Saldo insuficiente.");
			return false
		}

	}

	public void deposito( double valor ){
		this.saldo += valor;
	}

	public void transferir( double valor , Conta destino){
		if(this.sacar(valor)){
			destino.deposito(valor);
		}
	}
}