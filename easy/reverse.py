__author__= 'okameneva'

# simpliest way array[::-1]

# example 1
def rev1(arr):
    """ func takes array or string and return reversed version """
    rev = []
    for i in arr:
        rev.insert(0, i)
    return rev if type(arr) == list else ''.join(rev)

def rev2(arr):
    return [x for x in arr[::-1]]


#POC
ar = [1, 2, 3, 4, '5']
s = "Lazy Fox"
print(rev1(ar))
print(rev1(s))

print(rev2(ar))
