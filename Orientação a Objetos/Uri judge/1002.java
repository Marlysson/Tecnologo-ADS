import javax.swing.JOptionPane;

class Exercicio2{
	
	public static void main(String[] args){
		double pi = 3.14159;

		double raio = Double.parseDouble(JOptionPane.showInputDialog("Digite o raio: "));

		double area = pi * (raio * raio);

		JOptionPane.showMessageDialog(null,String.format("A area da circunferencia e: %.4f",area));
	}
}