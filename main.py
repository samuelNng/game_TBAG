from room import Room
from character import Enemy


kitchen = Room()
kitchen.set_name("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")

ballroom = Room()
ballroom.set_name("ballrom")
ballroom.set_description("A vast room with a shiny wooden floor")

dining_hall = Room()
dining_hall.set_name("dining_hall")
dining_hall.set_description("A large room with ornate golden decorations")

#print(kitchen.name)

#print(kitchen.get_description())
#kitchen.RoomName()
#kitchen.describe()


#print(ballroom.get_description())
#ballroom.RoomName()
#ballroom.describe()

#link_room
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom,"west")
ballroom.link_room(dining_hall,"east")



#kitchen.get_details()
#dining_hall.get_details()

#current_room = kitchen

#Add def charachter & enemy in main

dave = Enemy("Dave", "A smelly zombie")
dave.describe()
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

current_room = kitchen
while True:
  print("\n")
  current_room.get_details()
  inhabitant = current_room.get_character()

  if inhabitant is not None:
        inhabitant.describe()

  command = input("> ")
  current_room = current_room.move(command)