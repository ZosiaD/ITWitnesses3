'''
Question 10
Write a program to find the key of the maximum value in a dictionary.
'''
dic = {'a': 25, 'b': 48, 'c': 90, 'd': 5, 'e': 90}
'maximum value'
max_value = max(dic.values())  
'getting all keys containing the maximum:'
max_keys = [k for k, v in dic.items() if v == max_value]
print(max_value, max_keys)

