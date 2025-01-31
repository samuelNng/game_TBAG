from character import Character, Enemy

dave = Enemy("Dave", "A smelly zombie")


dave.describe()

dave.set_conversation("Arrrrrrr...")

dave.talk()

dave.set_weakness("cheese")

fight_with = input ("What are you going to fight with?: ")

dave.fight(fight_with)