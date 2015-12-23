import javax.swing.JOptionPane;

class Exercicio9 {
	public static void main(String[] args){
		int tempo = Integer.parseInt(JOptionPane.showInputDialog("Tempo da viagem"));
		float veloc_media = Float.parseFloat(JOptionPane.showInputDialog("Velocidade da vagem"));

		float espaco = veloc_media * tempo;

		float litros = espaco / (float)12.0;

		JOptionPane.showMessageDialog(null,String.format("Litros gastos %.3f",litros ));
	}
}