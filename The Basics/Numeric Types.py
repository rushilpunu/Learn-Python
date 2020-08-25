# Output: <class 'int'>
print(type(5))

# Output: <class 'float'>
print(type(5.0))

c = 5 + 3j

# Output: <class 'complex'>
print(type(c))

#Strings Are IMMUTABLE 
# all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)


str = 'programiz'
print('str = ', str)

print('str[0] = ', str[0])  # Output: p

print('str[-1] = ', str[-1])  # Output: z

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])  # Output: rogr

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])  # Output: am