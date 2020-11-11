msg = 'Good morning'

u = msg.upper()
print(u)

t = msg.title()
print(t)

fullname = 'mehul chopra'
c = fullname.capitalize()
print(c)

r = msg.replace('morning', 'night')
print(r)

greeting = 'hello to all. How many have finished writing hello world'
print(greeting.count('hello'))

print(msg.startswith('Good'))
print(msg.startswith('Bad'))

print(msg.endswith('morning'))

print(msg.find('ood')) # returns the position of the starting character

# a string is like a sequence of characters joined up together
# first character has a position no 0
# second character has position no 1....
print(msg.find('morning'))

print(msg.find('night')) # -1 indicating not found in the entire string

student_data = '         mehul,56,m,90    '
st = student_data.strip() # removes the leading and trailing spaces from an str object
print(st)
print(student_data)

# length of the string
print(len(msg)) # no of characters that are there in the msg string

# directly feed my str data to a forloop in python
for v in msg:
    print(v) # v represents the character from a str

s1 = 'mehul25'
print(s1.isalpha())
print(s1.isalnum())
print(s1.isnumeric())

s2 = '34'
print(s2.isnumeric())

# an str object is a immmutable object
