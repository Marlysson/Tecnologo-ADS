import javax.swing.JOptionPane;

class Exercicio10 {
	public static void main(String[] args){
		int x1 = Integer.parseInt(JOptionPane.showInputDialog("x1 do ponto: "));
		int y1 = Integer.parseInt(JOptionPane.showInputDialog("y1 do ponto: "));
		String quadrante;

		if( x1 > 0 && y1 > 0){
			quadrante = "1";
		}else if ( x1 < 0 && y1 > 0 ){
			quadrante = "2";
		}else if (x1 < 0 && y1 < 0){
			quadrante = "3";
		}else{
			quadrante = "4";
		}

		JOptionPane.showMessageDialog(null,String.format("O ponto (%d,%d) esta no quadrante %s",x1,y1,quadrante));
	}
}