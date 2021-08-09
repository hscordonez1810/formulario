import psycopg2

conexion= psycopg2.connect(
    host = 'localhost',
    database = 'Formulario',
    user = 'postgres',
    password  = '1810hsxd'
    )
cur = conexion.cursor()
# Obtener los resultados como objetos Python
#row = cur.fetchone()
def Formulario():
 try:
    cur=conexion.cursor()
    cur.execute( "SELECT Cedula,Nombre,Apellido,Correo,pregunta1,pregunta2 FROM Formulario" )
    for Cedula,Nombre,Apellido,Correo,pregunta1,pregunta2  in cur.fetchall() :
     lista = [Cedula,Nombre,Apellido,Correo,pregunta1,pregunta2 ]
     print (lista)
 except:
     print('error al conectar la base de datos')
     cerrarConexion()




def cerrarConexion():
    conexion.close()

Formulario()
