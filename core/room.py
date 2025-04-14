class Room:
    def __init__(self, room_id: int = None, building: int = None, 
                 room_type: str = None, floor_number: int = None,
                 description: str = None, total_rooms: int = None,
                 booked_rooms: int = None, available_rooms: int = None,
                 image_url: str = None):

        self.__room_id = room_id
        self.__building = building
        self.__room_type = room_type
        self.__floor_number = floor_number
        self.__description = description
        self.__total_rooms = total_rooms
        self.__booked_rooms = booked_rooms
        self.__available_rooms = available_rooms
        self.__image_url = image_url

    # Getters for all attributes
    def get_room_id(self):
        return self.__room_id

    def get_building(self):
        return self.__building

    def get_room_type(self):
        return self.__room_type

    def get_floor_number(self):
        return self.__floor_number

    def get_description(self):
        return self.__description

    def get_total_rooms(self):
        return self.__total_rooms

    def get_booked_rooms(self):
        return self.__booked_rooms

    def get_available_rooms(self):
        return self.__available_rooms

    def get_image_url(self):
        return self.__image_url

    def __str__(self):
        """String representation of the room"""
        return (f"Room(ID: {self.__room_id}, Building: {self.__building}, "
                f"Type: {self.__room_type}, Floor: {self.__floor_number}, "
                f"Available: {self.__available_rooms}/{self.__total_rooms})")