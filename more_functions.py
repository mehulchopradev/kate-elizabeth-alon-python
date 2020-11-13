# Variable number of inputs (0 to n)
def myadd(*args):
    # print(args) # tuple
    sum = 0
    for arg in args:
        sum += arg
    return sum

# tuple packing / positional arguments packing
print(myadd()) # 0
print(myadd(1, 3, 4)) # 8
print(myadd(5, 6, 4, 3, 7, 8, 4)) # 37




def perimeter_rectangle(length, breadth):
    return 2 * (length + breadth)

stats = (7, 4)
# print(perimeter_rectangle(stats[0], stats[1]))
print(perimeter_rectangle(*stats)) # tuple unpacking/positional arguments unpacking



def area_rectangle(**args):
    # print(args) # dict
    return args['length'] * args['breadth']


# print(area_rectangle(6, 4))
print(area_rectangle(length=6, breadth=4))
print(area_rectangle(breadth=4, length=6))
# print(area_rectangle(len=45, bre=34)) # this will give an error

stats_map = {'breadth': 5.4, 'length': 6.5}

# print(perimeter_rectangle(stats_map['length'], stats_map['breadth']))

print(perimeter_rectangle(**stats_map))