import copy
from person import Person
from job import Job

sunday = Job('sunday', ['amber', 'lisa', 'ana','matt', 'rob', 'kyle', 'kevin', 'abi', 'amy', 'jack', 'hope', 'mike'])
monday = Job('monday', ['abi', 'kevin', 'rob', 'matt','amy', 'amber', 'lisa', 'kyle', 'jack','ana', 'hope', 'mike'])
tuesday = Job('tuesday',  ['rob', 'hope', 'abi', 'matt','lisa', 'jack', 'kevin', 'kyle', 'ana', 'amber', 'amy', 'mike'])
wednesday = Job('wednesday',  ['hope', 'kevin', 'abi', 'lisa', 'jack','ana', 'kyle', 'amy','matt', 'mike', 'rob', 'amber'])
thursday = Job('thursday',  ['amy', 'kyle', 'lisa', 'mike', 'hope', 'kevin', 'amber','matt', 'ana', 'jack', 'rob', 'abi'])
studybreak = Job('studybreak',  ['jack','amy', 'kyle', 'lisa', 'amber', 'ana', 'rob', 'abi', 'matt', 'mike', 'hope', 'kevin'])
staples = Job('staples',  ['rose','vero','jaz','raul','jose','jack','amy', 'kyle', 'lisa', 'amber', 'ana', 'rob', 'abi', 'matt', 'mike', 'hope', 'kevin'],3)
kitchenMonster = Job('kitchenMonster',  ['rose','vero','jaz','raul','jose','jack','amy', 'kyle', 'lisa', 'amber', 'ana', 'rob', 'abi', 'matt', 'mike', 'hope', 'kevin'],1)
loungeMonster = Job('loungeMonster',  ['rose','vero','jaz','raul','jose','jack','amy', 'kyle', 'lisa', 'amber', 'ana', 'rob', 'abi', 'matt', 'mike', 'hope', 'kevin'],1)


abi = Person('abi',['tuesday', 'monday', 'thursday', 'sunday'])
ana = Person('ana', ['tuesday', 'monday', 'wednesday', 'thursday', 'sunday'])
rob = Person('rob', ['tuesday', 'sunday', 'wednesday', 'monday', 'thursday'])
lisa = Person('lisa', ['wednesday', 'monday', 'thursday', 'tuesday', 'sunday'])
kevin = Person('kevin', ['thursday', 'monday', 'wednesday', 'sunday', 'tuesday'])
kyle = Person('kyle', ['tuesday', 'monday', 'sunday', 'studybreak','thursday', 'wednesday'])
mike = Person('mike', ['tuesday', 'monday', 'studybreak','wednesday', 'sunday', 'thursday'])
hope = Person('hope', ['tuesday', 'monday', 'thursday', 'sunday', 'wednesday'])
amy = Person('amy', ['wednesday', 'tuesday', 'monday', 'sunday'])
amber = Person('amber', ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday'])
matt = Person('matt', ['wednesday','studybreak', 'tuesday', 'monday', 'sunday'])
jack = Person('jack', ['studybreak', 'thursday','sunday', 'monday', 'tuesday', 'wednesday'])
rose = Person('rose', ['staples','kitchenMonster','loungeMonster', 'sunday', 'tuesday', 'monday', 'thursday', 'wednesday'])
vero = Person('vero', ['loungeMonster','staples','kitchenMonster','sunday','monday','wednesday' ])
jaz = Person('jaz', ['staples','loungeMonster','kitchenMonster','sunday'])
raul = Person('raul', ['kitchenMonster','staples', 'tuesday', 'monday', 'sunday'])
jose = Person('jose', ['studybreak','loungeMonster','staples','thursday','sunday', 'monday', 'tuesday', 'wednesday'])

jobs = [sunday, monday, tuesday, wednesday, thursday, studybreak,staples,kitchenMonster,loungeMonster]
 
people = [abi,ana,rob,lisa,kevin,kyle,mike,hope,amy,amber,matt,jack,rose,vero,jaz,raul,jose]
 
def matchmaker():
    freeJobs = jobs[:]
    fullJobs = []
    i =0
    while freeJobs:
        i = i+1
        job = freeJobs.pop(0)
        person_name = job.pop()
        person = getPerson(person_name)

        if job.name in person.getPrefs():
            if person.isFree():
                person.match(job.name)
                job.match(person.name)
                print("  %s and %s" % (job.name, person.name))
            else:
                # Person has job
                if person.getMatchRank() > person.getJobRank(job.name):
                    oldjob = getRemoveJob(freeJobs,fullJobs,person.getMatch())
                    # Person prefers new job offer
                    person.match(job.name)
                    job.match(person.name)
                    # old job has open spot
                    oldjob.unmatch(person.name)
                    freeJobs.append(oldjob)
                    print("  %s quit %s for %s" % (person.name, oldjob.name, job.name))

        if job.isFree():
            # still has open spots
            freeJobs.append(job)
        else:
            # no more spots left
            fullJobs.append(job)
    return fullJobs
 
def getRemoveJob(jobs1,jobs2,name):
    for job in jobs1:
        if job.name == name:
            jobs1.remove(job)
            return job
    for job in  jobs2:
        if job.name == name:
            jobs2.remove(job)
            return job
    else:
        return None

def getPerson(name):
    for person in people:
        if name == person.name:
            return person

def match(job,person):
    person.match(job.name)
    job.match(person.name)


# print('\nEngagejobsts:')
# engaged = matchmaker()
 
# print('\nCouples:')
# print('  ' + ',\n  '.join('%s is matched to %s' % couple
#                           for couple in sorted(engaged.items())))
# print()
#print('Engagejobst stability check PASSED'
#      if check(engaged) else 'Engagejobst stability check FAILED')
 
#print('\n\nSwapping two old_jobs to introduce an error')
#engaged[people[0]], engaged[people[1]] = engaged[people[1]], engaged[people[0]]
#for person in people[:2]:
#    print('  %s is now engaged to %s' % (person, engaged[person]))
#print()
#print('Engagejobst stability check PASSED'
#      if check(engaged) else 'Engagejobst stability check FAILED')
