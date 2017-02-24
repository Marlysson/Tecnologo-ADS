# -*- coding : utf-8 -*-

# Mostrar números em ordem crescente ( menor pro maior )

def crescente(num1,num2,num3):

	if (num1 < num2) and (num1 < num3):
		if (num2 < num3):
			return [num1,num2,num3]
		else:
			return [num1,num3,num2]
	elif (num2 < num1) and (num2 < num3):
		if num1 < num3:
			return [num2,num1,num3]
		else:
			return [num2,num3,num1]
	else:
		if (num1 < num2):
			return [num3,num1,num2]
		else:
			return [num3,num2,num3]

assert crescente(1,2,3) == [1,2,3]
assert crescente(5,3,1) == [1,3,5]
assert crescente(13,12,10) == [10,12,13]
