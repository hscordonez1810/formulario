from flask import Flask 
from flask import render_template,request,redirect
import psycopg2
from flask import flash
from datetime import datetime
from random import randint
from database import abrirConexion,cerrarConexion
app= Flask(__name__)

conexion= abrirConexion()



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

@app.route('/update',methods=['POST'])
def update():
    cur= conexion.cursor()
    _nombre=request.form['txtNombre']
    _apellido=request.form['txtApellido']
    _edad=request.form['txtEdad']
    _telefono=request.form['txtTelefono']
    _correo=request.form['txtCorreo']
    _pregunta1=request.form['txtPregunta1'] 
    _pregunta2=request.form['txtPregunta2'] 
    _pregunta3=request.form['txtPregunta3']
    _cedula=request.form["txtCedula"]
    query="UPDATE  Formulario SET nombre=%s,apellido=%s,edad=%s,telefno=%s,correo=%s,pregunta1=%s,pregunta2=%s,pregunta3=%s WHERE cedula=%s;"
    datos=(_nombre,_apellido,_edad,_telefono,_correo,_pregunta1,_pregunta2,_pregunta3,_cedula)
    #query="INSERT INTO Formulario (cedula,nombre,apellido,edad,telefno,correo,pregunta1,pregunta2,pregunta3) VALUES (1966617813,'Gloria Alejandra','Molina Ron',20,0928739478,'gloria@gmail.com','te gustan los gatos','como estas hoy','que vas a hacer') "
    cur.execute(query,datos)
    conexion.commit() 
    return redirect('/almacenados')



@app.route('/store', methods=['POST'])
def storage():
  try:
    _cedula=request.form["txtCedula"]
    _nombre=request.form['txtNombre']
    _apellido=request.form['txtApellido']
    _edad=request.form['txtEdad']
    _telefono=int(request.form['txtTelefono'])
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
  except ValueError:
     flash('esta ingresando datos erroneos')
     return redirect('index.html')




@app.route('/almacenados')
def almacenados():
    cur=conexion.cursor()
    query="SELECT * FROM Formulario"
    cur.execute(query)
    formulario=cur.fetchall()
    print(formulario)
    conexion.commit()
    return render_template('almacenados.html',formulario=formulario)





@app.route('/destroy/<int:cedula>')
def destroy(cedula):
    cur=conexion.cursor()  
    cur.execute("DELETE FROM Formulario WHERE cedula=%s",[cedula])
    conexion.commit()
    return redirect('/almacenados')


@app.route('/edit/<int:cedula>')
def edit(cedula): 
    cur=conexion.cursor()
    cur.execute("SELECT * FROM Formulario WHERE cedula=%s",[cedula])
    formulario=cur.fetchall()
    conexion.commit()
    return render_template('edit.html',formulario=formulario)

@app.route('/formularios_guardados')
def formularios_guardados():
    return render_template('formularios_guardados.html')

if __name__ == '__main__':
    app.run(debug=True)

def cerrarConexion():
    conexion.close()