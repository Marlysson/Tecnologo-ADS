# -*- coding : utf-8 -*-

# Maior de dois números

def maior(num1,num2):
	if num1 > num2:
		return num1
	return num2

assert maior(5,6) == 6
assert maior(10,6) == 10
assert maior(15,14) == 15