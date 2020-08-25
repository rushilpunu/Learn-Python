# set of integers
my_set = {1, 2, 3}
print(my_set)

# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)

# set of integers
my_set = {1, 2, 3}

my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

my_set.add(2)
print(my_set)  # Output: {1, 2, 3, 4}

my_set.update([3, 4, 5])
print(my_set)  # Output: {1, 2, 3, 4, 5}

my_set.remove(4)
print(my_set)  # Output: {1, 2, 3, 5}

A = {1, 2, 3}
B = {2, 3, 4, 5}

# Equivalent to A.union(B)
# Also equivalent to B.union(A)
print(A | B)  # Output: {1, 2, 3, 4, 5}

# Equivalent to A.intersection(B)
# Also equivalent to B.intersection(A)
print(A & B)  # Output: {2, 3}

# Set Difference
print(A - B)  # Output: {1}

# Set Symmetric Difference
print(A ^ B)  # Output: {1, 4, 5}
