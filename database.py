import psycopg2

try:
 conexion= psycopg2.connect(
    host = 'localhost',
    database = 'Formulario',
    user = 'postgres',
    password  = '1810hsxd'
    )
except psycopg2.Error as e:
    print('ocurrio un error al conectarse a PostgresSQL',e)
cur = conexion.cursor()
# Obtener los resultados como objetos Python
#row = cur.fetchone()
def Formulario():
 try:
    cur=conexion.cursor()
    cur.execute( "SELECT cedula,nombre,apellido,edad,telefno,correo,pregunta1,pregunta2,pregunta3 FROM Formulario" )
    for cedula,nombre,apellido,edad,telefno,correo,pregunta1,pregunta2,pregunta3  in cur.fetchall() :
     lista = [cedula,nombre,apellido,edad,telefno,correo,pregunta1,pregunta2,pregunta3 ]
     print (lista)
 except:
     print('error al conectar la base de datos')
     cerrarConexion()

def cerrarConexion():
    conexion.close()

# def index():
#     #sql="INSERT INTO 'Formulario'('cedula','nombre','apellido','edad','telefno','correo','pregunta1','pregunta2','pregunta3') VALUES (1766617813,'Gloria Alejandra','Molina Ron',20,0928739478,'gloria@gmail.com','te gustan los gatos','como estas hoy','que vas a hacer')"
#     cur=conexion.cursor()
#     cur.execute("INSERT INTO Formulario (cedula,nombre,apellido,edad,telefno,correo,pregunta1,pregunta2,pregunta3) VALUES (1766617813,'Gloria Alejandra','Molina Ron',20,0928739478,'gloria@gmail.com','te gustan los gatos','como estas hoy','que vas a hacer') ")
#     conexion.commit()

#index()
Formulario()
