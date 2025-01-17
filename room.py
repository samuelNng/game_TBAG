class Room:
    def __init__(self):
        self.name =None
        self.description= None
        self.linked_rooms={}
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
    
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        print(self.name)
        print("-------------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
        print("The " + room.get_name()+ " is "+direction)