'''
Question 15
Create a function which reverts a dictionary
(keys become values, values become keys)
'''
def inverse_dict(my_dict):
    result_dict = {}
    for key, value in my_dict.items():
        if not value in result_dict.keys():
            result_dict[value] = []
        result_dict[value].append(key)
    return result_dict
print(inverse_dict({'a': 1, 'b': 2}))
