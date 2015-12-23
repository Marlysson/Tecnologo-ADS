import javax.swing.JOptionPane;

class Exercicio7 {
	public static void main(String[] args){
		float distancia = Float.parseFloat(JOptionPane.showInputDialog("Distancia percorrida: "));
		
		float gasto = Float.parseFloat(JOptionPane.showInputDialog("Combustivel gasto: "));

		float media = distancia / gasto; 

		JOptionPane.showMessageDialog(null,String.format("Media de combustivel gasto: %.3f km/l",media));
	}
}