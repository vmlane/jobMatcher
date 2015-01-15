from person import Person
from job import Job

jobprefers = {
'sunday':   ['amber', 'lisa', 'ana','matt', 'rob', 'kyle', 'kevin', 'abi', 'amy', 'jack', 'hope', 'mike'],
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

prefs = ['amber', 'lisa', 'ana','matt', 'rob', 'kyle', 'kevin', 'abi', 'amy', 'jack', 'hope', 'mike']
sunday = Job('sunday', ['amber', 'lisa', 'ana','matt', 'rob', 'kyle', 'kevin', 'abi', 'amy', 'jack', 'hope', 'mike'])
print sunday.isFree()
print sunday.getPrefs() == prefs
print sunday.getPersonRank('rob') == 4
print sunday.pop() == 'amber'
sunday.match(sunday.pop())
print sunday.matches == ['lisa']
print sunday.isFree() == True
sunday.match(sunday.pop())
print sunday.isFree() == False
print sunday.getMatchRank() == 2
sunday.unmatch('lisa')
print sunday.matches == ['ana']
print sunday.getPrefs() == prefs

mikePrefs =  ['tuesday', 'monday', 'studybreak','wednesday', 'sunday', 'thursday']
mike = Person('mike', mikePrefs)
print mike.isFree() == True
print mike.getPrefs() == mikePrefs
print mike.getJobRank('thursday') == 5
print mike.getJobRank('fakeday') == float("inf")
print mike.pop().name == 'tuesday'
mike.match(mike.pop())
print mike.getMatchRank() == 1
print mike.isFree() == False
mike.unmatch()
print mike.isFree()
