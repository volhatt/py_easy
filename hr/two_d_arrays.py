"""
Today, we're building on our knowledge of Arrays by adding another dimension. Check out the Tutorial tab for learning materials and an instructional video!

Context
Given a  2D Array, :

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
We define an hourglass in  to be a subset of values with indices falling in this pattern in 's graphical representation:

a b c
  d
e f g
There are  hourglasses in , and an hourglass sum is the sum of an hourglass' values.

Task
Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum.

Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
Sample Output

19
Explanation

 contains the following hourglasses:

1 1 1   1 1 0   1 0 0   0 0 0
  1       0       0       0
1 1 1   1 1 0   1 0 0   0 0 0

0 1 0   1 0 0   0 0 0   0 0 0
  1       1       0       0
0 0 2   0 2 4   2 4 4   4 4 0

1 1 1   1 1 0   1 0 0   0 0 0
  0       2       4       4
0 0 0   0 0 2   0 2 0   2 0 0

0 0 2   0 2 4   2 4 4   4 4 0
  0       0       2       0
0 0 1   0 1 2   1 2 4   2 4 0
The hourglass with the maximum sum () is:

2 4 4
  2
1 2 4
"""
a = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0], 
    [1, 1, 1, 0, 0, 0], 
    [0, 0, 2, 4, 4, 0], 
    [0, 0, 0, 2, 0, 0], 
    [0, 0, 1, 2, 4, 0],
]
# create first element of HG like (a, b, c)
# first is each 3 elements without last 2 in row and last 2 in columns
first = []
for row in a[:-2]:
    for i in range(len(row)-2):
        temp = [row[i], row[i+1], row[i+2]]
        first.append(temp)
first = [([row[i], row[i+1], row[i+2]]) for row in a[:-2] for i in range(len(row)-2)]

#print(first)
print(len(first))

# second is 1 element, starts with second and without last
# to select this we take len array - 2  and len row - 2 (first and last)
second = []
for row in a[1:-1]:
    for i in row[1:-1]:
        temp = [i]
        second.append(temp)
second = [[i] for row in a[1:-1] for i in row[1:-1]]
#print(second)
print(len(second))

# third element is the same as first but starting with a[2:]
third = []
for row in a[2:]:
    for i in range(len(row)-2):
        temp = [row[i], row[i+1], row[i+2]]
        third.append(temp)
third = [[row[i], row[i+1], row[i+2]] for row in a[2:] for i in range(len(row)-2)]

#print(third)
print(len(third))

# now zip 3 row in one element 
#d = list(zip(first, second, third))
#d = [list(a) for a in zip(first, second, third)]
# d = list(map(list, zip(first, second, third)))
# d = lambda first, second, third: [list(n) for n in zip(first, second, third)]
# d(first, second, third)

hourglasses = [[i, j, z] for i, j, z in zip(first, second, third)]
print(f"this is hourglasses {hourglasses}")
#print(len(hourglasses))
# for i in hourglasses:
#     print(i)
def nested_sum(arr):
    return(sum(nested_sum(x) if isinstance(x, list) else x for x in arr))

all_sum = [nested_sum(i) for i in hourglasses]
print(max(all_sum))
