package br.edu.ifpi.conta.modelo;

public class Conta {

		protected double saldo;
		
		public double getSaldo(){
			return this.saldo;
		}
		
		public void saca(double valor){
			this.saldo -= valor;
		}
		
		public void deposita(double valor){
			this.saldo += valor;			
		}
		
		public void atualiza(double taxa){
			this.saldo += this.saldo * taxa;
		}
		
		
}
