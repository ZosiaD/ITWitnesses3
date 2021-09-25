'''
Question 14
Write a function that for 2 given dictionaries find their common keys.
'''
def Common_key(dict1, dict2):
    for i in dict1.keys():
        for j in dict2.keys():
            if i == j:
                print(i, 'is the common key')
dict1={'Lesya':200,'Peter':20,'':250,'Shawn':100,'Sam':600}
dict2={'Sam':600,'Oleg':450,'Lesya':200,'George':55,'Stas':20}
Common_key(dict1, dict2)
