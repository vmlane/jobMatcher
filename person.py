class Person:
	def __init__(self, name, semsCooked, prefs, arrivalTimes, isNoob=False):
		self.name = name
		self.prefs = prefs
		self.possibilities = self.prefs[:]
		self.arrivalTimes = arrivalTimes
		self.myMatch = None
		self.isNoob = isNoob
		self.semsCooked = semsCooked
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