import javax.swing.JOptionPane;

class Exercicio1{
	public static void main(String[] args){

		int num1 = Integer.parseInt(JOptionPane.showInputDialog("Digite o primeiro numero: "));
		int num2 = Integer.parseInt(JOptionPane.showInputDialog("Digite o segundo numero:"));

		JOptionPane.showMessageDialog(null,"A soma e: " + (num1 + num2));
	}
}