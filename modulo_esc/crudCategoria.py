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

class DlgCrudCategorias(QMainWindow):
    def __init__(self,dlgPrincipal):
        super(DlgCrudCategorias,self).__init__()
        loadUi('uis/crudCategorias.ui',self)
        self.dlgPrincipal = dlgPrincipal
        
    
        nombreColumnas = ['id_categoria','Categoria','Estado']
        self.tblWdgtUsuarios.setColumnCount(len(nombreColumnas))
        self.tblWdgtUsuarios.setHorizontalHeaderLabels(nombreColumnas)
        
        self.cargarDatos()
        self.btnInsertar.clicked.connect(self.insertar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnActualizar.clicked.connect(self.actualizar)
        self.tblWdgtUsuarios.clicked.connect(self.filaElegida)
        self.btnReporte.clicked.connect(self.reporteCategorias)
        
        
    def cargarDatos(self):
        miLibreriaCon = connector.connect(host = 'localhost',
                                        user = 'root',
                                        password = '',
                                        database = 'libreriajsse2614986')
        myCursor = miLibreriaCon.cursor()
        stmt = f"""SELECT id_categoria,categoria,estado FROM categorias"""
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
        idCategoria = self.tblWdgtUsuarios.item(fila, 0)
        categoria = self.tblWdgtUsuarios.item(fila, 1)
        estado = self.tblWdgtUsuarios.item(fila, 2)
        
        self.spIdCategoria.setValue(int(idCategoria.text()))
        self.txtCategoria.setText(categoria.text())
        self.txtEstado.setText(estado.text())
        
    def actualizar(self):
        if self.txtCategoria.text() !="" and self.txtEstado.text() !="":
            idCategoria = self.spIdCategoria.value()
            categoria = self.txtCategoria.text()
            estado = self.txtEstado.text()
            miLibreriaCon = connector.connect(host = 'localhost',
                                            user = 'root',
                                            password = '',
                                            database = 'libreriajsse2614986')
            myCursor = miLibreriaCon.cursor()
            stmtUpdate = f"""UPDATE categorias SET
                            categoria = '{categoria}',
                            estado = '{estado}'
                        WHERE id_categoria ='{idCategoria}'"""
            myCursor.execute(stmtUpdate)
            miLibreriaCon.commit()
            
            self.cargarDatos()
            self.txtCategoria.setText("")
            self.txtEstado.setText("")
            
            
    def eliminar(self):
        if self.txtCategoria.text() !="" and self.txtEstado.text() !="":
            idCategoria = self.spIdCategoria.value()
            miLibreriaCon = connector.connect(host = 'localhost',
                                            user = 'root',
                                            password = '',
                                            database = 'libreriajsse2614986')
            myCursor = miLibreriaCon.cursor()
            stmtDelete = f"""DELETE FROM categorias
                        WHERE id_categoria ='{idCategoria}'"""
            myCursor.execute(stmtDelete)
            miLibreriaCon.commit()
            
            self.cargarDatos()
            self.txtCategoria.setText("")
            self.txtEstado.setText("")
            
            
    def insertar(self):
        if self.txtCategoria.text() !="" and self.txtEstado.text() !="":
            categoria = self.txtCategoria.text()
            estado = self.txtEstado.text()
            miLibreriaCon = connector.connect(host = 'localhost',
                                            user = 'root',
                                            password = '',
                                            database = 'libreriajsse2614986')
            myCursor = miLibreriaCon.cursor()
            stmtInsertar = f"""INSERT INTO Categorias (categoria,estado)
            VALUES('{categoria}','{estado}')"""
                            
            myCursor.execute(stmtInsertar)
            miLibreriaCon.commit()
            
            self.cargarDatos()
            self.txtCategoria.setText("")
            self.txtEstado.setText("")
        else:
            self.lblMensaje.setText("Debe llenar todos los campos")
            
    def reporteCategorias(self):
        nombreArchivo = "reporte categorias.pdf"
        # imagen = "cambio.png"
        titulo = "Reporte Categorias"
        encabezado = "ID CATEGORIA     CATEGORIA      ESTADO"
        lineas = [encabezado]
        miLibreriaCon = connector.connect(host= "localhost",
                                        user = "root",
                                        password = "",
                                        database = "libreriajsse2614986"
                                        )
        myCursosr = miLibreriaCon.cursor()
        stmt = "SELECT * FROM categorias"
        myCursosr.execute(stmt)
        registros = myCursosr.fetchall() #reportlab,html12pdf, fpdf
        
        for registro in registros:
            linea =f"{registro[0]} {registro[1]} {registro[2]}"
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