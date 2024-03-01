# numbres = list(range(20))
# print(numbres[::3])

# List unpacking
# numbers = [1, 2, 3, 4, 5, 5, 7]
# first, second, *others = numbers

# print(first, second)
# print(others)


# Loop over list
# numbers = [1, 2, 3, 4, 5, 5, 7]
# for index, number in enumerate(numbers):
#     print(index, number)

# letters = ["a", "b", "c"]
# Add
# letters.append("d")
# letters.insert(2, "bc")

# Remove
# letters.pop(3)
# letters.remove("bc")
# del letters[0:1]
# letters.clear()
# print(letters)

# Finding item in a list
# print(letters.count("d"))
# if "d" in letters:
#     print(letters.index("d"))

# Sorting list
# numbers = [1, 21, 13, 74, 5, 5, 7]
# # numbers.sort(reverse=True)
# print(sorted(numbers, reverse=True))
# print(numbers)

# List of Tuples
items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
]

# def sort_item(item):
#     return item[1]


# items.sort(key=sort_item)
# print(items)

# Using lamda function
# items.sort(key=lambda item: item[1])
# print(items)

# Tramsform this tuple list into a list of prices
# prices = []
# for item in items:
#     prices.append(item[1])

# print(prices)

# Better way to rewrite the above code using MAP
prices = list(map(lambda item: item[1], items))
print(prices)