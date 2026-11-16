numbers= [1, 2, 3, 4, 5,5]

unique_numbers = set(numbers)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

unique_numbers.add(6)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5, 6}

unique_numbers.remove(3)
print(unique_numbers)  # Output: {1, 2, 4, 5, 6}

unique_numbers.discard(3)
print(unique_numbers)  # Output: {1, 2, 4, 5, 6}

# if you try to remove an element that is not present in the set, it will raise a KeyError. 
# To avoid this, you can use the discard() method, which does not raise an error if the element is not found.