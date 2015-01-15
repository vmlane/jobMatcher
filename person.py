class Person:
	def __init__(self, name, prefs,isNoob=False):
		self.name = name
		self.prefs = prefs
		self.possibilities = self.prefs[:]
		self.myMatch = ''
		self.isNoob = isNoob
	def isFree(self):
		return len(self.myMatch) == 0
	def getPrefs(self):
		return self.prefs[:]
	# lower rank means more preferred
	def getJobRank(self, job):
		return self.prefs.index(job) if job in self.prefs else float("inf")
	def getMatchRank(self):
		return self.getJobRank(self.myMatch)
	def getMatch(self):
		return self.myMatch
	def pop(self):
		return self.possibilities.pop(0)
	def match(self, name):
		self.myMatch = name
	def unmatch(self):
		self.myMatch = ''