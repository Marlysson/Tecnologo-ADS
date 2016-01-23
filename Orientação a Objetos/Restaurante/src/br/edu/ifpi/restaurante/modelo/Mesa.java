package br.edu.ifpi.restaurante.modelo;

public class Mesa {
	
	public final static String DISPONIVEL = "Aberta";
	public final static String OCUPADA = "Fechada";
	private final static int MAX_PEDIDOS = 4;
	
	private int identificador;
	private String status;
	private Pedido[] pedidos;
	private int qtdMaximaDePedidosAtual = MAX_PEDIDOS;
	private int contPedidos;
	private boolean taxa;
	private int qtdPessoasRateio;
	
	public Mesa(int numero) {
		this.identificador = numero;
		this.status = Mesa.DISPONIVEL;
		this.pedidos = new Pedido[qtdMaximaDePedidosAtual];
		
		for (int i = 0;i < pedidos.length; i++){
			pedidos[i] = new Pedido();
		}
	}

	public void abrirMesa(int mesa){
		
		Mesa mesaSolicitada = new Mesa(mesa-1);
		
		if (mesaSolicitada.isDisponivel()){
			this.status = Mesa.OCUPADA;	
		}else{
			System.out.println("Mesa "+mesaSolicitada.getIdentificador()+" está ocupada.");
		}
		
	}
	
	public boolean isDisponivel(){
		if (this.getStatus() == Mesa.DISPONIVEL){
			return true;
		}else{
			return false;
		}
	}
	
	public void adicionarPedido(String nome, double valor){
		if (!this.isDisponivel()){
			System.out.println("Por favor, abra a mesa primeiro!"+identificador);
			return;
		}
		
		pedidos[contPedidos++] = new Pedido(nome,valor);
		
		if (contPedidos == qtdMaximaDePedidosAtual){
			qtdMaximaDePedidosAtual += MAX_PEDIDOS;
			
			Pedido[] pedidosDeslocados = this.pedidos;
			
			this.pedidos = new Pedido[qtdMaximaDePedidosAtual];
			
			for (int i = 0; i < pedidosDeslocados.length; i++) {
				this.pedidos[i] = pedidosDeslocados[i];
			}
		}
	}
	
	public double checarConta(boolean taxa){
		double valorConta = 0;
		
		for (Pedido pedido : this.pedidos) {
			if (pedido == null) break;
			valorConta += pedido.getValor();
		}
		
		if (taxa){
			valorConta *= 1.1;
		}
		
		return valorConta;
	}
	
	
	public double rateio(int pessoas){
		this.qtdPessoasRateio = pessoas;
		double valorConta = checarConta(taxa=true);
		
		return valorConta / pessoas;
	}
	
	
	public String getStatus() {
		return this.status;
	}
	
	public void setStatus(String status){
		this.status = status;
	}
	
	public int getIdentificador() {
		return identificador;
	}
	
	public String toString() {
		String str = "\nMesa nº. "+identificador
				    + "\nSTATUS: "+this.getStatus()
					+ "\nNº DE PEDIDOS: "+this.contPedidos+"\n"
					+ "\nPEDIDOS: \n";
					
					for (Pedido pedido : pedidos) {
						if (pedido.getItem() == null) break;
						str +="- "+pedido.getItem()+"  R$ "+pedido.getValor()+"\n";
					}
					if(taxa){
						str += "\nTotal da conta:(+10%) R$ " + String.format("%.2f",this.checarConta(taxa=true)); 
					}else{
						str += "\nTotal da conta: R$ " + String.format("%.2f",this.checarConta(taxa=false));
					}
					
					
					if (this.qtdPessoasRateio > 1){
						str += "\nValor do rateio para " + this.qtdPessoasRateio + ": R$ "+String.format("%.2f", rateio(this.qtdPessoasRateio)) + "\n";
					}
		return str;
	}


}