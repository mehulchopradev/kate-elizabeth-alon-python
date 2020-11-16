print('Program starts...')

i = input('Enter n: ')

try:
    n = int(i) # n (entire module)
except ValueError:
    # handle the error
    print('Please enter integer values')
else:
    # will execute when there is no error thrown in the corresponding try block
    print('Odd') if n % 2 else print('Even')

print('Program ends!')

# try - except
# try - except - else
# try - except - except - else