class Character():
 # Create a character​

    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character​

    def describe(self):

        print( self.name + " is here!")

        print( self.description)

    # Set what this character will say when talked to​

    def set_conversation(self, conversation):
        self.conversation = conversation
    # Talk to this character​

    def talk(self):
        if self.conversation is not None:
            print(self.name + ": "+ self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character​

    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")

        return True
    
class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You have defeated " + self.name + " with the " + combat_item )
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False
        
class Supporter(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.cheese_given = False  # Track whether cheese has been given

    def pet(self):
        if not self.cheese_given:
            print(f"You pet {self.name}. {self.name} purrs happily and gives you some cheese!")
            self.cheese_given = True
            return "cheese"  # Return the cheese as an item
        else:
            print(f"{self.name} has already given you cheese. No more cheese for now.")
            return None