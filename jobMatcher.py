import copy
 
jobprefers = {
'sunday':   ['amber', 'lisa', 'ana','matt', 'rob', 'kyle', 'kevin', 'abi', 'amy', 'jack,' 'hope', 'mike'],
'monday':  ['abi', 'kevin', 'rob', 'matt','amy', 'amber', 'lisa', 'kyle', 'jack','ana', 'hope', 'mike'],
'tuesday':  ['rob', 'hope', 'abi', 'matt','lisa', 'jack', 'kevin', 'kyle', 'ana', 'amber', 'amy', 'mike'],
'wednesday':  ['hope', 'kevin', 'abi', 'lisa', 'jack','ana', 'kyle', 'amy','matt', 'mike', 'rob', 'amber'],
'thursday':  ['amy', 'kyle', 'lisa', 'mike', 'hope', 'kevin', 'amber','matt', 'ana', 'jack', 'rob', 'abi'],
'studybreak':  ['jack','amy', 'kyle', 'lisa', 'amber', 'ana', 'rob', 'abi', 'matt', 'mike', 'hope', 'kevin']}
personprefers = {
'abi': ['tuesday', 'monday', 'thursday', 'sunday'],
'ana': ['tuesday', 'monday', 'wednesday', 'thursday', 'sunday'],
'rob': ['tuesday', 'sunday', 'wednesday', 'monday', 'thursday'],
'lisa': ['wednesday', 'monday', 'thursday', 'tuesday', 'sunday'],
'kevin': ['thursday', 'monday', 'wednesday', 'sunday', 'tuesday'],
'kyle': ['tuesday', 'monday', 'sunday', 'studybreak','thursday', 'wednesday'],
'mike': ['tuesday', 'monday', 'studybreak','wednesday', 'sunday', 'thursday'],
'hope': ['tuesday', 'monday', 'thursday', 'sunday', 'wednesday'],
'amy': ['wednesday', 'tuesday', 'monday', 'sunday'],
'amber': ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday'],
'matt': ['wednesday','studybreak', 'tuesday', 'monday', 'sunday'],
'jack': ['studybreak', 'thursday','sunday', 'monday', 'tuesday', 'wednesday']}

jobs = sorted(jobprefers.keys())

people = sorted(personprefers.keys())
 
def matchmaker():
    jobsfree = jobs[:]
    jobsfree.extend(jobs[:]) # copy twice since they can have 2 wives
    engaged  = {}

    jobprefers2 = copy.deepcopy(jobprefers)
    personprefers2 = copy.deepcopy(personprefers)
    while jobsfree:
        job = jobsfree.pop(0)
        joblist = jobprefers2[job]
        print joblist
        person = joblist.pop(0)

        if job in personprefers2[person]:
            old_job = engaged.get(person)
            if not old_job:
                # She's free
                engaged[person] = job
                print("  %s and %s" % (job, person))
            else:
                # Proposes to an engaged person
                personlist = personprefers2[person]
                jobRank = personlist.index(job) if job in personlist else -1
                if personlist.index(old_job) > jobRank:
                    # She prefers new job
                    engaged[person] = job
                    print("  %s dumped %s for %s" % (person, old_job, job))
                    if jobprefers2[old_job]:
                        # Ex has more girls to try
                        jobsfree.append(old_job)
                else:
                    # She prefers old_job
                    if joblist:
                        # Look again
                        jobsfree.append(job)
        else:
            if joblist:
               # Look again
               jobsfree.append(job)
    return engaged
 
 
print('\nEngagejobsts:')
engaged = matchmaker()
 
print('\nCouples:')
print('  ' + ',\n  '.join('%s is matched to %s' % couple
                          for couple in sorted(engaged.items())))
print()
