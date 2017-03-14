import sys
import time

def slowprint(string):
	for i in string:
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(.03)
	print "\n"

if __name__ == "__main__": # test if not used in another program
	slowprint("Welcome to the game!")
