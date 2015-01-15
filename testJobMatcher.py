from jobMatcher import *

fullJobs = matchmaker()
allnames = []
for job in fullJobs:
    people = job.getMatches()
    names = []
    for person in people:
        names.append(person.name)
    allnames.extend(names)
    print job.name,':',names
print sorted(allnames)
