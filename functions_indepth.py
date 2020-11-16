from math import pi

def perimeter_circle(radius):
    return pi * radius ** 2

radius = 5

print(type(radius)) # class int
print(type(perimeter_circle)) # class function

# functions in python are objects
# treated like regular values in python like a str, int, float,.... function

# perimeter_circle -> callable variable
# radius -> non callable variable
print(perimeter_circle(radius))
# radius() # radius is not callable

# functional programming

def abc():
    i = 45 # i(abc) -> (int)
    j = 100 # j(abc) -> int
    k = 30 # k (abc) -> int

    # xyz(abc) -> (function)
    def xyz():
        y = 56 # y(xyz) -> int

        # inner function can access the enclosing function variables
        print(y + i) # 101

        j = 6 # j(xyz) -> int
        print(j ** 2)  # 36

        # k = k + 10 # this will not work
        # print(k) 
    
    xyz()
    print(i) # 45
    print(j) # 100

abc()
# xyz() # error since xyz function is only available within the scopeof the abc()

def rty():
    g = 90 # g (rty) -> int

    # pwe (rty) -> function
    def pwe(u):
        '''
        Inner function can access the enclosing function variables.
        The program maintains enclosing scope variables even after the
        enclosing function has returned. This is called as Closures
        '''
        return (g + 10) ** u
    
    # a function can return another function
    return pwe

p = rty()
# p (entire module) -> function
# p (callable variable)

print(p(5)) # 10000000000

# asd (entire module) -> function
def asd(f):
    # f (asd) -> function
    i = 5
    return f(i) + 10

# toi (entire module) -> function
def toi(r):
    return r ** 2

# a function can be passed as a parameter to another function
# callback functions
print(asd(toi))