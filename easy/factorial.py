#find factorial ( with recursion and loop )

def factorial_rec(num):
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial_rec(num-1))

def factorial_loop(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result


number = 8
print(factorial_rec(number))
print(factorial_loop(number))

number = 4
print(factorial_rec(number))
print(factorial_loop(number))