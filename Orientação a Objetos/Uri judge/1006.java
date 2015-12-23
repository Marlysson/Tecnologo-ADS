import javax.swing.JOptionPane;

class Exercicio6 {
	public static void main(String[] args){
		int valor = Integer.parseInt(JOptionPane.showInputDialog("Segundos: "));

		int horas =(int)Math.floor(valor / 3600);
		int minutos = (int)Math.floor(( valor - horas * 3600 )/ 60);
		int segundos = valor - (horas * 3600) - (minutos * 60);
		
		// if (segundos >= 60){
		//	minutos += 1;
		// 	segundos = 60 - segundos;
		// }
		// if(minutos >= 60){
		//	horas += 1;
		// 	minutos = 60 - minutos;
		// }

		JOptionPane.showMessageDialog(null,horas + ":" + minutos + ":" + segundos);
	}
}