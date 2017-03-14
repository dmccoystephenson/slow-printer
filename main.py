import sys
import time

def slowprint(string):
	for i in string:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(.03)
	print "\n"

slowprint("Welcome to the game!")
