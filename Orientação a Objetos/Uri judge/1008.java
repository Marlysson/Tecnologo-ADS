import javax.swing.JOptionPane;

class Exercicio8 {
	public static void main(String[] args){
		int num1 = Integer.parseInt(JOptionPane.showInputDialog("Digite o primeiro numero:"));
		int num2 = Integer.parseInt(JOptionPane.showInputDialog("Digite o segundo numero:"));

		int maior = (num1 + num2 + Math.abs(num1 - num2)) / 2;

		JOptionPane.showMessageDialog(null,"O maior e: " + maior );
	}
}