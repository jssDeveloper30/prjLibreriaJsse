#
# @autor: Jhon Sebastian Serna
# @fecha: 2023/11/17
# @descripción: Crud Autor
#

# librerias propias de python
from mysql import connector
# librerias QtDesigner
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

# librerias PDF Generator
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

class DlgCrudClientes(QMainWindow):
    def __init__(self,dlgPrincipal):
        super(DlgCrudClientes,self).__init__()
        loadUi('uis/crudClientes.ui',self)
        self.dlgPrincipal = dlgPrincipal
        
    
        nombreColumnas = ['ID Clientes','Identificación','Nombres','Apellidos','Telefono','Direccion','Correo electronico','Estado']
        self.tblWdgtUsuarios.setColumnCount(len(nombreColumnas))
        self.tblWdgtUsuarios.setHorizontalHeaderLabels(nombreColumnas)
        
        self.cargarDatos()
        self.btnInsertar.clicked.connect(self.insertar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnActualizar.clicked.connect(self.actualizar)
        self.tblWdgtUsuarios.clicked.connect(self.filaElegida)
        self.btnReporte.clicked.connect(self.reporteCliente)
        
        
    def cargarDatos(self):
        miLibreriaCon = connector.connect(host = 'localhost',
                                        user = 'root',
                                        password = '',
                                        database = 'libreriajsse2614986')
        myCursor = miLibreriaCon.cursor()
        stmt = f"""SELECT id_Cliente,identificacion,nombres,apellidos,telefono,direccion,correo_electronico,estado FROM clientes"""
        myCursor.execute(stmt)
        filas = myCursor.fetchall()
        
        nroFilas = len(filas)
        self.tblWdgtUsuarios.setRowCount(nroFilas)
        f = 0
        
        if filas:
            for fila in filas:
                self.tblWdgtUsuarios.setItem(f, 0, QtWidgets.QTableWidgetItem(str(fila[0]))) 
                self.tblWdgtUsuarios.setItem(f, 1, QtWidgets.QTableWidgetItem(fila[1]))   
                self.tblWdgtUsuarios.setItem(f, 2, QtWidgets.QTableWidgetItem(fila[2]))
                self.tblWdgtUsuarios.setItem(f, 3, QtWidgets.QTableWidgetItem(fila[3]))
                self.tblWdgtUsuarios.setItem(f, 4, QtWidgets.QTableWidgetItem(fila[4]))
                self.tblWdgtUsuarios.setItem(f, 5, QtWidgets.QTableWidgetItem(fila[5]))
                self.tblWdgtUsuarios.setItem(f, 6, QtWidgets.QTableWidgetItem(fila[6]))
                self.tblWdgtUsuarios.setItem(f, 7, QtWidgets.QTableWidgetItem(fila[7]))
                
                f +=1


    def filaElegida(self):
        fila = self.tblWdgtUsuarios.currentRow()
        idCliente = self.tblWdgtUsuarios.item(fila, 0)
        identificacion = self.tblWdgtUsuarios.item(fila,1)
        nombres = self.tblWdgtUsuarios.item(fila, 2)
        apellidos = self.tblWdgtUsuarios.item(fila, 3)
        telefono = self.tblWdgtUsuarios.item(fila, 4)
        direccion = self.tblWdgtUsuarios.item(fila, 5)
        correo = self.tblWdgtUsuarios.item(fila, 6)
        estado = self.tblWdgtUsuarios.item(fila, 7)
        
        self.spIdCliente.setValue(int(idCliente.text()))
        self.txtIdentificacion.setText(identificacion.text())
        self.txtNombres.setText(nombres.text())
        self.txtApellidos.setText(apellidos.text())
        self.txtTelefono.setText(telefono.text())
        self.txtDireccion.setText(direccion.text())
        self.txtCorreo.setText(correo.text())
        self.txtEstado.setText(estado.text())

    def actualizar(self):
        if self.txtIdentificacion.text() !="" and self.txtNombres.text() !="" and self.txtApellidos.text() !="" and self.txtTelefono.text() !="" and self.txtDireccion.text() !="" and self.txtCorreo.text() != "" and self.txtEstado.text() != "":
            idCliente = self.spIdCliente.value()
            identificacion = self.txtIdentificacion.text()
            nombres = self.txtNombres.text()
            apellidos = self.txtApellidos.text()
            telefono = self.txtTelefono.text()
            direccion = self.txtDireccion.text()
            correo = self.txtCorreo.text()
            estado = self.txtEstado.text()
            
            miLibreriaCon = connector.connect(host = 'localhost',
                                            user = 'root',
                                            password = '',
                                            database = 'libreriajsse2614986')
            myCursor = miLibreriaCon.cursor()
            stmtUpdate = f"""UPDATE clientes SET
                            identificacion = '{identificacion}',
                            nombres = '{nombres}',
                            apellidos = '{apellidos}',
                            telefono = '{telefono}',
                            direccion = '{direccion}',
                            correo_electronico = '{correo}',
                            estado='{estado}'
                        WHERE id_cliente ='{idCliente}'"""
            myCursor.execute(stmtUpdate)
            miLibreriaCon.commit()
            
            self.cargarDatos()
            self.txtIdentificacion.setText("")
            self.txtNombres.setText("")
            self.txtApellidos.setText("")
            self.txtTelefono.setText("")
            self.txtDireccion.setText("")
            self.txtCorreo.setText("")
            self.txtEstado.setText("")
            
    def eliminar(self):
        if self.txtIdentificacion.text() !="" and self.txtNombres.text() !="" and self.txtApellidos.text() !="" and self.txtTelefono.text() !="" and self.txtDireccion.text() !="" and self.txtCorreo.text() != "" and self.txtEstado.text() != "":
            idCliente = self.spIdCliente.value()
            miLibreriaCon = connector.connect(host = 'localhost',
                                            user = 'root',
                                            password = '',
                                            database = 'libreriajsse2614986')
            myCursor = miLibreriaCon.cursor()
            stmtDelete = f"""DELETE FROM clientes
                        WHERE id_cliente ='{idCliente}'"""
            myCursor.execute(stmtDelete)
            miLibreriaCon.commit()
            
            self.cargarDatos()
            self.txtIdentificacion.setText("")
            self.txtNombres.setText("")
            self.txtApellidos.setText("")
            self.txtTelefono.setText("")
            self.txtDireccion.setText("")
            self.txtCorreo.setText("")
            self.txtEstado.setText("")
            
    def insertar(self):
        if self.txtIdentificacion.text() !="" and self.txtNombres.text() !="" and self.txtApellidos.text() !="" and self.txtTelefono.text() !="" and self.txtDireccion.text() !="" and self.txtCorreo.text() != "":
            identificacion = self.txtIdentificacion.text()
            nombres = self.txtNombres.text()
            apellidos = self.txtApellidos.text()
            telefono = self.txtTelefono.text()
            direccion = self.txtDireccion.text()
            correo = self.txtCorreo.text()
            estado = self.txtEstado.text()
            miLibreriaCon = connector.connect(host = 'localhost',
                                            user = 'root',
                                            password = '',
                                            database = 'libreriajsse2614986')
            myCursor = miLibreriaCon.cursor()
            stmtInsertar = f"""INSERT INTO clientes (identificacion,nombres,apellidos,telefono,direccion,correo_electronico,estado)
            VALUES('{identificacion}','{nombres }','{apellidos}','{telefono}','{direccion}','{correo}','{estado}')"""
                            
            myCursor.execute(stmtInsertar)
            miLibreriaCon.commit()
            
            self.cargarDatos()
            self.txtIdentificacion.setText("")
            self.txtNombres.setText("")
            self.txtApellidos.setText("")
            self.txtTelefono.setText("")
            self.txtDireccion.setText("")
            self.txtCorreo.setText("")
            self.txtEstado.setText("")
        else:
            self.lblMensaje.setText("Debe llenar todos los campos")
            
    def reporteCliente(self):
        nombreArchivo = "Reporte_Cliente.pdf"
        titulo = "REPORTE DE CLIENTES"
        encabezado = "  ID CLIENTE IDENTIFICACION    NOMBRE      APELLIDOS    TELEFONO DIRECCION CORREO ELECTRONICO ESTADO"
        lineas = [encabezado]

        miLibreriaCon = connector.connect(
            host="localhost",
            user="root",
            password="",
            database="libreriajsse2614986"
        )
        myCursor = miLibreriaCon.cursor()
        stmt = "SELECT * FROM clientes"
        myCursor.execute(stmt)
        registros = myCursor.fetchall()

        for registro in registros:
            linea = f"     {registro[0]}          {registro[1]}     {registro[2]}     {registro[3]}  {registro[4]}   {registro[5]}   {registro[6]}   {registro[7]}"
            lineas.append(linea)

        # Crear el archivo PDF fuera del bucle for
        pdf = canvas.Canvas(nombreArchivo)
        pdf.setTitle(titulo)
        pdf.setFillColorRGB(0, 0, 0)
        pdf.setFont("Courier", 10)

        # Obtener el ancho de la página y el encabezado
        ancho_pagina, _ = pdf._pagesize
        ancho_encabezado = pdf.stringWidth(encabezado, "Courier", 10)

        # Centrar el encabezado
        x_centro_encabezado = (ancho_pagina - ancho_encabezado) / 2
        pdf.drawCentredString(x_centro_encabezado, 800, titulo)
        pdf.line(20, 780, 550, 780)

        # Crear un texto multilinea utilizando textObject y un ciclo 'for'
        y_inicio_texto = 760
        texto = pdf.beginText(x_centro_encabezado, y_inicio_texto)
        texto.setFont("Courier", 8)
        texto.setFillColor(colors.green)

        for linea in lineas:
            texto.textLine(linea)

        pdf.drawText(texto)

        # Cerrar la conexión a la base de datos
        miLibreriaCon.close()

        # Guardar el archivo PDF fuera del bucle for
        pdf.save()