class Pair:
	def __init__(self, person1, person2):
		self.names = [person1.name, person2.name]
		self.name = person1.name+person2.name
		self.myMatch = ''
		self.isNoob = False

		self.prefs = []
		# Pair preferences is intersection of preferences of each person
		person2prefs = person2.getPrefs()
		for pref in person1.getPrefs():
			if pref in person2prefs:
				self.prefs.append(pref)
		self.possibilities = self.prefs[:]
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