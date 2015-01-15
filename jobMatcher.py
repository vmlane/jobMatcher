import copy
from person import Person
from job import Job
from pair import *
from cookingjob import *
from noncookingjob import *


abi = Person('abi', 0,
    ['tuesday', 'monday', 'thursday', 'sunday'],
    { 'sunday': 4.5, 'monday': 4.0, 'tuesday': 3, 'wednesday': 4.15, 'thursday': 3.5, 'studybreak': 10 },
    True
    )
ana = Person('ana', 1,
    ['tuesday', 'monday', 'wednesday', 'thursday', 'sunday'],
    { 'sunday': 3.5, 'monday': 4, 'tuesday': 3, 'wednesday': 4.15, 'thursday': 3.5, 'studybreak': 'minimal' })
rob = Person('rob', 0,
    ['tuesday', 'sunday', 'wednesday', 'monday', 'thursday'],
    { 'sunday': 4.0, 'monday': 4.0, 'tuesday': 4.0, 'wednesday': 4, 'thursday': 3.5, 'studybreak': 'minimal' },
    True)
lisa = Person('lisa', 3,
    ['wednesday', 'monday', 'thursday', 'tuesday', 'sunday'],
    { 'sunday': 4.5, 'monday': 4.0, 'tuesday': 4.0, 'wednesday': 4, 'thursday': 4.15, 'studybreak': 'minimal' })
kevin = Person('kevin', 2,
    ['thursday', 'monday', 'wednesday', 'sunday', 'tuesday'],
    { 'sunday': 4.0, 'monday': 4.15, 'tuesday': 4.15, 'wednesday': 4, 'thursday': 3.5, 'studybreak': 'minimal' })
kyle = Person('kyle', 4,
    ['tuesday', 'monday', 'sunday', 'studybreak','thursday', 'wednesday'],
    { 'sunday': 4.0, 'monday': 4.0, 'tuesday': 4.0, 'wednesday': 4, 'thursday': 3.5, 'studybreak': 10 })
mike = Person('mike', 5,
    ['tuesday', 'monday', 'studybreak','wednesday', 'sunday', 'thursday'],
    { 'sunday': 4.0, 'monday': 4.0, 'tuesday': 4.0, 'wednesday': 4.16, 'thursday': 4.15, 'studybreak': 10 })
hope = Person('hope', 3,
    ['tuesday', 'monday', 'thursday', 'sunday', 'wednesday'],
    { 'sunday': 4.0, 'monday': 4.0, 'tuesday': 4.0, 'wednesday': 4.20, 'thursday': 4.15, 'studybreak': 10 })
amy = Person('amy', 5,
    ['wednesday', 'tuesday', 'monday', 'sunday'],
    { 'sunday': 4.15, 'monday': 4.5, 'tuesday': 4.0, 'wednesday': 4, 'thursday': 'minimal', 'studybreak': 'minimal' })
amber = Person('amber', 3,
    ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday'],
    { 'sunday': 4.0, 'monday': 4.0, 'tuesday': 4.15, 'wednesday': 4, 'thursday': 3.5, 'studybreak': 'minimal' })
matt = Person('matt', 5,
    ['wednesday','studybreak', 'tuesday', 'monday', 'sunday'],
    { 'sunday': 4.0, 'monday': 4.0, 'tuesday': 4.15, 'wednesday': 4, 'thursday': 'minimal', 'studybreak': 10 })
jack = Person('jack', 6,
    ['staples','studybreak', 'thursday','sunday', 'monday', 'tuesday', 'wednesday'],
    { 'sunday': 5, 'monday': 4.0, 'tuesday': 4.0, 'wednesday': 4, 'thursday': 3.5, 'studybreak': 10 })
rose = Person('rose', 6,
    ['staples','kitchenMonster','loungeMonster', 'sunday', 'tuesday', 'monday', 'thursday', 'wednesday'],
    { 'sunday': 4.0, 'monday': 4.0, 'tuesday': 4.5, 'wednesday': 4, 'thursday': 3.5, 'studybreak': 'minimal' })
vero = Person('vero', 5,
    ['loungeMonster','staples','kitchenMonster','sunday','monday','wednesday' ],
    { 'sunday': 4.0, 'monday': 4.0, 'tuesday': 4.5, 'wednesday': 4, 'thursday': 3.5, 'studybreak': 'minimal' })
jaz = Person('jaz', 6,
    ['staples','studybreak','loungeMonster','kitchenMonster','sunday'],
    { 'sunday': 4.5, 'monday': 4.0, 'tuesday': 4.0, 'wednesday': 4, 'thursday': 3.5, 'studybreak': 'minimal' })
raul = Person('raul', 6,
    ['kitchenMonster','studybreak','staples'],
    { 'sunday': 'minimal', 'monday': 'minimal', 'tuesday': 'minimal', 'wednesday': 'minimal', 'thursday': 'minimal', 'studybreak': 10 })
jose = Person('jose', 5,
    ['studybreak','loungeMonster','staples','thursday','sunday', 'monday'],
    { 'sunday': 4.0, 'monday': 4.0, 'tuesday': 'minimal', 'wednesday': 'minimal', 'thursday': 3.5, 'studybreak': 10 })
mattjose=Pair(matt,jose)
people = [abi,ana,rob,lisa,kevin,kyle,mike,hope,amy,amber,jack,rose,vero,jaz,raul,mattjose]

sunday = CookingJob('sunday', people[:])
monday = CookingJob('monday', people[:])
tuesday = CookingJob('tuesday', people[:])
wednesday = CookingJob('wednesday', people[:])
thursday = CookingJob('thursday', people[:])
studybreak = CookingJob('studybreak', people[:], latestArrival=10)
staples = NoncookingJob('staples', people[:] ,3)
kitchenMonster = NoncookingJob('kitchenMonster', people[:],1)
loungeMonster = NoncookingJob('loungeMonster',  people[:],1)
jobs = [sunday, monday, tuesday, wednesday, thursday, studybreak,staples,kitchenMonster,loungeMonster]
 
 
def matchmaker():
    freeJobs = jobs[:]
    fullJobs = []
    i =0
    while freeJobs:
        i = i+1
        job = freeJobs.pop(0)
        try:
            person = job.pop()
        except IndexError:
            freePeople = filter(lambda x: x.isFree(), people)
            names = []
            for p in freePeople:
                names.append(p.name)
            print names
            allnames = []
            freeJobs.append(job)
            for job in freeJobs:
                matches = job.getMatches()
                names = []
                for person in matches:
                    names.append(person.name)
                allnames.extend(names)
                print 'Free',job.name,':',names

            return fullJobs

        if job.name in person.getPrefs() and job.canMatch(person):
            if person.isFree():
                match(job,person)
                print("  %s and %s" % (job.name, person.name))
            else:
                # Person has job
                if person.getMatchRank() > person.getJobRank(job.name):
                    oldjob = person.getMatch()
                    removeJob(freeJobs,fullJobs,oldjob)
                    # Person prefers new job offer
                    match(job,person)
                    # old job has open spot
                    oldjob.unmatch(person)
                    freeJobs.append(oldjob)
                    print("  %s quit %s for %s" % (person.name, oldjob.name, job.name))

        if job.isFree():
            # still has open spots
            freeJobs.append(job)
        else:
            # no more spots left
            fullJobs.append(job)
    return fullJobs
 
def removeJob(jobs1,jobs2,job):
    if job in jobs1:
        jobs1.remove(job)
    if job in jobs2:
        jobs2.remove(job)

def match(job,person):
    person.match(job)
    job.match(person)