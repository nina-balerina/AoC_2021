
f = open('02input.txt', 'r')
txt = f.readlines()

dirs = []
steps = []
for line in txt:
    dirs.append(line.split(' ')[0])
    steps.append(int(line.split(' ')[1]))
    
d = 0
p = 0
aim = 0
d2 = 0
for i in range(0,len(dirs)):
    if dirs[i]=='forward':
        p = p+steps[i]
        d2 = d2+aim*steps[i]
    elif dirs[i]=='up':
        d = d-steps[i]
        aim = aim-steps[i]
    elif dirs[i]=='down':
        d = d+steps[i]
        aim = aim+steps[i]
           
print(d*p)
print(d2*p)
