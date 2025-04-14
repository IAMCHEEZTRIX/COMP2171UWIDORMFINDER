class Application:
    def __init__(self, application_data: dict):
 
        self.__application_id = application_data.get('application_id')
        self.__user_id = application_data['user_id']
        self.__education_level = application_data['education_level']
        self.__program_type = application_data['program_type']
        self.__reason_for_applying = application_data['reason_for_applying']
        self.__co_curricular_activities = application_data.get('co_curricular_activities')
        self.__agreement = application_data['agreement']
        self.__room_id = application_data['room_id']
        self.__status = application_data.get('status', 'Pending')
        self.__application_date = application_data.get('application_date')
        self.__processed_by = application_data.get('processed_by')
        self.__processed_date = application_data.get('processed_date')

    # Getters for all attributes
    def get_application_id(self) -> int:
        """Get application ID"""
        return self.__application_id

    def get_user_id(self) -> str:
        """Get student ID"""
        return self.__user_id

    def get_education_level(self) -> str:
        """Get education level"""
        return self.__education_level

    def get_program_type(self) -> str:
        """Get program type"""
        return self.__program_type

    def get_reason_for_applying(self) -> str:
        """Get reason for applying"""
        return self.__reason_for_applying

    def get_co_curricular_activities(self) -> str:
        """Get co-curricular activities"""
        return self.__co_curricular_activities

    def get_agreement(self) -> bool:
        """Get agreement status"""
        return self.__agreement

    def get_room_id(self) -> int:
        """Get room ID"""
        return self.__room_id

    def get_status(self) -> str:
        """Get application status"""
        return self.__status

    def get_application_date(self):
        """Get application date"""
        return self.__application_date

    def get_processed_by(self):
        """Get admin who processed the application"""
        return self.__processed_by

    def get_processed_date(self):
        """Get processing date"""
        return self.__processed_date

    def to_dict(self) -> dict:
        """Convert application to dictionary"""
        return {
            'application_id': self.__application_id,
            'user_id': self.__user_id,
            'education_level': self.__education_level,
            'program_type': self.__program_type,
            'reason_for_applying': self.__reason_for_applying,
            'co_curricular_activities': self.__co_curricular_activities,
            'agreement': self.__agreement,
            'room_id': self.__room_id,
            'status': self.__status,
            'application_date': self.__application_date,
            'processed_by': self.__processed_by,
            'processed_date': self.__processed_date
        }

    def __str__(self):
        """String representation of the application"""
        return (f"Application(ID: {self.__application_id}, Student: {self.__user_id}, "
                f"Room: {self.__room_id}, Status: {self.__status})")