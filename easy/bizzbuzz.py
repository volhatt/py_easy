# bizz buzz with list and set comprehension

# eg 1 - easy !
best_fizzbuzz = [ 'Fizzbuzz' if num % 15 == 0 else
	     'Fizz' if num % 3 == 0 else
	     'Buzz' if num % 5 == 0 else
	     num for num in range (1, 101) ]

# output
# [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 
# 13, 14, 'Fizzbuzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz',
# 'Buzz', 26, 'Fizz', 28, 29, 'Fizzbuzz', 31, 32, 'Fizz', 34, 'Buzz',
# 'Fizz', 37, 38, 'Fizz', 'Buzz', 41, 'Fizz', 43, 44, 'Fizzbuzz', 46,
# 47, 'Fizz', 49, 'Buzz', 'Fizz', 52, 53, 'Fizz', 'Buzz', 56, 'Fizz', 58,
# 59, 'Fizzbuzz', 61, 62, 'Fizz', 64, 'Buzz', 'Fizz', 67, 68, 'Fizz',
# 'Buzz', 71, 'Fizz', 73, 74, 'Fizzbuzz', 76, 77, 'Fizz', 79, 'Buzz',
# 'Fizz', 82, 83, 'Fizz', 'Buzz', 86, 'Fizz', 88, 89, 'Fizzbuzz',
# 91, 92, 'Fizz', 94, 'Buzz', 'Fizz', 97, 98, 'Fizz', 'Buzz']

# eg 2 
def fizz_or_buzz(num):
    if num % 15 == 0:
        return 'Fizzbuzz' 
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz' 
    else:
        return num

fizzbuzz = [fizz_or_buzz(num) for num in range (1, 101)]



# eg 3 - is not finished
total_numbers = range(1, 101)

fizzbuzzes = {
    'fizz': [n for n in total_numbers if n % 3 == 0],
    'buzz': [n for n in total_numbers if n % 7 == 0]
}

# {'fizz': [3, 6, 9, 12, 15, 18, 21], 'buzz': [7, 14, 21]}
fb = { key: set(value) for key, value in fizzbuzzes.items() }
# {'fizz': {3, 6, 9, 12, 15, 18, 21}, 'buzz': {21, 14, 7}}

fb['fizzbuzz'] = {n for n in fb['fizz'].intersection(fb['buzz'])}
# {'fizz': {3, 6, 9, 12, 15, 18, 21}, 'buzz': {21, 14, 7}, 'fizzbuzz': {21}}