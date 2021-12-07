f = open('07input.txt', 'r')
data = f.readlines()

positions = []
for position in data[0].split(','):
    positions.append(int(position))

fuel_1 = [] 
fuel_2 = []
for i in range(max(positions)+1):
    fuel_loc_1 = 0
    fuel_loc_2 = 0
    for position in positions:
        fuel_loc_1 = fuel_loc_1 + abs(i-position)
        fuel_loc_2 = fuel_loc_2 + (abs(i-position)*(abs(i-position)+1))/2
    fuel_1.append(fuel_loc_1)
    fuel_2.append(int(fuel_loc_2))
    
print(min(fuel_1))
print(min(fuel_2))