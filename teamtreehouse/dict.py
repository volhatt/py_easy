some_dict = {
    'Kenneth Love': ['Python Basics', 'Python Collections'],
    'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
    'Olga Kameneva': ['Do nothing', 'Love everybody', 'Hawaii forever']
    }
# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here.
def num_teachers( some ):
    return len(some)

# That one wasn't too bad, right? Let's try something a bit more challenging.
# Create a new function named num_courses that will receive the same dictionary as its only argument.
# The function should return the total number of courses for all of the teachers.

def num_courses ( some_dict ):
    c_number = 0
    for value in some_dict.values():
        c_number += len(value)
    return c_number

# new function named courses that wil take the dictionary of teachers and courses.
# should return a single list of all of the available courses in the dictionary.
# No teachers, just course names!

def courses ( some_dict ):
    courses = []
    for value in some_dict.values():
        for item in value:
            courses.append(item)
    return courses


# Create a function named most_courses that takes our good ol' teacher dictionary.
# most_courses should return the name of the teacher with the most courses. You might need
# to hold onto some sort of max count variable.
def most_courses( some_dict):
    best_teacher = ''
    courses = 0
    for key, value in some_dict.items():
        if len(value) > courses:
            best_teacher = key
            courses = len(value)
    # here should be check if some teachers has the same number of classes
    return best_teacher

# create a function named stats and it'll take our teacher dictionary as its only argument.
# stats should return a list of lists where the first item in each inner list is the teacher's
# name and the second item is the number of courses that teacher has. For example,
# it might return: [["Kenneth Love", 5], ["Craig Dennis", 10]]

def stats (some_dict):
    teacher_list = []
    for key, value in some_dict.items():
        teacher_list.append([key, len(value)])
    return teacher_list

