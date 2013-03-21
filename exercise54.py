#exercise 5.4

Mark Levi 


def is_triangle(a,b,c):
	if a > (b+c):
		print "No"
	elif b > (a+c):
			print "No"
	elif c > (a+b):
			print "No"
	else:
		print "Yes"

a = int(raw_input('What is the length of the first side?\n'))
b = int(raw_input('What is the length of the second side?\n'))
c = int(raw_input('What is the length of the third side?\n'))

is_triangle(a,b,c)

