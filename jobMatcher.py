import copy
from person import Person
from job import Job
from pair import *
from cookingjob import *
from noncookingjob import *


anthony = Person('anthony', 3,
    ['staples','studybreak','loungeMonster','kitchenMonster','thursday','tuesday','sunday','wednesday','monday'],
    { 'sunday': 4, 'monday': 5, 'tuesday': 3, 'wednesday': 4, 'thursday': 3.25, 'studybreak': 10 })
raul = Person('raul', 4,
    ['staples','loungeMonster','kitchenMonster','studybreak','tuesday', 'monday', 'wednesday', 'thursday', 'sunday'],
    { 'sunday': 'minimal', 'monday': 'iminimal', 'tuesday': 'minimal', 'wednesday': 'minimal', 'thursday': 'minimal', 'studybreak': 10 })
vero = Person('vero', 5,
    ['loungeMonster','staples','kitchenMonster','studybreak','sunday', 'monday', 'wednesday', 'tuesday', 'thursday'],
    { 'sunday': 3.5, 'monday': 4.33, 'tuesday': 4.25, 'wednesday': 'minimal', 'thursday': 'minimal', 'studybreak': 10 })
rose = Person('rose', 6,
    ['loungeMonster','kitchenMonster','staples', 'studybreak', 'sunday', 'wednesday', 'tuesday', 'monday', 'thursday'],
    { 'sunday': 3.0, 'monday': 'minimal', 'tuesday': 'minimal', 'wednesday': 4, 'thursday': 'minimal', 'studybreak': 10 })
hollie = Person('hollie', 4,
    ['studybreak','staples','kitchenMonster','loungeMonster','wednesday', 'monday', 'thursday', 'tuesday', 'sunday'],
    { 'sunday': 'minimal', 'monday': 'minimal', 'tuesday': 'minimal', 'wednesday': 'minimal', 'thursday': 'minimal', 'studybreak': 10 })
matt = Person('matt', 2,
    ['studybreak','sunday','tuesday','thursday','wednesday','monday'],
    { 'sunday': 3.0, 'monday': 4.0, 'tuesday': 3.0, 'wednesday': 4, 'thursday': 'minimal', 'studybreak': 10 })
ernesto = Person('ernesto', 4,
    ['staples','loungeMonster','kitchenMonster','studybreak', 'tuesday', 'thursday', 'wednesday', 'monday','sunday'],
    { 'sunday': 4.0, 'monday': 4.15, 'tuesday': 4.15, 'wednesday': 4, 'thursday': 3.5, 'studybreak': 'minimal' })
willy = Person('willy', 6,
    ['loungeMonster','staples','kitchenMonster','studybreak','sunday', 'tuesday', 'monday', 'wednesday','thursday'],
    { 'sunday': 4, 'monday': 'minimal', 'tuesday': 4.0, 'wednesday': 'minimal', 'thursday': 'minimal', 'studybreak': 10 })
ana = Person('ana', 0,
    ['loungeMonster','staples','kitchenMonster','studybreak','sunday', 'tuesday', 'monday', 'wednesday','thursday'],
    { 'sunday': 4, 'monday': 'minimal', 'tuesday': 4.0, 'wednesday': 'minimal', 'thursday': 'minimal', 'studybreak': 10 })
deanna = Person('deanna', 4,
    ['kitchenMonster','loungeMonster','studybreak','staples','tuesday', 'monday', 'thursday', 'sunday', 'wednesday'],
    { 'sunday': 3, 'monday': 3.25, 'tuesday': 3.0, 'wednesday': 3.25, 'thursday': 3, 'studybreak': 10 })
hugo = Person('hugo', 4,
    ['sunday','tuesday','monday','thursday','wednesday'],
    { 'sunday': 3.5, 'monday': 4, 'tuesday': 5, 'wednesday': 4, 'thursday': 3.5, 'studybreak': 10 })
marcos = Person('marcos', 4,
    ['staples','loungeMonster','kitchenMonster','studybreak','sunday', 'monday', 'tuesday', 'wednesday', 'thursday'],
    { 'sunday': 3, 'monday': 'minimal', 'tuesday': 3, 'wednesday': 'minimal', 'thursday': 3, 'studybreak': 'minimal' })
tiny = Person('tiny', 4,
    ['staples','studybreak', 'sunday', 'monday', 'thursday', 'wednesday', 'tuesday'],
    { 'sunday': 4, 'monday': 3.5, 'tuesday': 3.5, 'wednesday': 3.5, 'thursday': 3.5, 'studybreak': 10 })
paola = Person('paola', 2,
    ['sunday','monday','tuesday','wednesday','thursday','studybreak','loungeMonster','staples','kitchenMonster' ],
    { 'sunday': 4.0, 'monday': 5.0, 'tuesday': 5, 'wednesday': 5, 'thursday': 5, 'studybreak': 10 })
andres = Person('andres', 2,
    ['studybreak','staples','loungeMonster','kitchenMonster','sunday','monday','thursday','tuesday','wednesday'],
    { 'sunday': 3, 'monday': 3, 'tuesday': 3.5, 'wednesday': 3, 'thursday': 3.5, 'studybreak': 10 })
silvia = Person('silvia', 2,
    ['loungeMonster','studybreak','kitchenMonster','staples','sunday','monday','tuesday','wednesday','thursday'],
    { 'sunday': 'minimal', 'monday': 'minimal', 'tuesday': 'minimal', 'wednesday': 'minimal', 'thursday': 'minimal', 'studybreak': 10 })
sandy = Person('sandy', 2,
    ['tuesday','thursday','wednesday','monday','sunday'],
    { 'sunday': 3.0, 'monday': 3.0, 'tuesday': 3.50, 'wednesday': 3, 'thursday': 3.5, 'studybreak': 10 })
david = Person('david', 2,
    ['sunday','monday','wednesday','tuesday','thursday'],
    { 'sunday': 3.0, 'monday': 3.0, 'tuesday': 3.50, 'wednesday': 3, 'thursday': 3.5, 'studybreak': 10 })
sara = Person('sara', 2,
    ['sunday','monday','tuesday','wednesday','thursday'],
    { 'sunday': 3.0, 'monday': 3.0, 'tuesday': 3.50, 'wednesday': 3, 'thursday': 3.5, 'studybreak': 10 })
yazmin = Person('yazmin', 0,
    ['tuesday','wednesday','monday','sunday','thursday'],
    { 'sunday': 'minimal', 'monday': 5.0, 'tuesday': 3, 'wednesday': 5, 'thursday': 3, 'studybreak': 10 },
    True)
lisa = Person('lisa', 2,
    ['sunday','monday','wednesday','tuesday','thursday'],
    { 'sunday': 3.0, 'monday': 4.5, 'tuesday': 'minimal', 'wednesday': 4.50, 'thursday': 'minimal', 'studybreak': 10 },
    True)
miguelM = Person('miguelM', 2,
    ['sunday','tuesday','wednesday','monday','thursday'],
    { 'sunday': 3.0, 'monday': 3.25, 'tuesday': 4.25, 'wednesday': 4.25, 'thursday': 4.25, 'studybreak': 10 },
    True)
cesar = Person('cesar', 0,
    ['sunday','thursday','wednesday','tuesday','monday'],
    { 'sunday': 3.0, 'monday': 4.75, 'tuesday': 4.75, 'wednesday': 4.75, 'thursday': 4.5, 'studybreak': 10 },
    True)
yasmin = Person('yasmin', 0,
    ['sunday','tuesday','thursday','monday','wednesday'],
    { 'sunday': 3.25, 'monday': 'minimal', 'tuesday': 4, 'wednesday': 'minimal', 'thursday': 4, 'studybreak': 10 },
    True)
bere = Person('bere', 0,
    ['sunday','monday','wednesday','tuesday','thursday'],
    { 'sunday': 3.75, 'monday': 4.5, 'tuesday': 'minimal', 'wednesday': 'minimal', 'thursday': 5, 'studybreak': 10 },
    True)
victoria = Person('victoria', 0,
    ['tuesday','wednesday','monday','sunday','thursday'],
    { 'sunday': 'minimal', 'monday': 5, 'tuesday': 3, 'wednesday': 5, 'thursday': 'minimal', 'studybreak': 10 },
    True)
navil = Person('navil', 0,
    ['sunday','monday','thursday','tuesday','wednesday'],
    { 'sunday': 3, 'monday': 4.5, 'tuesday': 'minimal', 'wednesday': 'minimal', 'thursday': 'minimal', 'studybreak': 10 },
    True)
matthollie=Pair(matt,hollie)
willyana=Pair(willy,ana)
paolasilvia=Pair(paola,silvia)
people = [anthony,raul,vero,rose,matthollie,ernesto,willyana,deanna,hugo,marcos,tiny,paolasilvia,andres,sandy,david,sara,yazmin,lisa,miguelM,cesar,yasmin,bere,victoria,navil]

numPeople = sum(p.numPeople for p in people)
print numPeople
numNoncooking = numPeople - 24 #TODO: should be 24
numStaples = numNoncooking - 2 # 2 = lounge + kitchen monster
numKitchenMonster = 1
if numStaples > 4:
    numStaples -= 1
    numKitchenMonster += 1

sunday = CookingJob('sunday', people[:])
monday = CookingJob('monday', people[:])
tuesday = CookingJob('tuesday', people[:])
wednesday = CookingJob('wednesday', people[:])
thursday = CookingJob('thursday', people[:])
studybreak = CookingJob('studybreak', people[:], latestArrival=10)
staples = NoncookingJob('staples', people[:], numStaples)
kitchenMonster = NoncookingJob('kitchenMonster', people[:], numKitchenMonster)
loungeMonster = NoncookingJob('loungeMonster',  people[:], 1)
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