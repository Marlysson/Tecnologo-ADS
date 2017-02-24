# -*- coding : utf-8 -*-

def TesteIf(L1, L2, L3):
	letras = '';
	
	if L1 == 'V':
		letras = letras + 'A'
	else:
		if L2 == 'V':
			if L3 == 'V':
				letras = letras + 'B'
			else:
				letras = letras + 'C'
				letras = letras + 'D'
	letras = letras + 'E'
	return letras

La = input("Digite uma letra: ")
Lb = input("Digite uma letra: ")
Lc = input("Digite uma letra: ")

#A) Deverá ser mostrado: AE
#B) Deverá ser mostrado: BE
#C) Deverá ser mostrado: CDE
#D) A sequência deve ser: F-F-F

print(TesteIf('F', 'V', 'F'))

