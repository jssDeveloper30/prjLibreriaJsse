#
# @autor: Jhon Sebastian Serna
# @fecha: 2023/11/17
# @descripción: Crud Autor
#

# librerias propias de python
from mysql import connector
# librerias QtDesigner
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

# librerias PDF Generator
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

class DlgCrudAutores(QMainWindow):
    def __init__(self,dlgPrincipal):
        super(DlgCrudAutores,self).__init__()
        loadUi('uis/crudAutores.ui',self)
        self.dlgPrincipal = dlgPrincipal
        
    
        nombreColumnas = ['id_Autor','nombres','apellidos']
        self.tblWdgtUsuarios.setColumnCount(len(nombreColumnas))
        self.tblWdgtUsuarios.setHorizontalHeaderLabels(nombreColumnas)
        
        self.cargarDatos()
        self.btnInsertar.clicked.connect(self.insertar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnActualizar.clicked.connect(self.actualizar)
        self.tblWdgtUsuarios.clicked.connect(self.filaElegida)
        self.btnReporte.clicked.connect(self.reporteAutor)
        
        
    def cargarDatos(self):
        miLibreriaCon = connector.connect(host = 'localhost',
                                        user = 'root',
                                        password = '',
                                        database = 'libreriajsse2614986')
        myCursor = miLibreriaCon.cursor()
        stmt = f"""SELECT id_autor,nombres,apellidos FROM autores"""
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
                
                f +=1


    def filaElegida(self):
        fila = self.tblWdgtUsuarios.currentRow()
        idAutor = self.tblWdgtUsuarios.item(fila, 0)
        nombres = self.tblWdgtUsuarios.item(fila, 1)
        apellidos = self.tblWdgtUsuarios.item(fila, 2)
        
        self.spIdAutor.setValue(int(idAutor.text()))
        self.txtNombres.setText(nombres.text())
        self.txtApellidos.setText(apellidos.text())
        
    def actualizar(self):
        if self.txtNombres.text() !="" and self.txtApellidos.text() !="":
            idAutor = self.spIdAutor.value()
            nombres = self.txtNombres.text()
            apellidos = self.txtApellidos.text()
            miLibreriaCon = connector.connect(host = 'localhost',
                                            user = 'root',
                                            password = '',
                                            database = 'libreriajsse2614986')
            myCursor = miLibreriaCon.cursor()
            stmtUpdate = f"""UPDATE autores SET
                            nombres = '{nombres}',
                            apellidos = '{apellidos}'
                        WHERE id_autor ='{idAutor}'"""
            myCursor.execute(stmtUpdate)
            miLibreriaCon.commit()
            
            self.cargarDatos()
            self.txtNombres.setText("")
            self.txtApellidos.setText("")
            
            
    def eliminar(self):
        if self.txtNombres.text() !="" and self.txtApellidos.text() !="":
            idAutor = self.spIdAutor.value()
            nombres = self.txtNombres.text()
            apellidos = self.txtApellidos.text()
            miLibreriaCon = connector.connect(host = 'localhost',
                                            user = 'root',
                                            password = '',
                                            database = 'libreriajsse2614986')
            myCursor = miLibreriaCon.cursor()
            stmtDelete = f"""DELETE FROM autores
                        WHERE id_autor ='{idAutor}'"""
            myCursor.execute(stmtDelete)
            miLibreriaCon.commit()
            
            self.cargarDatos()
            self.txtNombres.setText("")
            self.txtApellidos.setText("")
            
            
    def insertar(self):
        if self.txtNombres.text() !="" and self.txtApellidos.text() !="":
            nombres = self.txtNombres.text()
            apellidos = self.txtApellidos.text()
            miLibreriaCon = connector.connect(host = 'localhost',
                                            user = 'root',
                                            password = '',
                                            database = 'libreriajsse2614986')
            myCursor = miLibreriaCon.cursor()
            stmtInsertar = f"""INSERT INTO autores (nombres,apellidos)
            VALUES('{nombres }','{apellidos}')"""
                            
            myCursor.execute(stmtInsertar)
            miLibreriaCon.commit()
            
            self.cargarDatos()
            self.txtNombres.setText("")
            self.txtApellidos.setText("")
        else:
            self.lblMensaje.setText("Debe llenar todos los campos")
            
    def reporteAutor(self):
        nombreArchivo = "reporte_autores.pdf"
        # imagen = "cambio.png"
        titulo = "REPORTE AUTORES"
        encabezado = "ID AUTOR      NOMBRES      APELLIDOS               ESTADO"
        lineas = [encabezado]
        miLibreriaCon = connector.connect(host= "localhost",
                                        user = "root",
                                        password = "",
                                        database = "libreriajsse2614986"
                                        )
        myCursosr = miLibreriaCon.cursor()
        stmt = "SELECT * FROM autores"
        myCursosr.execute(stmt)
        registros = myCursosr.fetchall() #reportlab,html12pdf, fpdf
        
        for registro in registros:
            linea =f"{registro[0]:5d} {registro[1]:13s} {registro[2]:20s} {registro[3]}"
            lineas.append(linea)
            
            # print(f"""
            #       TItulo:{titulo}
            #       Cuerpo:
            #             lineas""")
            
            # configuracion del canvas (lienzo)
            pdf = canvas.Canvas(nombreArchivo)
            pdf.setTitle(titulo)
            pdf.setFillColorRGB(0,0,0)
            pdf.setFont("Courier", 24)
            pdf.drawCentredString(290,720, titulo)
            # pdf.setTitle(documentTitle)
            
            pdf.line(30, 710, 550, 710) # coordenadas (x, y)
            
            # crear un texto multilinea utilizando 
            # textline y un ciclo 'for' 
            texto = pdf.beginText(40, 680)
            texto.setFont("Courier", 12)
            texto.setFillColor(colors.green)
            
            # recorrido sobre las lineas creadas previamente
            for linea in lineas:
                texto.textLine(linea)
                
            pdf.drawText(texto)
            
            # dibujar una imagen en una posición (x,y) específica
            # pdf.drawInlineImage(imagen, 475, 750)
            
            pdf.save()