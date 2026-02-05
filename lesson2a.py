# python lists
# a list is a collection of items that are ordered in a certain way
# the items of a list are stored inside of indexes.

cars=["BMW", "Benze", "Range", "mercedes", "Probox", "Axio", ]

print(cars)
print(type(cars))

# Accessing items of a list.
print(cars[0])
print("the car on index four is:", cars[4])

# List slicing-this is creating a list from a bigger list.
print(cars[4:])
print(cars[0:3])
print(cars[:4])

# list-mutability
# we use the function append to add an item at the end of a list
cars.append("marcus")
print(cars)
# we use pop to remove an item at the end of a list
cars.pop()
print(cars)
# we can use an index to add items to a list
cars[5]="pajero"
print(cars)
# we use sort function to sort out items in alphabetical order
cars.sort()
print(cars)
# this is how we do z-a
cars.sort(reverse = True)