pointers = [5, 6, 4, 5, 7, 8, 2, 3, 10, 5, 6, 7]

# get a new list of only the even pointers more than 5 from the pointers list
# filtering

''' def even_more_than_5(element):
    return element % 2 == 0 and element > 5

# filter => higher order function
# even_more_than_5 => lower order function (callback function)
evens = list(filter(even_more_than_5, pointers)) '''

# Pre requisite : Lower order function must have only one statement
# Lambda expressions in python - Define ur function inline - at the line of function call

evens = list(filter(lambda element: element % 2 == 0 and element > 5, pointers))
print(evens)

# get a new list of pointers deducted by 1 from the pointers list
# mapping

''' def deduct_by_one(element):
    return element - 1

d = list(map(deduct_by_one, pointers)) '''

d = list(map(lambda element: element - 1, pointers))
print(d)