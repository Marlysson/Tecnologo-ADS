# -*- coding : utf-8 -*-

def get_dezenas(number):
	return (number // 10) % 10

print(get_dezenas(420))
print(get_dezenas(100))
print(get_dezenas(142))
print(get_dezenas(440))
print(get_dezenas(123))