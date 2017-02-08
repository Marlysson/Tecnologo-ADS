# -*- coding : utf-8 -*-

name = str(input("Your name: "))
number = str(input("Your phone number: "))
address = str(input("Your home address: "))

def show_information(name,number,address):
	print("Name : {}".format(name))
	print("Phone number : {}".format(number))
	print("Address : {}".format(address))

print("")
show_information("Marlysson","9999-1111","Home")
print("")
