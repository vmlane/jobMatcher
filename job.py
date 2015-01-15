class Job:
	def __init__(self, name, prefs,maxMatches=2):
		self.name = name
		self.maxMatches = maxMatches
		self.prefs = prefs
		self.possibilities = self.prefs[:]
		self.matches = []
	def isFree(self):
		return len(self.matches) < self.maxMatches
	def getPrefs(self):
		return self.prefs[:]
	# lower rank means more preferred
	def getPersonRank(self, name):
		return self.prefs.index(name) if name in self.prefs else float("inf")
	# todo fix this, get worst (highest) rank?
	def getMatchRank(self):
		worstMatchRank = -1
		worstMatch = ''
		for match in self.matches:
			if self.getPersonRank(match) >  worstMatchRank:
				worstMatchRank = self.getPersonRank(match)
				worstMatch = match
		return worstMatchRank
	def getMatches(self):
		return self.matches[:]
	def pop(self):
		return self.possibilities.pop(0)
	def match(self, name):
		self.matches.append(name)
	def unmatch(self, name):
		self.matches.remove(name)
	def isEmpty(self):
		len(self.possibilities) == 0