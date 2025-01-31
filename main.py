from room import Room
from character import Supporter,Enemy
from item import Item

# Create rooms
kitchen = Room()
kitchen.set_name("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")

ballroom = Room()
ballroom.set_name("ballrom")
ballroom.set_description("A vast room with a shiny wooden floor")

dining_hall = Room()
dining_hall.set_name("dining_hall")
dining_hall.set_description("A large room with ornate golden decorations")



#link_room
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom,"west")
ballroom.link_room(dining_hall,"east")


# Create a cat character
cat = Supporter("Whiskers", "A fluffy white cat with green eyes. If you \033[4mpet\033[0m it, it may give you something.")
# Set the cat's conversation
cat.set_conversation("Meow! Purr...")
# Describe the cat
cat.describe() 
# Talk to the cat
cat.talk() 
kitchen.set_character(cat)

#put Enemy to the room
dave = Enemy("Dave", "A smelly zombie")
dave.describe()
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

# Create a key and add it to the kitchen
key = Item()
key.set_name("key")
key.set_description("A small, shiny key that looks like it could open a door.")
kitchen.set_item(key)

cheese = False
YouDead = False
has_key = False
current_room = kitchen
while YouDead == False:
      print("\n")
      current_room.get_details()
      inhabitant = current_room.get_character()
      
      if inhabitant is None:
            print("There have no character!\n")
            print("Which direction would you like to go? North, east, south, west")
      
      if inhabitant is not None:
            inhabitant.describe()
      command = input("\n> ")
      if command in ["north", "south", "east", "west"]:
                  current_room = current_room.move(command)
      elif command == "talk":
            if inhabitant is not None:
                inhabitant.talk()
     
      elif command == "pet":
            if inhabitant is not None and isinstance(inhabitant, Supporter):
                  cheese = True
                  print("You now have cheese in your inventory!")
            else:
                  print("There's no one here to pet.")
      elif command == "take":
            if item is not None:
                  if item.name == "key":
                        has_key = True
                        print("You take the key.")
                        current_room.remove_item()
                  else:
                        print(f"You take the {item.name}.")
            else:
                   print("There's nothing here to take.")

      elif command == "fight":
            if inhabitant is not None and isinstance(inhabitant, Enemy):
                  fight_with = input ("What are you going to fight with?: ")
                  if fight_with == "cheese"and cheese == False:
                        print("you have no cheese, you should pet the cat next time.")
                        print("GAME OVER!")
                        YouDead = True

                  elif inhabitant.fight(fight_with) == True and cheese == True:
                        current_room.set_character(None)
                        cheese = False
                        print("Hooray, you won the fight!")

                  else:
                        YouDead = True
                        print("GAME OVER!")
            elif inhabitant is not None and isinstance(inhabitant, Supporter):
                  inhabitant.talk()
                  print(f"Seem the {Supporter.name} do not want to fight with you!")
            else:
                  print("There's no one here to fight.")
      else :
            print("Invalid command. Try 'north', 'south', 'east', 'west', 'talk', 'pet', or 'fight'.")     
                  