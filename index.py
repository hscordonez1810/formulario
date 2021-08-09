from flask import Flask 
from flask import render_template,request
import psycopg2

app= Flask(__name__)

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


@app.route('/')

# def db():
#     sql="insert into Formulario(cedula,nombre,apellido,edad,telefno,correo,pregunta1,pregunta2,pregunta3) values (1766617813,'Gloria Alejandra','Molina Ron',20,0928739478,'gloria@gmail.com','te gustan los gatos','como estas hoy','que vas a hacer')"
#     conn=psycopg2.connect()
#     cursor=conn.cursor()
#     cursor.execute(sql)
#     conn.commit() 

def index():
    #sql="INSERT INTO 'Formulario'('cedula','nombre','apellido','edad','telefno','correo','pregunta1','pregunta2','pregunta3') VALUES (1766617813,'Gloria Alejandra','Molina Ron',20,0928739478,'gloria@gmail.com','te gustan los gatos','como estas hoy','que vas a hacer')"
    #cur=conexion.cursor()
    #cur.execute("INSERT INTO Formulario (cedula,nombre,apellido,edad,telefno,correo,pregunta1,pregunta2,pregunta3) VALUES (1966617813,'Gloria Alejandra','Molina Ron',20,0928739478,'gloria@gmail.com','te gustan los gatos','como estas hoy','que vas a hacer') ")
    #conexion.commit()
    #index()
    #conexion.close()
    return render_template('index.html')
#@app.route('/')
@app.route('/store', methods=['POST'])
def storage():
    _cedula=request.form["txtCedula"]
    _nombre=request.form['txtNombre']
    _apellido=request.form['txtApellido']
    _edad=request.form['txtEdad']
    _telefono=request.form['txtTelefono']
    _correo=request.form['txtCorreo']
    _pregunta1=request.form['txtPregunta1'] 
    _pregunta2=request.form['txtPregunta2'] 
    _pregunta3=request.form['txtPregunta3']  
    cur=conexion.cursor()  
    #query= cur.execute("INSERT INTO Formulario (cedula,nombre,apellido,edad,telefno,correo,pregunta1,pregunta2,pregunta3) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) ")
    query="INSERT INTO Formulario( cedula,nombre,apellido,edad,telefno,correo,pregunta1,pregunta2,pregunta3) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    datos=(_cedula,_nombre,_apellido,_edad,_telefono,_correo,_pregunta1,_pregunta2,_pregunta3)
    #query="INSERT INTO Formulario (cedula,nombre,apellido,edad,telefno,correo,pregunta1,pregunta2,pregunta3) VALUES (1966617813,'Gloria Alejandra','Molina Ron',20,0928739478,'gloria@gmail.com','te gustan los gatos','como estas hoy','que vas a hacer') "
    cur.execute(query,datos)
    conexion.commit()
    #storage()
    #conexion.close()
    return render_template('index.html')




@app.route('/formularios_guardados')
def formularios_guardados():
    return render_template('formularios_guardados.html')

if __name__ == '__main__':
    app.run(debug=True)

def cerrarConexion():
    conexion.close()