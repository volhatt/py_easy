# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 12:28:36 2019

@author: okamene
"""
# columns: Name, Day/Month, Celebrates, Age
BIRTHDAYS = (
    ("James", "9/8", True, 9),
    ("Shawna", "12/6", True, 22),
    ("Amaya", "23/2", False, 8),
    ("Kamal", "29/4", True, 19),
    ("Sam", "16/7", False, 22),
    ("Xan", "14/3", False, 34),
)

#Problem 1 Selebration
# loop through and print "Happy Birthday" if they selebrate)
print("Celebrations:")
print(*[f"Happy Birthday, {person[0]}!\n" for person in BIRTHDAYS if person[2]], sep='')
print(" - " * 20)

#Problem 2: Half birthday 
# calculate half birthday (3 months lager) print name and half birthday
print("Half birthdays:")
def half_bd(bd):
    month = int(bd.split('/')[1])
    if month + 6 > 12:
        month = (month + 6) - 12
    else:
        month += 6
    h_bd = bd[:bd.find('/')+1] + f"{month}"
    return (h_bd)
    
print(*[f"Name is {i[0]} and half birthday is {half_bd(i[1])}\n" for i in BIRTHDAYS], sep="")
print(" - " * 20)

# Problem 3 only school year birthdays
# if their birthday is between Septermber (9) and June (6) print their name
print("School birthdays:")
def sch_bd(bd):
    month = int(bd.split('/')[1])
    if month in range(7,9):
        return True
    
print(*[f"{name[0]} has school birthday\n" for name in BIRTHDAYS if not sch_bd(name[1])], sep='')
print(" - " * 20)

# problem 4 whishing stars
# if person celebrates their BD and their age is 10 or less print out name and 
# as many stars as their age 
print("Starts:")
print(*[f"{person[0]}  {'* ' * person[3] }\n" for person in BIRTHDAYS if person[2] and person[3] < 10], sep='')