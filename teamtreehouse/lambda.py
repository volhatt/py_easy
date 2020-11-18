from functools import reduce
from operator import add

##### reduce ####

prices = [
    (6.99, 5),
    (2.94, 15),
    (156.99, 2),
    (99.99, 4),
    (1.82, 102)
]


def product_sales(pr):
    return pr[0] * pr[1]

total = reduce(add, map(product_sales, prices))
print(total)
"""
Finish the prereqs function so that it recursively finds all of the prerequisite course titles in courses (like "Object-Oriented Python" is a prerequisite for "Django Basics"). You should add() the title of the prerequisite to the pres set and then call prereqs again with the child courses.
In the end, return the prereqs set.
"""
courses = {'count': 2,
           'title': 'Django Basics',
           'prereqs': [{'count': 3,
                        'title': 'Object-Oriented Python',
                        'prereqs': [{'count': 1,
                                     'title': 'Python Collections',
                                     'prereqs': [{'count': 0,
                                                  'title': 'Python Basics',
                                                  'prereqs': []}]},
                                    {'count': 0,
                                     'title': 'Python Basics',
                                     'prereqs': []},
                                    {'count': 0,
                                     'title': 'Setting Up a Local Python Environment',
                                     'prereqs': []}]},
                       {'count': 0,
                        'title': 'Flask Basics',
                        'prereqs': []}]}


def prereqs(data, pres=None):
    # press if press has data or set() if press is emty
    pres = pres or set()
    # loop through eacth item in the prereqs property
    # for each 'prereqs' add its titile to the press
    # recursion
    for item in data['prereqs']:
        pres.add(item['title'])
        prereqs(item, pres)
    return pres

print(prereqs(courses))

##### lambda
total = reduce(lambda x, y: x + y, [b for b in prices])
print(total)

"""Use reduce() and a lambda to find the longest string in strings. Save this value in the variable longest."""

strings = [
    "Do not take life too seriously. You will never get out of it alive.",
    "My fake plants died because I did not pretend to water them.",
    "A day without sunshine is like, you know, night.",
    "Get your facts first, then you can distort them as you please.",
    "My grandmother started walking five miles a day when she was sixty. She's ninety-seven know and we don't know where she is.",
    "Life is hard. After all, it kills you.",
    "All my life, I always wanted to be somebody. Now I see that I should have been more specific.",
    "Everyone's like, 'overnight sensation.' It's not overnight. It's years of hard work.",
]

longest = reduce(lambda a, b: a if len(a) > len(b) else b, strings)
print(longest)
