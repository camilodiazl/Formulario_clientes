#pip install mysql-connector-python
import mysql.connector

class CConexion:
    @staticmethod
    def ConexionBaseDeDatos():
        try:
            conexion=mysql.connector.connect(user='uudcivbbgtiloj9y',password='YtSf8ADLnMECjvYjDhCJ',host='bkslurgle4kky8o0pool-mysql.services.clever-cloud.com', database='bkslurgle4kky8o0pool',port='3306')
            
            print("Conexion correcta")
            
            return conexion
        
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos {}" .format(error))
            
            return None

CConexion.ConexionBaseDeDatos()