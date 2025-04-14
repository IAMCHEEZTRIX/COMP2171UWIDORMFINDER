from models.database import Database
from typing import Optional, Dict, List
from core.room import Room

class RoomModel:
    __room_id = None
    __building = None
    __room_type = None
    __floor_number = None
    __description = None
    __total_rooms = None
    __booked_rooms = None
    __available_rooms = None
    __image_url = None
    __db = Database()
    
    def __init__(self, **kwargs):
       
        self.__room_id = kwargs.get('room_id')
        self.__building = kwargs.get('building')
        self.__room_type = kwargs.get('room_type')
        self.__floor_number = kwargs.get('floor_number')
        self.__description = kwargs.get('description')
        self.__total_rooms = kwargs.get('total_rooms')
        self.__booked_rooms = kwargs.get('booked_rooms')
        self.__available_rooms = kwargs.get('available_rooms')
        self.__image_url = kwargs.get('image_url')
        
    
    def getRooms(self, filters: Optional[Dict] = None) -> List[Dict]:
       
        base_query = 'SELECT * FROM rooms'
        where_clauses = []
        values = []
        
        if filters:
            for field, value in filters.items():
                if value and value != 'All':  # Skip None and 'All' values
                    where_clauses.append(f"{field} = %s")
                    values.append(value)
            
            if where_clauses:
                base_query += ' WHERE ' + ' AND '.join(where_clauses)
        
        rooms_data = self.__db.exec(base_query, tuple(values), fetch=True)
        
        # Convert database rows to Room objects
        rooms = []
        if rooms_data:
            for room_data in rooms_data:
                room = Room(
                    room_id=room_data[0],
                    building=room_data[1],
                    room_type=room_data[2],
                    floor_number=room_data[3],
                    description=room_data[4],
                    total_rooms=room_data[5],
                    booked_rooms=room_data[6],
                    available_rooms=room_data[7],
                    image_url=room_data[8]
                )
                rooms.append(room)
        
        return rooms
    
    def get_room_by_id(self, room_id: int) -> Optional[Room]:
        query = 'SELECT * FROM rooms WHERE room_id = %s'
        room_data = self.__db.exec(query, (room_id,), fetch=True)
        
        if room_data:
            room = Room(
                room_id=room_data[0][0],
                building=room_data[0][1],
                room_type=room_data[0][2],
                floor_number=room_data[0][3],
                description=room_data[0][4],
                total_rooms=room_data[0][5],
                booked_rooms=room_data[0][6],
                available_rooms=room_data[0][7],
                image_url=room_data[0][8]
            )
            return room
        return None