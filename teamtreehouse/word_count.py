# transform string into Dict that every word is a key and
# value is how many times word occurs in this string
# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to makdef word_count(s):
def word_count(s):
	# transform string into list
	list_from_string = s.split()
	list_for_dict = []
	    
	# prepare list wehre every element is tuple with pair for dictionary
	for item in list_from_string:
		if item not in list_for_dict:
			list_for_dict.append((item.lower(), list_from_string.count(item)))
	new_dict = { key : value for key, value in list_for_dict }
	return new_dict
