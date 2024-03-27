from Conexion import *

class CClientes:   
    

    def IngresarClientes(self, Nombre, Telefono, Pueblo, Financiamiento, Falla, Solucion, Tier):
            
        try:
            sql = "insert into usuarios values (null, %s, %s, %s, %s, %s, %s, %s);"
            valores = (Nombre, Telefono, Pueblo, Financiamiento, Falla, Solucion, Tier)
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            #la variable valores tiene que ser una tupla
            #como minima expresion es: (valor,) la coma hace que se a una tupla
            #las tuplas son listas inmutables, eso quiere decir que no se puede modificar

            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            cone.close()
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datos {}".format(error))
            
                    
    
    def ModificarClientes(self, Usuarioid, Nombre, Telefono, Pueblo, Financiamiento, Falla, Solucion, Tier):
            
        try:
            sql = "UPDATE usuarios SET usuarios.Nombre = %s,usuarios.Telefono = %s,usuarios.Pueblo = %s,usuarios.Financiamiento = %s,usuarios.Falla = %s,usuarios.Solucion = %s,usuarios.Tier = %sWhere usuarios.Id =%s;"
            valores = (Nombre, Telefono, Pueblo, Financiamiento, Falla, Solucion, Tier, Usuarioid)
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro actualizado")
            cone.close()
            
        except mysql.connector.Error as error:
            print("Error de actualizacion de datos {}".format(error))
            

    def BuscarCliente(self, criterio_busqueda, valor):
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()

            if criterio_busqueda == "Nombre":
                sql = "SELECT * FROM usuarios WHERE Nombre = %s"
            elif criterio_busqueda == "Telefono":
                sql = "SELECT * FROM usuarios WHERE Telefono = %s"

            cursor.execute(sql, (valor,))
            resultados = cursor.fetchall()
            
            cone.close()
            
            return resultados
        except mysql.connector.Error as error:
            print("Error al buscar cliente: {}".format(error))
    
    
    def EliminarClientes(self, Usuarioid):
            
        try:
            sql = "DELETE from usuarios WHERE usuarios.Id = %s;"
            valores = (Usuarioid,)
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute(sql,valores)
            cone.commit()
            print(cursor.rowcount,"Registro eliminado")
            cone.close()
            
        except mysql.connector.Error as error:
            print("Error al eliminar los datos {}".format(error))
            
    
    def MostrarClientes():
        
        try:
            cone = CConexion.ConexionBaseDeDatos()
            cursor = cone.cursor()
            cursor.execute("SELECT * FROM usuarios;")
            miResultado = cursor.fetchall()
            cone.commit()
            cone.close()
            return miResultado
                
        except mysql.connector.Error as error:
            print("Error de mostrar datos {}".format(error))