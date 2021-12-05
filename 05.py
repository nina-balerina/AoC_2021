
f = open('05input.txt', 'r')
txt = f.readlines()
import numpy as np
import copy as cp

# input

x1 = []
x2 = []
y1 = []
y2 = []
for line in txt:
    x1.append( int(line.split(' -> ')[0].split(',')[0]) )
    y1.append( int(line.split(' -> ')[0].split(',')[1]) )
    x2.append( int(line.split(' -> ')[1].split(',')[0]) )
    y2.append( int(line.split(' -> ')[1].split(',')[1]) )

# calculation

x_max = max( max(x1), max(x2))
y_max = max( max(y1), max(y2))
field = np.zeros([x_max+1, y_max + 1, 2])
field2 = cp.copy(field)
for i in range(len(x1)):
    if x1[i]==x2[i]:
        field[x1[i], min(y1[i], y2[i]):(max(y1[i], y2[i])+1), :] += 1
    elif y1[i]==y2[i]:
        field[min(x1[i], x2[i]):(max(x1[i], x2[i])+1), y1[i], :] += 1
    elif abs(x2[i]-x1[i])==abs(y2[i]-y1[i]):
        derx = x2[i] - x1[i]
        dery = y2[i] - y1[i]
        for j in range(x1[i], (x2[i] + 1*np.sign(derx)), np.sign(derx)):
            field[j, y1[i]+abs(j-x1[i])*np.sign(dery), 1] += 1 
        
              
print( sum(sum(field[:, :, 0]>1)) )
print( sum(sum(field[:, :, 1]>1)) )
