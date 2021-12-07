
f = open('06input.txt', 'r')
txt = f.readlines()
import copy as cp
n = 256

ages = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
for number in txt[0].split(','):
    if int(number) in ages: 
        ages[int(number)] += 1
    else:
        ages[int(number)] = 1

new_age = cp.copy(ages)     
for k in range(1,n+1):
    new_new_age = {}
    key_list = list(new_age.keys())
    val_list = list(new_age.values())
    for i in range(0,len(new_age)):
        if key_list[i]==0 and val_list[i]!=0:
            new_new_age[8] = val_list[i]
            if 7 in new_age:
                new_new_age[6] = val_list[i] + new_age[7]
            else:
                new_new_age[6] = val_list[i]
        elif key_list[i]!=0 and val_list[i]!=0:
            if key_list[i]== 7: 
                if 6 not in new_new_age:
                    new_new_age[key_list[i]-1] = val_list[i]
            else:
                new_new_age[key_list[i]-1] = val_list[i]
    new_age = cp.copy(new_new_age)

fish = 0
for i in range(9):
    if i in new_age:
        fish += new_age[i]
print(fish)

            