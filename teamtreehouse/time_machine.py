# Write a function named time_machine that takes an integer and
# a string of "minutes", "hours", "days", or "years". This describes a
# timedelta. Return a datetime that is the timedelta's duration from
# the starter datetime.

import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

# Remember, you can't set "years" on a timedelta!
# Consider a year to be 365 days.

## Example
# time_machine(5, "minutes") => datetime(2015, 10, 21, 16, 34)

def time_machine(num, value):
	delta_val = ''
	value = value[:3]
	if value == 'min':
		delta_val = 'minutes'
	elif value == 'hou':
		delta_val = 'hours'
	elif value == 'day':
		delta_val = 'days'
	elif value == 'yea':
		num = num * 365
		delta_val = 'days'
	#print(num, delta_val)
	return starter + datetime.timedelta(**{delta_val:num})
