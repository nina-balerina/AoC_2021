f = open('07input.txt', 'r')
data = f.readlines()

positions = []
for position in data[0].split(','):
    positions.append(int(position))

fuel_1 = [] 
fuel_2 = []
for i in range(max(positions)+1):
    fuel_1.append(0)
    fuel_2.append(0)
    for position in positions:
        fuel_1[i] = fuel_1[i] + abs(i-position)
        fuel_2[i] = fuel_2[i] + (abs(i-position)*(abs(i-position)+1))//2
    
print(min(fuel_1))
print(min(fuel_2))