from character import Enemy
dave = Enemy("Dave", "A smelly zombie")

dave.describe()

# Add some conversation for Dave when he is talked to
dave.set_conversation("Hello there! I am going to join your OOP game very soon")

# Trigger a conversation with Dave
dave.talk()

# Set a weakness
dave.set_weakness("cheese")

# Fight with dave
print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)