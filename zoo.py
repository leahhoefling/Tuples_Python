# Create a tuple named zoo that contains your favorite animals.
zoo = ("Cheetah", "Shark", "Hyena", "Lion", "Penguin", "Warthog")

# Find one of your animals using the .index(value) method on the tuple.
print(zoo.index("Lion"))

# Determine if an animal is in your tuple by using value in tuple.
print(zoo[1])

# Create a variable for each of the animals in your tuple with this cool feature of Python.

# # example
# (lizard, fox, mammoth) = zoo
# print(lizard)

# Convert your tuple into a list.
zoo_list = list(zoo)

# Use extend() to add three more animals to your zoo.
zoo_list.extend(["Dolphin", "Red Panda"])

# Convert the list back into a tuple.
zoo_tup = tuple(zoo_list)
