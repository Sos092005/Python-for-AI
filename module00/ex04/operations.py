import sys

args = sys.argv[1:]
len = len(args)==2
type= args[0].isnumeric() and args[1].isnumeric( ) and len


if not type:
	 print("""more or less than two arguments are provided or if one of the arguments is not
		an integer""")
else:
	try:

		A= int(args[0])
		B= int(args[1])

		print(f"""
		Sum:		{A+B}
		Difference: {A-B}
		Product: {A*B}
		Quotient: {int(A/B)}
		Remainder: {A%B}
		""")
	except Exception as e:
		print(e)

