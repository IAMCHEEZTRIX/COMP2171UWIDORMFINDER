from models.database import Database
from typing import Optional, Dict, List
from datetime import datetime
from core.application import Application

from core.room import Room

class ApplicationModel:
    __db = Database()
    
    def create_application(self, user, room: Room, application: Application) -> bool:
        query = """
            INSERT INTO applications (
                room_id, user_id, education_level, program_type,
                reason_for_applying, co_curricular_activities, agreement
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            room.get_room_id(),
            user.getuserID(),
            application.get_education_level(),
            application.get_program_type(),
            application.get_reason_for_applying(),
            application.get_co_curricular_activities(),
            application.get_agreement()
        )
        
        try:
            self.__db.exec(query, values)
            return True
        except Exception as e:
            print(f"Error creating application: {e}")
            return False
    
    def application_exists(self, application_id: int) -> bool:
        query = "SELECT 1 FROM applications WHERE application_id = %s LIMIT 1"
        result = self.__db.exec(query, (application_id,), fetch=True)
        return bool(result)
    
    
    def get_all_applications(self) -> list[Application]:
        query = """
            SELECT * FROM applications 
            ORDER BY application_date DESC
        """
        results = self.__db.exec(query, (), fetch=True)
        
        applications = []
        
        if results:
            for row in results:
                applications.append(Application({
                    'application_id': row[0],
                    'room_id': row[1],
                    'user_id': row[2],
                    'education_level': row[3],
                    'program_type': row[4],
                    'reason_for_applying': row[5],
                    'co_curricular_activities': row[6],
                    'agreement': bool(row[7]),
                    'application_date': row[8],
                    'status': row[9],
                    'processed_by': row[10],
                    'processed_date': row[11]
                }))
        
        return applications
    
    
    def get_application_with_user_details(self, application_id: int) -> Optional[Dict]:

        query = """
            SELECT a.*, u.fname, u.lname, u.email, u.telephone, u.gender
            FROM applications a
            JOIN users u ON a.user_id = u.user_id
            WHERE a.application_id = %s
        """
        result = self.__db.exec(query, (application_id,), fetch=True)
        return result[0] if result else None
    
    def get_application_by_room_and_student(self, room_id: int, student_id: int) -> Optional[Application]:
  
        query = """
            SELECT * FROM applications 
            WHERE room_id = %s AND user_id = %s
            ORDER BY application_date DESC
            LIMIT 1
        """
        result = self.__db.exec(query, (room_id, student_id), fetch=True)
        
        if not result or len(result) == 0:
            return None
        
        # Extract the first row (since we limited to 1 result)
        app_data = result[0]
        
        # Map database columns to application fields
        application_dict = {
            'application_id': app_data[0],
            'room_id': app_data[1],
            'user_id': app_data[2],
            'education_level': app_data[3],
            'program_type': app_data[4],
            'reason_for_applying': app_data[5],
            'co_curricular_activities': app_data[6],
            'agreement': bool(app_data[7]),
            'application_date': app_data[8],
            'status': app_data[9],
            'processed_by': app_data[10],
            'processed_date': app_data[11]
        }
        
        return Application(application_dict)
    
    def get_all_applications_by_student(self, student_id: int) -> list[Application]:
  
        query = """
            SELECT * FROM applications 
            WHERE user_id = %s
            ORDER BY application_date DESC
        """
        results = self.__db.exec(query, (student_id,), fetch=True)
        
        applications = []
        
        if results:
            for row in results:
                application_data = {
                    'application_id': row[0],
                    'room_id': row[1],
                    'user_id': row[2],
                    'education_level': row[3],
                    'program_type': row[4],
                    'reason_for_applying': row[5],
                    'co_curricular_activities': row[6],
                    'agreement': bool(row[7]),
                    'application_date': row[8],
                    'status': row[9],
                    'processed_by': row[10],
                    'processed_date': row[11]
                }
                applications.append(Application(application_data))
        
        return applications
    
    def get_user_applications(self, user_id: int) -> List[Dict]:

        query = """
            SELECT a.*, r.room_type, r.building, r.floor_number
            FROM applications a
            JOIN rooms r ON a.room_id = r.room_id
            WHERE a.user_id = %s
            ORDER BY a.application_date DESC
        """
        return self.__db.exec(query, (user_id,), fetch=True)
    
    def update_application_status(self, application_id: int, status: str) -> bool:
        query = "UPDATE applications SET status = %s WHERE application_id = %s"
        return bool(self.__db.exec(query, (status, application_id)))
    
    def get_All_applications_by_user(self, user):
        query = "SELECT * from applications where user_id = %s"
        results = self.__db.exec(query, (user.getuserID(),), fetch=True)
        
        applications = []
        if results:
            for row in results:
                # Map database row to application data dictionary
                application_data = {
                    'application_id': row[0],
                    'room_id': row[1],
                    'user_id': row[2],
                    'education_level': row[3],
                    'program_type': row[4],
                    'reason_for_applying': row[5],
                    'co_curricular_activities': row[6],
                    'agreement': bool(row[7]),
                    'application_date': row[8],
                    'status': row[9],
                    'processed_by': row[10],
                    'processed_date': row[11]
                }
                applications.append(Application(application_data))
        
        return applications
    
    
    def update_application(self, application_id: int, update_data: Dict) -> bool:
        if not update_data:
            return False
        
        set_clauses = []
        values = []
        
        # List of allowed fields that can be updated
        allowed_fields = [
            'education_level', 'program_type', 'reason_for_applying',
            'co_curricular_activities', 'agreement', 'status'
        ]
        
        for field, value in update_data.items():
            if field in allowed_fields:
                set_clauses.append(f"{field} = %s")
                values.append(value)
        
        if not set_clauses:
            return False
        
        values.append(application_id)
        query = f"UPDATE applications SET {', '.join(set_clauses)} WHERE application_id = %s"
        
        try:
            return bool(self.__db.exec(query, tuple(values)))
        except Exception as e:
            print(f"Error updating application: {e}")
            return False