class Room:
    def __init__(self,room_name):
        self.name =room_name
        self.description= None
    #getter
    def get_description (self):
        return self.description
    #setter
    def set_description(self, room_description):
        self.description = room_description
    