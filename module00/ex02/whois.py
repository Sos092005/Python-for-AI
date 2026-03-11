import sys

args = sys.argv[1:]

if (len(args) ==0):
	pass
elif (len(args) >1):
	print('AssertionError: more than one argument is provided')
else:
	if (type(int(args[0])) != int):
		print('AssertionError: argument is not an integer')
	elif (len(args) == 1):
		number = int(args[0])
		even = ((number % 2)==0 and number !=0)
		odd  = (number % 2)==1
		zero = number == 0
		
		if zero:
			print ("I'm Zero")
		elif even:
			print("I'm Even")
		elif odd:
			print("I'm Odd")
	else:
		pass
