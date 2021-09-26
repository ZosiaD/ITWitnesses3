a = 0
instr = "please enter your symbols and after each press 'enter', enter 'stop' to stop the program"
print(instr)
c = []
x = []
while c != 'stop':
    c = input()
    x.append(c)

n = 0
for i in x:
    n += 1
print(n-1)
