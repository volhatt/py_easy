import re

# pattern is not at the start of the string
re.search(r'LOG', 'SOME LOGS')
#<re.Match object; span=(5, 8), match='LOG'>

# pattern that is only at the start of the string
re.search(r'^LOG', 'LOGS')
# <re.Match object; span=(0, 3), match='LOG'>

# pattern that is only at the end of the string
re.search(r'LOG$', 'SOME LOGS')
# <re.Match object; span=(5, 8), match='LOG'>

# Match the word 'thing' (not excluding things), but not something or anything.
# Note the \b at the start of the second pattern:
STRING = 'something in the things she shows me'
match = re.search(r'thing', STRING)
# OUTPUT <re.Match object; span=(4, 9), match='thing'>

# STRING
print(match)