f = open('08input.txt', 'r')
txt = f.readlines()

data_In = []
data_Out = []
for line in txt:
    data_Out.append(line.split(' | ')[1].split())

counter = 0    
for line in data_Out:
    for data in line:   
        l = len(data)
        if l in [2, 4, 3, 7]:
            counter += 1
        
print(counter)