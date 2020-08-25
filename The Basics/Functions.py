
def print_lines():
  print("I am line1.")
  print("I am line2.")


# function call
print_lines()


def add_numbers(a, b):
  sum = a + b
  print(sum)


add_numbers(4, 5)

# Output: 9


def add_numbers(a, b):
  sum = a + b
  return sum


result = add_numbers(4, 5)
print(result)

# Output: 9
