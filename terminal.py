from parse import command

isRunning = 1

user = 0

import os
os.system('cls' if os.name == 'nt' else 'clear')

print
print "Welcome to the ASYS control terminal"
print "Please enter a command, or type HELP for help"
print
print "------------------------------------"
print

while isRunning:
	args = raw_input("terminal@ASYS: ")
	if(args == "exit"):
		os.system('cls' if os.name == 'nt' else 'clear')
		isRunning = 0
	else:
		cmd = command(user,args)
		print cmd.run()
