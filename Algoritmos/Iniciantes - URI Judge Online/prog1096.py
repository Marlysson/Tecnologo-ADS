# -*- coding:utf8 -*-

i = 1
j = 7 

while True:
	print 'I={} J={}'.format(i,j)
	j -= 1

	if i == 9 and j == 5:
		print 'I={} J={}'.format(i,j)
		break

	if j == 5:
		print 'I={} J={}'.format(i,j)
		j = 7
		i += 2	
	
