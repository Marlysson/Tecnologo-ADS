import javax.swing.JOptionPane;

class Exercicio5 {
	public static void main(String[] args){
		float x1 = Float.parseFloat(JOptionPane.showInputDialog("x1 do ponto 1: "));
		float y1 = Float.parseFloat(JOptionPane.showInputDialog("y1 do ponto 1: "));
		float x2 = Float.parseFloat(JOptionPane.showInputDialog("x2 do ponto 2: "));
		float y2 = Float.parseFloat(JOptionPane.showInputDialog("y2 do ponto 2: "));

		float distancia = (float)Math.sqrt(Math.pow((x1 - x2),2) + Math.pow((y1 - y2),2));

		JOptionPane.showMessageDialog(null,String.format("Distancia entre (%d,%d) e (%d,%d): %.2f",(int)x1,(int)y1,(int)y1,(int)y2,distancia));
		
	}
}