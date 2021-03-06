import re
from commands import *

#Command groups with all alternate commands for that group
cmdOpen = ("open")
cmdAuthorize = ("authorize","authorise")
cmdDeauthorize = ("deauthorize","deauthorise")
cmdLock = ("lock","lockdown")
cmdHelp = ("help","?")
cmdAdd = ("add")

#Authorization levels required for different commands
levOpen = 2
levAuthorize = 3
levDeauthorize = 4
levLock = 3
levAdd = 0

#Help text displayed for different commands
texOpen = " - Open the door"
texAuthorize = " - Authorize $USER to open the door"
texDeauthorize = " - Prevent $USER from opening the door"
texLock = " - Prevent the door from being opened"
texHelp = " - Lists commands, or gives help using $COMMAND"
texAdd = " - Add an additional phone number tied to your user"

global cmdList

#Functions for each command
def funcOpen():
	return "opening the door"

def funcHelp(command):
	if (command != "null"):
		for i in baseCmd.instances:
			if(command in i.cmd):
				return i.getHelp()
	else:
		string = "{"
		for i in baseCmd.instances:
			string += i.getAlts()
		string += "}"
		return string

def funcAuthorize():
	return "placeholder"

def funcDeauthorize():
	return "placeholder"

def funcLock():
	return "placeholder"	

openObj = baseCmd(cmdOpen,texOpen,funcOpen)
helpObj = baseCmd(cmdHelp,texHelp,funcHelp)
authorizeObj = actionCmd(cmdAuthorize,texAuthorize,funcAuthorize)
deauthorizeObj = actionCmd(cmdDeauthorize,texDeauthorize,funcDeauthorize)
lockObj = baseCmd(cmdLock,texLock,funcLock)

class command:
	def __init__(self,issuer,text): # Who issued the command (either a phone number or terminal which is 0), and the text of the command
		text = text.lower()
		self.splitText = text.split() # Splits text up into individual arguments (e.g authorize user becomes 'authorize,user')
		self.commandType = self.splitText[0] # Command type is the first argument in the command
		if(len(self.splitText) > 1): # If the command has additional arguments beyond the command type
			self.argument = self.splitText[1]
	
	def run(self): # Command is run
		for i in baseCmd.instances:
			if(self.commandType in i.cmd):
				try:
					self.argument *= 1
					try:
						return i.func(self.argument)
					except:
						return i.func()
				except:
					try:
						return i.func()
					except:
						return i.func("null")

		return "Unrecognized command \"" + self.commandType.upper() + "\""
