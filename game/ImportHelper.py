import sys
sys.path.insert(0, './functions')
class managePackages:
	def __init__(self):
		self.imports = {'UIelements.py','dialog.py'}
	def getImports(self):
		for item in self.imports:
			import 
	def setImports(self,imports):
		self.imports = imports
