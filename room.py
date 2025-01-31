class Room:
    def __init__(self):
        self.name =None
        self.description= None
        self.linked_rooms={}
        self.character = None
        self.item = None
    #getter description
    def get_description (self):
        return self.description
    #setter description
    def set_description(self, room_description):
        self.description = room_description

    def describe(self):
        print(self.description)

    #getter name
    def get_name (self):
        return self.name
    #setter name
    def set_name(self, room_name):
        self.name = room_name

    def RoomName(self):
        print(self.name)
    
    def link_room(self, room_to_link, direction, locked=False):
        self.linked_rooms[direction] = (room_to_link, locked)

    def get_details(self):
        print(self.name)
        print("-------------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room, locked  = self.linked_rooms[direction]
            if locked == True:
                print(f"The {room.get_name()} is {direction} (locked)")
            else:
                print(f"The {room.get_name()} is {direction}")
        print("-------------------------\n")
    #moving between rooms
    def move(self, direction, has_key=False):
        if direction in self.linked_rooms:
            room, locked = self.linked_rooms[direction]
            if locked and not has_key:
                print("The door is locked. You need a key to open it.")
                return self
            else:
                return room
        else:
            print("You can't go that way.")
            return self
        
    #Put character into room
    # set & get character
    def set_character(self, new_character):
     self.character = new_character

    # set & get item
    def get_character(self):
        return self.character
    
    def get_item(self):
        return self.item

    def set_item(self, item):
        self.item = item

    def remove_item(self):
        self.item = None