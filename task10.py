'''
Question 10
Write a program to find the key of the maximum value in a dictionary.
'''
dic = {'a': 25, 'b': 48, 'c': 90, 'd': 5, 'e':90}
max_value = max(dic.values())  # maximum value
max_keys = [k for k, v in dic.items() if v == max_value] # getting all keys containing the 'maximum'
print(max_value, max_keys)
