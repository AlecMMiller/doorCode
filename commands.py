class baseCmd(object):
	instances = []

	def __init__(self,cmd,help,func): # List of commands, help text, function this command runs
		self.cmd = cmd
		self.help = help
		self.func = func
		self.instances.append(self)


	def getAlts(self): # Returns list of all alternate commands

		if type(self.cmd) is str: # If there's only one command in the group
			return "{" + self.cmd.upper() + "}"

		else:
			n = 0	# Don't put comma before the first command		
			string = "{"
			for cmd in self.cmd: # Adds ',$COMMAND' to the string listing commands'
				if(n==1):
					string += ","
				string += cmd.upper()
				n = 1
			string += "}"
			return string

	def getHelp(self): # Gives list of alts followed by the help text

		return self.getAlts() + self.help

class actionCmd(baseCmd):
	def __init__(self,cmd,help,func):
		super(baseCmd,self).__init__()

class lvlCmd(actionCmd):
	def __init__(self,cmd,help,func):
		super(baseCmd,self).__init__()
