import javax.swing.JOptionPane;

class Exercicio3{
	public static void main(String[] args){

		double num1 = Double.parseDouble(JOptionPane.showInputDialog("Digite um numero: "));
		double num2 = Double.parseDouble(JOptionPane.showInputDialog("Digite um numero: "));

		double media = ( num1 * 3.5 + num2 * 7.5 ) / (3.5 + 7.5);

		JOptionPane.showMessageDialog(null,String.format("A media de %.1f com %.1f e: %.5f",num1,num2,media));

	}
}