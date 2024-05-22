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

class DlgCrudLibros(QMainWindow):
    def __init__(self,dlgPrincipal):
        super(DlgCrudLibros,self).__init__()
        loadUi('uis/crudLibro.ui',self)
        self.dlgPrincipal = dlgPrincipal
        
    
        nombreColumnas = ['Isbn','Titulo','Fecha publicacion','Categoria','Precio','Portada','Cantidad en stock','Estado']
        self.tblWdgtUsuarios.setColumnCount(len(nombreColumnas))
        self.tblWdgtUsuarios.setHorizontalHeaderLabels(nombreColumnas)
        
        self.cargarDatos()
        self.btnInsertar.clicked.connect(self.insertar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnActualizar.clicked.connect(self.actualizar)
        self.tblWdgtUsuarios.clicked.connect(self.filaElegida)
        self.btnReporte.clicked.connect(self.generarReporte)
        
        
    def cargarDatos(self):
        miLibreriaCon = connector.connect(host = 'localhost',
                                        user = 'root',
                                        password = '',
                                        database = 'libreriajsse2614986')
        myCursor = miLibreriaCon.cursor()
        stmt = f"""SELECT isbn,titulo,fecha_pub,b.categoria,precio,portada,cantidad_stock,a.estado FROM libros a
                    inner join categorias b on a.categoria = b.id_categoria"""
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
                self.tblWdgtUsuarios.setItem(f, 3, QtWidgets.QTableWidgetItem(str(fila[3])))
                self.tblWdgtUsuarios.setItem(f, 4, QtWidgets.QTableWidgetItem(str(fila[4])))
                self.tblWdgtUsuarios.setItem(f, 5, QtWidgets.QTableWidgetItem(str(fila[5])))
                self.tblWdgtUsuarios.setItem(f, 6, QtWidgets.QTableWidgetItem(str(fila[6])))
                self.tblWdgtUsuarios.setItem(f, 7, QtWidgets.QTableWidgetItem(fila[7]))
                
                f +=1


    def filaElegida(self):
        fila = self.tblWdgtUsuarios.currentRow()
        isbn = self.tblWdgtUsuarios.item(fila, 0)
        titulo = self.tblWdgtUsuarios.item(fila,1)
        fechaPub = self.tblWdgtUsuarios.item(fila, 2)
        categoria = self.tblWdgtUsuarios.item(fila, 3)
        precio = self.tblWdgtUsuarios.item(fila, 4)
        portada = self.tblWdgtUsuarios.item(fila, 5)
        cantidadStock = self.tblWdgtUsuarios.item(fila, 6)
        estado = self.tblWdgtUsuarios.item(fila, 7)
        
        self.txtIsbn.setText(isbn.text())
        self.txtTitulo.setText(titulo.text())
        self.txtFechaPub.setText(fechaPub.text())
        self.txtCategoria.setText(categoria.text())
        self.txtPrecio.setText(precio.text())
        self.txtPortada.setText(portada.text())
        self.txtCantidadStock.setText(cantidadStock.text())
        self.txtEstado.setText(estado.text())

    def actualizar(self):
        if self.txtIsbn.text() !="" and self.txtTitulo.text() !="" and self.txtFechaPub.text() !="" and self.txtCategoria.text() !="" and self.txtPrecio.text() !="" and self.txtPortada.text() != "" and self.txtCantidadStock.text() != "" and self.txtEstado.text() != "":
            isbn = self.txtIsbn.text()
            titulo = self.txtTitulo.text()
            fechaPub = self.txtFechaPub.text()
            categoria = self.txtCategoria.text()
            precio = self.txtPrecio.text()
            portada = self.txtPortada.text()
            cantidadStock = self.txtCantidadStock.text()
            estado = self.txtEstado.text()
            
            miLibreriaCon = connector.connect(host = 'localhost',
                                            user = 'root',
                                            password = '',
                                            database = 'libreriajsse2614986')
            myCursor = miLibreriaCon.cursor()
            stmtUpdate = f"""UPDATE libros SET
                            titulo = '{titulo}',
                            fecha_pub = '{fechaPub}',
                            categoria = '{categoria}',
                            precio = '{precio}',
                            portada = '{portada}',
                            cantidad_stock = '{cantidadStock}',
                            estado='{estado}'
                            WHERE isbn ='{isbn}'"""
            myCursor.execute(stmtUpdate)
            miLibreriaCon.commit()
            
            self.cargarDatos()
            self.txtIsbn.setText("")
            self.txtTitulo.setText("")
            self.txtFechaPub.setText("")
            self.txtCategoria.setText("")
            self.txtPrecio.setText("")
            self.txtPortada.setText("")
            self.txtCantidadStock.setText("")
            self.txtEstado.setText("")
            
    def eliminar(self):
        if self.txtIsbn.text() !="" and self.txtTitulo.text() !="" and self.txtFechaPub.text() !="" and self.txtCategoria.text() !="" and self.txtPrecio.text() !="" and self.txtPortada.text() != "" and self.txtCantidadStock.text() != "" and self.txtEstado.text() != "":
            isbn = self.txtIsbn.text()
            miLibreriaCon = connector.connect(host = 'localhost',
                                            user = 'root',
                                            password = '',
                                            database = 'libreriajsse2614986')
            myCursor = miLibreriaCon.cursor()
            stmtDelete = f"""DELETE FROM libros
                        WHERE isbn ='{isbn}'"""
            myCursor.execute(stmtDelete)
            miLibreriaCon.commit()
            
            self.cargarDatos()
            self.txtIsbn.setText("")
            self.txtTitulo.setText("")
            self.txtFechaPub.setText("")
            self.txtCategoria.setText("")
            self.txtPrecio.setText("")
            self.txtPortada.setText("")
            self.txtCantidadStock.setText("")
            self.txtEstado.setText("")
            
    def insertar(self):
        if self.txtIsbn.text() !="" and self.txtTitulo.text() !="" and self.txtFechaPub.text() !="" and self.txtCategoria.text() !="" and self.txtPrecio.text() !="" and self.txtPortada.text() != "" and self.txtCantidadStock.text() != "" and self.txtEstado.text() != "":
            isbn = self.txtIsbn.text()
            titulo = self.txtTitulo.text()
            fechaPub = self.txtFechaPub.text()
            categoria = self.txtCategoria.text()
            precio = self.txtPrecio.text()
            portada = self.txtPortada.text()
            cantidadStock = self.txtCantidadStock.text()
            estado = self.txtEstado.text()
            miLibreriaCon = connector.connect(host = 'localhost',
                                            user = 'root',
                                            password = '',
                                            database = 'libreriajsse2614986')
            myCursor = miLibreriaCon.cursor()
            stmtInsertar = f"""INSERT INTO libros (isbn,titulo,fecha_pub,categoria,precio,precio,portada,cantidad_stock,estado)
            VALUES('{isbn}','{titulo}','{fechaPub}','{categoria}','{precio}','{portada}','{cantidadStock}','{estado}')"""
                            
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
            
    def generarReporte(self):
        nombreArchivo = "reporteLibros.pdf"

        titulo = "Reporte de Libros"
        encabezado = "ISBN | TITULO | FECHA PUBLICACIÓN | CATEGORIA | PRECIO | PORTADA | CANTIDAD STOCK | ESTADO"
        lineas = [encabezado]
        libreria = connector.connect(host = "localhost", user="root", password="", database="libreriajsse2614986")
        stmt = f"""SELECT isbn, titulo, fecha_pub, categoria, precio, portada, cantidad_stock, estado FROM libros"""

        micursor = libreria.cursor()
        micursor.execute(stmt)
        registros = micursor.fetchall()

        for registro in registros:
            linea = f"{registro[0]} | {registro[1]} | {registro[2]} | {registro[3]} | {registro[4]} | {registro[5]} | {registro[6]} | {registro[7]}"
            lineas.append(linea)

        print(f"""Titulo: {titulo} Cuerpo: {lineas}""")

        pdf = canvas.Canvas(nombreArchivo)
        pdf.setTitle(titulo)
        pdf.setFillColor(colors.black)
        pdf.setFont("Courier", 12)
        pdf.drawCentredString(300, 770, titulo)

        pdf.line(30, 760, 550, 760)

        texto = pdf.beginText(40, 740)
        texto.setFont("Courier", 9)
        texto.setFillColor(colors.black)

        for linea in lineas:
            texto.textLine(linea)

        pdf.drawText(texto)

        pdf.save()