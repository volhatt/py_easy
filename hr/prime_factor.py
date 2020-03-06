# Python script to found :
# prime factors of the number
# divisors of the number

import math

# function that prints all prime factors of a given number
def primeFactors(n):
    """
        Function return array with all prime factors of a given number.
    """
    # empty array to store prime factors
    prime_factors = []
    # 1. while n divisible by 2 store 2 as prime factor and divide n by 2
    while n % 2 == 0:
        prime_factors.append(2)
        n = n / 2
        # print(n)
    # now n should be odd as it is not dividable by 2 
    # now check numbers from 3 to square root of a given number n with step 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        # while i divides n , store i and divide n by i
        while n % i == 0:
            prime_factors.append(i)
            n = n / i
            # print(n)
    # check if last n is a prime number and add it to array
    # we already knows that i < math.sqrt(n) , otherwise check if number is prime should include range ( 2 , math.sqrt(n))
    """ eg. how to check if number is a prime
    def is_prime(n):
	    if(n > 1):
		    for i in range(2, int(math.sqrt(n))):
			    if n % 1 == 0:
				    return False
	    if n <= 1:
		    return False
	    else:
		    return True
    """
    if n > 2:
        prime_factors.append(int(n))
    

    return prime_factors

def all_divisors(n):
    pass



print(primeFactors(100))
# output
# [2, 2, 5, 5]
print(primeFactors(6542312))
# output
# [2, 2, 2, 7, 116827]
