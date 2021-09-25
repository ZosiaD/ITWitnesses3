'''
Question 12
Write a program that generates the 26-line block of letters partially
shown below. Use a loop containing one or two print statements.

abcdefghijklmnopqrstuvwxyz

bcdefghijklmnopqrstuvwxyza

cdefghijklmnopqrstuvwxyzab

'''
from collections import deque
from string import ascii_lowercase 
d = deque(ascii_lowercase)
for _ in range(len(d)):
    print(*d, '\n', sep="")
    d.rotate(-1)
