print ('Preston Foote')

cars = ['Ford', 'Chrysler', 'Dodge', 'Ram', 'Jeep', 'Chevy', 'GMC',]

cars.append('Buick')

print (cars)

x = len(cars)

print (x)

print (cars)

z = cars[4]

print (z)

print (cars)

cars.insert(3, 'Toyota')

print (cars)

cars.pop(5)

print (cars)

cars.sort()

print (cars)

cars.sort(reverse=True)

print (cars)

length = len(cars)

array_string = 'The length of my array is '

txt = array_string

print (txt.format(length))