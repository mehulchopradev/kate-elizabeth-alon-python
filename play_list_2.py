marks = [5, 6, 3, 4, 7, 8, 10, 9, 4]

# get a new list consisting of odd marks from the marks list
# filtering
''' ol = []
for mark in marks:
    if mark % 2:
        ol.append(mark) '''

# Pre requisite - Requiring a new list
# for comprehensions
ol = [ele for ele in marks if ele % 2]
print(ol)

# get a new list consisting of even elements more than 4 from the marks list
# filtering
el = [ele for ele in marks if ele % 2 == 0 and ele > 4]
print(el)

# get a new list consisting of all the marks from the marks list; but deducted by 1
# mapping
deducted_marks = [ele - 1 for ele in marks]
print(deducted_marks)

# get a new list consisting of even elements more than 4 from the marks list,
# where every element found must be squared up
# filtering + mapping together

nl = [ele ** 2 for ele in marks if ele % 2 == 0 and ele > 4]
print(nl)