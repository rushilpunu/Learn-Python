num_int = 123  # integer type
num_flo = 1.23  # float type

num_new = num_int + num_flo

print("Value of num_new:", num_new)
print("datatype of num_new:", type(num_new))


# Shown Below Is what the Python Interpreter cannot work out.
#It will be in a comment form to stop it from messing with the interpreter when we run this script.

"""
num_int = 123     # int type
num_str = "456"   # str type

print(num_int+num_str)
"""

#Explicit Conversion:
num_int = 123  # int type
num_str = "456"  # str type

# explicitly converted to int type
num_str = int(num_str)

print(num_int+num_str)
