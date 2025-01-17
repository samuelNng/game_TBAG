from room import Room

kitchen = Room("kitchen")
ballroom = Room("ballroom")
dining_hall = Room("dining_hall")

#print(kitchen.name)
kitchen.set_description("A dank and dirty room buzzing with flies")
print(kitchen.get_description())