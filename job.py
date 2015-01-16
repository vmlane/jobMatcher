from pair import *
class Job:
	def __init__(self, name, prefs, maxMatches=4):
		self.name = name
		self.maxMatches = maxMatches
		self.prefs = prefs
		self.possibilities = self.prefs[:]
		self.matches = []
		self.numMatches = 0
	def isFree(self):
		return self.numMatches < self.maxMatches
	def isEmpty(self):
		len(self.possibilities) == 0
	def getPrefs(self):
		return self.prefs[:]
	# lower rank means more preferred
	def getPersonRank(self, person):
		return self.prefs.index(person) if person in self.prefs else float("inf")
	# Get worst (highest) rank
	def getMatchRank(self):
		worstMatchRank = -1
		worstMatch = None
		for match in self.matches:
			if self.getPersonRank(match) >  worstMatchRank:
				worstMatchRank = self.getPersonRank(match)
				worstMatch = match
		return worstMatchRank
	def getMatches(self):
		return self.matches[:]
	def pop(self):
		return self.possibilities.pop(0)
	def match(self, person):
		self.numMatches += person.numPeople
		self.matches.append(person)
	def canMatch(self, person):
		if person.isNoob:
			# cooking jobs can't pair noobs
			numNoobs = len(filter(lambda x: x.isNoob, self.matches)) 
			tooManyNoobs = numNoobs > self.maxMatches / 2
			# one match is a pair, and the other is a noob
			pairAndNoob = len(self.matches) != self.numMatches and numNoobs > 0
			return not (pairAndNoob and tooManyNoobs)
		return self.numMatches + person.numPeople <= self.maxMatches
	def unmatch(self, person):
		if isinstance(person, Pair):
			self.numMatches -= 2
		else:
			self.numMatches -= 1
		self.matches.remove(person)