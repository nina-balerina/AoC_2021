
f = open('06input.txt', 'r')
txt = f.readlines()
import copy as cp
n = 80

ages = {}
youngs = {}
fish = 0
for number in txt[0].split(','):
    fish += 1
    ages[fish] = int(number)
    youngs[fish] = 0

new_age = cp.copy(ages) 
new_youngs = cp.copy(youngs)      
for k in range(n):
    for i in range(1,len(new_age)+1):
        if new_youngs[i]==0:
            if new_age[i]==0:
                fish += 1
                new_age[fish] = 8
                new_youngs[fish] = 1
            if new_age[i]>0:
                new_age[i] -= 1
            else:
                new_age[i] = 6
        else:
            new_youngs[i] = 0
            new_age[i] -= 1

print(len(new_age))
            