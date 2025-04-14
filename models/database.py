import mysql.connector
from config import DB_CONFIG

class Database:
    
    def getConnection(self):
        
        conn = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database']
        )
        
        return conn
    
    def exec(self, query, values, fetch=False):
        conn = self.getConnection()
        cursor = conn.cursor()
        result = None
        
        try:
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)  

            if fetch:
                result = cursor.fetchall()
                
            conn.commit() 
             
        except Exception as e:
            
            print(f"Error executing query: {e}")
            conn.rollback() 
             
        finally:
            conn.close() 
        
        return result
        
        
