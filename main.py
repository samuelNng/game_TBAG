from room import Room

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
kitchen.RoomName()
kitchen.describe()


#print(ballroom.get_description())
ballroom.RoomName()
ballroom.describe()

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom,"west")
ballroom.link_room(dining_hall,"east")



kitchen.get_details()
dining_hall.get_details()