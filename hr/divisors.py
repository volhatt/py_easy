"""
    given a natural number calculate sum of all its proper divisors.
    For any number N all of its divisors are always less than and equal
    to N/2 and all prime factors are always less than and equal to sqrt(N)
    So iterate through i till i <= sqrt(N) and for any i if it divides N, 
    then we get 2 divisors i and N/i, continuously add these divisors
    but for some numbers divisors 'i' and 'N/i' wil same, and in this case
    just add only one divisor
"""
import math
# function to calculate sum of all proper
# divisors n -> given natural number

def divSum(n):
    # finale sum of all divisors
    result = 0

    # find all divisors for 'n'
    i = 2
    while i <= (int(math.sqrt(n))):
        # if 'i' is divisor on N
        if (n % i == 0):
            # if both divisors are same then
            # add it only once else add both
            if (i == (n/i)):
                result += i
            else:
                result += (i + n/i)
        i = i + 1

    # add 1 to the result as 1 is also a divisor
    return (result + 1)

"""
    find all divisors and stor in array
"""
def find_divisors(n):
    # array to store divisors
    divs = []

    # list to store half of divisors
    for i in range (1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            divs.append(i)
            # check if divisors are equal
            if n / i == i:
                print(i, 'ine')
            else:
                print(i, 'two')
                #divs.append(int(n/i))
    print(divs, 'end')

print(divSum(36))
print(divSum(6))

find_divisors(6)

'Southeast Asia': {'value': f"12601,{'101274' if TIER == 'prod' else '100084' if TIER='test' else '99025'},1", 'price': '$5,000 (USD)'},
