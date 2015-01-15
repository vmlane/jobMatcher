import copy

class Pair:
	def __init__(self, person1, person2):
		self.names = [person1.name, person2.name]
		self.name = person1.name+person2.name
		self.semsCooked = (person1.semsCooked + person2.semsCooked)/2
		self.myMatch = None
		self.isNoob = False
		self.numPeople = 2

		# Intersection of preferences of each person, with order based on combined rank
		tempPrefs = {}
		person1prefs = person1.getPrefs()
		person2prefs = person2.getPrefs()
		for i in range(0,len(person1prefs)):
			pref = person1prefs[i]
			if pref in person2prefs:
				tempPrefs[pref] = i + person2prefs.index(pref)
		self.prefs = sorted(tempPrefs, key=tempPrefs.get)
		self.possibilities = self.prefs[:]
		self.arrivalTimes = copy.deepcopy(person1.arrivalTimes)
		for k in self.arrivalTimes:
			# if one is minimal, minimal will be returned
			self.arrivalTimes[k] = max(person2.arrivalTimes[k],self.arrivalTimes[k])
	def isFree(self):
		return self.myMatch is None
	def getPrefs(self):
		return self.prefs[:]
	# lower rank means more preferred
	def getJobRank(self, job):
		return self.prefs.index(job) if job in self.prefs else float("inf")
	def getMatchRank(self):
		return self.getJobRank(self.myMatch.name)
	def getMatch(self):
		return self.myMatch
	def getArrivalTime(day):
		return self.arrivalTimes[day]
	def pop(self):
		return self.possibilities.pop(0)
	def match(self, job):
		self.myMatch = job
	def unmatch(self):
		self.myMatch = None