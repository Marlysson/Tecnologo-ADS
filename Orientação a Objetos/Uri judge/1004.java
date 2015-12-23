import javax.swing.JOptionPane;

class Exercicio4{
	public static void main(String[] args){
		int cedula = Integer.parseInt(JOptionPane.showInputDialog("Valor da cedula: "));

		int []cedulas = {100,50,20,10,5,2,1};
		int []valores = new int [7];
		int i = 0;
		String saida = "";
		
		while (cedula > 0){
			double valor = Math.floor( (double)cedula / (double)cedulas[i]);
			valores[i] = (int)valor;
			cedula -= valor * cedulas[i];

			saida += valores[i] + " cedulas de " + "R$ " + cedulas[i] + ",00\n";

			i++;
		}

		JOptionPane.showMessageDialog(null,saida);
	}
}