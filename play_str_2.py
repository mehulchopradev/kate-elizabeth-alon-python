msg = 'hello to all hel.lo world to all'

# in operator (membership operator)
print('world' in msg)
print('night' in msg)

# access the character at position 4 in the str
# left to right positive indexing
print(msg[4])
print(msg[0])

# access the second last character from the str
# right to left negative indexing
print(msg[-2])
print(msg[-6])

# extract 'all. hello' from the main msg str
print(msg[9:19])

print(msg[0:8])
print(msg[:8]) # if start position is 0, u can drop it off

# extract a substring which is after a period in the msg str
i = msg.find('.')
if i > -1:
    print(msg[i+1:]) # skipping the end index, means it will give till the end of the string

# create a clone of the str msg
m = msg[:] # start is assumed to be 0 and end is assumed to be the end of the str. Default step size = 1
print(m)

re = msg[::-1] # -1 indicate right to left reading
print(re)

print(msg[::2])
