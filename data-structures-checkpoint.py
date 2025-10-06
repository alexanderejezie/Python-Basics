# Question 1 => Multiply all items in a list
sample_list = [2, 3, 6]

result = 1
for item in sample_list:
    result *= item

print("Result =", result)
# Output: 36

_______________________________________________________________________________________________________________________________________________________________________________________

# Question 2 => Sort a list of tuples by the last element in each tuple
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# Sort using a lambda function to access the last element of each tuple
sample_list.sort(key=lambda x: x[-1])

print("Expected result:", sample_list)
# Output: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

_______________________________________________________________________________________________________________________________________________________________________________________

# Question 3 => Combine two dictionaries by adding values for common keys
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

# Create a new dictionary that combines both
result = {}

for key in d1.keys() | d2.keys():  # union of all keys
    result[key] = d1.get(key, 0) + d2.get(key, 0)

print("Expected result:", result)
# Output: {'a': 400, 'b': 400, 'c': 300, 'd': 400}


_______________________________________________________________________________________________________________________________________________________________________________________

# Question 4 => Generate a dictionary where keys are numbers and values are squares
n = int(input("Enter a number: "))  # Example: 8

square_dict = {i: i * i for i in range(1, n + 1)}

print("Result:", square_dict)
# Output for n = 8 → {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

_______________________________________________________________________________________________________________________________________________________________________________________

# Question 5 => Sort a tuple by its float element in descending order
sample_list = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

# Sort by converting the second element to float, in reverse order
sorted_list = sorted(sample_list, key=lambda x: float(x[1]), reverse=True)

print("Expected result:", sorted_list)
# Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]
