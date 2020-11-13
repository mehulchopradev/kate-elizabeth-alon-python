# empty list
el = []
print(type(el))
print(el)

# list of cars that I have
cars = ['audi', 'porshe']

# list of marks scored in the class
marks = [5, 6, 4, 5, 8, 8, 10, 9, 3, 6]

# length of the list
print(len(marks))

# list sequence of elements
for mark in marks:
    print(mark)

# list sequence of elements where first element is at position 0, second element position 1, .....
print(marks[2])
print(marks[0])
print(marks[-1])

# sublist from the larger list
l = marks[0:4]
print(l)
print(marks[:4]) # default start index will be 0
print(marks[-4:]) # defalt end index will be the end of the list

# update the marks scored by the second last student in the class
marks[-2] = 7

marks[0] = 10
print(marks)

# add a new car at the end of the list
cars.append('mercedes')
print(cars)

# add two more cars at the end of the list
cars.extend(['i10', 'i20'])
print(cars)

# remove a car from the end of the list
print(cars.pop())
print(cars)

print(cars.pop())
print(cars)

# add element anywhere
cars.insert(1, 'bmw')
print(cars)

# remove element from anywhere
print(cars.pop(2))
print(cars)

# remove audi from the list
cars.remove('audi')
print(cars)

# find out whether the list has bmw or no
print('bmw' in cars) # in - membership operator
print('audi' in cars)

# count the number of occurences of an element in the list
print(marks.count(8))
print(marks.count(0))
print(marks.count(10))

marks.sort() # sorts the list in place in the ascending order
print(marks)

marks.sort(reverse=True) # sorts the list in place in the descending order
print(marks)

# reverses the list
marks.reverse()
print(marks)




