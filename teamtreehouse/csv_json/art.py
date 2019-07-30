import json

with open('E:\\code\\test\\jsonfile.json') as artfile:
	art = json.load(artfile)
	print(art['menu'])


me = {'first_name': 'Olga', 'last_name': 'Love', 'topic': 'Python'}
craig = {'first_name': 'Craig', 'last_name': 'Test', 'topic': 'Java'}

with open('E:\\code\\test\\teacher.json', 'a') as teacherfile:
	json.dump([me, craig], teacherfile)