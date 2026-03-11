import sys, string

arg= sys.argv[1:]

def text_analyzer(args):
	"""
	Displays the total number of printable characters,
	and respectively : the number of upper-case
	characters, lower-case characters, 
	punctuation characters and spaces.
	"""
	if args==[]:
		print("What's the text to analyse?")
	else:
		up=0
		low=0
		space=0
		signs=0
		char=0
		for i in args:
			for j in i:
				char +=1
				if j.isupper():
					up+=1
				elif j.islower():
					low+=1
				elif j in string.punctuation:
					signs+=1
				elif j==' ':
					space+=1

		print('The text contains ',char,' printable character(s):')
		print('-', up, ' upper letter(s)') 
		print('-' ,low ,'lower letter(s)')
		print('-' ,signs ,'punctuation mark(s)')
		print('-',space,' space(s)')


text_analyzer(arg)
