from jobMatcher import *

fullJobs = matchmaker()
allnames = []
for job in fullJobs:
    allnames.extend(job.getMatches())
    print job.name,':',job.getMatches()
print sorted(allnames)
