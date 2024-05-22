from PyQt5.QtWidgets import QMainWindow
from mysql import connector

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMainWindow
from datetime import datetime
from PyQt5.uic import loadUi


from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from PyQt5.uic import loadUi

class DlgCrudPedidos(QMainWindow):
    def __init__(self,dlgPrincipal):
        super(DlgCrudPedidos,self).__init__()
        loadUi('uis/crudPedidos.ui',self)
        self.dlgPrincipal = dlgPrincipal
        
    
        nombreColumnas = ['Id pedido','Nro Pedido','id_cliente','isbn','Fecha de pedido','cantidad','subtotal','estado']
        self.tblWdgtUsuarios.setColumnCount(len(nombreColumnas))
        self.tblWdgtUsuarios.setHorizontalHeaderLabels(nombreColumnas)
        
        self.cargarDatos()
        self.btnInsertar.clicked.connect(self.insertar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnActualizar.clicked.connect(self.actualizar)
        self.tblWdgtUsuarios.clicked.connect(self.filaElegida)
        self.btnReporte.clicked.connect(self.reporteUsuario)
        
        
    def cargarDatos(self):
        print("Cargando datos...")
        try:
            miLibreriaCon = connector.connect(host = 'localhost',
                                            user = 'root',
                                            password = '',
                                            database = 'libreriajsse2614986')
            myCursor = miLibreriaCon.cursor()
            stmt = f"""SELECT id_pedido,nro_pedido,id_cliente,isbn,fecha_pedido,cantidad,subtotal,estado FROM tbl_pedido_cliente"""
            myCursor.execute(stmt)
            filas = myCursor.fetchall()
        except Exception as e:
            print(f"error: {e}")
        
        nroFilas = len(filas)
        self.tblWdgtUsuarios.setRowCount(nroFilas)
        f = 0
        
        if filas:
            for fila in filas:
                self.tblWdgtUsuarios.setItem(f, 0, QtWidgets.QTableWidgetItem(str(fila[0])))    
                self.tblWdgtUsuarios.setItem(f, 1, QtWidgets.QTableWidgetItem(str(fila[1])))
                self.tblWdgtUsuarios.setItem(f, 2, QtWidgets.QTableWidgetItem(str(fila[2])))
                self.tblWdgtUsuarios.setItem(f, 3, QtWidgets.QTableWidgetItem(str(fila[3])))
                self.tblWdgtUsuarios.setItem(f, 4, QtWidgets.QTableWidgetItem(str(fila[4])))
                self.tblWdgtUsuarios.setItem(f, 5, QtWidgets.QTableWidgetItem(str(fila[5])))
                self.tblWdgtUsuarios.setItem(f, 6, QtWidgets.QTableWidgetItem(str(fila[6])))
                self.tblWdgtUsuarios.setItem(f, 7, QtWidgets.QTableWidgetItem(fila[7]))
                self.tblWdgtUsuarios.repaint()
                f +=1


    def filaElegida(self):
        print("Fila elegida...")
        fila = self.tblWdgtUsuarios.currentRow()
        idPedido = self.tblWdgtUsuarios.item(fila,0)
        nroPedido = self.tblWdgtUsuarios.item(fila, 1)
        idCliente = self.tblWdgtUsuarios.item(fila, 2)
        isbn = self.tblWdgtUsuarios.item(fila, 3)
        fechaPedido = self.tblWdgtUsuarios.item(fila, 4)
        cantidad = self.tblWdgtUsuarios.item(fila, 5)
        subtotal = self.tblWdgtUsuarios.item(fila, 6)
        estado = self.tblWdgtUsuarios.item(fila, 7)
        
        
        self.spIdPedido.setValue(int(idPedido.text()))
        self.txtNroPedido.setText(nroPedido.text())
        self.txtIdCliente.setText(idCliente.text())
        self.txtIsbn.setText(isbn.text())
        self.txtFechaPedido.setText(fechaPedido.text())
        self.txtCantidad.setText(cantidad.text())
        self.txtSubtotal.setText(subtotal.text())
        self.txtEstado.setText(estado.text())
        
    def actualizar(self):
        if self.txtNroPedido.text() !="" and self.txtFechaPedido.text() !="" and self.txtCantidad.text() !="" and self.txtSubtotal.text() !="" and self.txtEstado.text() !="": 
            idPedido = self.spIdPedido.value()
            nroPedido = self.txtNroPedido.text()
            fechaPedido = self.txtFechaPedido.text()
            cantidad = self.txtCantidad.text()
            subtotal = self.txtSubtotal.text()
            estado = self.txtEstado.text()
            miLibreriaCon = connector.connect(host = 'localhost',
                                            user = 'root',
                                            password = '',
                                            database = 'libreriajsse2614986')
            myCursor = miLibreriaCon.cursor()
            stmtUpdate = f"""UPDATE tbl_pedido_cliente SET
                            nro_pedido= '{nroPedido}',
                            fecha_pedido = '{fechaPedido}',
                            cantidad = '{cantidad}',
                            subtotal = '{subtotal}',
                            estado = '{estado}'
                        WHERE id_pedido ='{idPedido}'"""
            myCursor.execute(stmtUpdate)
            miLibreriaCon.commit()
            
            self.cargarDatos()
            self.txtNroPedido.setText("")
            self.txtIdCliente.setText("")
            self.txtIsbn.setText("")
            self.txtFechaPedido.setText("")
            self.txtCantidad.setText("")
            self.txtSubtotal.setText("")
            self.txtEstado.setText("")
            
    def eliminar(self):
        if self.txtNroPedido.text() !="" and self.txtFechaPedido.text() !="" and self.txtCantidad.text() !="" and self.txtSubtotal.text() !="" and self.txtEstado.text() !="":
            idPedido = self.spIdPedido.value()
            miLibreriaCon = connector.connect(host = 'localhost',
                                            user = 'root',
                                            password = '',
                                            database = 'libreriajsse2614986')
            myCursor = miLibreriaCon.cursor()
            stmtDelete = f"""DELETE FROM tbl_pedido_cliente
                        WHERE id_pedido ='{idPedido}'"""
            myCursor.execute(stmtDelete)
            miLibreriaCon.commit()
            
            self.cargarDatos()
            self.txtNroPedido.setText("")
            self.txtIdCliente.setText("")
            self.txtIsbn.setText("")
            self.txtFechaPedido.setText("")
            self.txtCantidad.setText("")
            self.txtSubtotal.setText("")
            self.txtEstado.setText("")
            
    def insertar(self):
        if self.txtNroPedido.text() !="" and self.txtFechaPedido.text() !="" and self.txtCantidad.text() !="" and self.txtSubtotal.text() !="" and self.txtEstado.text() !="":
            nroPedido = self.txtNroPedido.text()
            idCliente = self.txtIdCliente.text()
            isbn = self.txtIsbn.text()
            fechaPedido = self.txtFechaPedido.text()
            cantidad = self.txtCantidad.text()
            subtotal = self.txtSubtotal.text()
            estado = self.txtEstado.text()
            miLibreriaCon = connector.connect(host = 'localhost',
                                            user = 'root',
                                            password = '',
                                            database = 'libreriajsse2614986')
            myCursor = miLibreriaCon.cursor()
            stmtInsertar = f"""INSERT INTO tbl_pedido_cliente (nro_pedido,id_cliente, isbn, fecha_pedido, cantidad, subtotal,estado)
            VALUES('{nroPedido}','{idCliente}','{isbn}','{fechaPedido}','{cantidad}','{subtotal}','{estado}')"""
                            
            myCursor.execute(stmtInsertar)
            miLibreriaCon.commit()
            
            self.cargarDatos()
            self.txtNroPedido.setText("")
            self.txtIdCliente.setText("")
            self.txtIsbn.setText("")
            self.txtFechaPedido.setText("")
            self.txtCantidad.setText("")
            self.txtSubtotal.setText("")
            self.txtEstado.setText("")
        else:
            self.lblMensaje.setText("Debe llenar todos los campos")
            
    def reporteUsuario(self):
        nombreArchivo = "reporte_pedido_cliente.pdf"
        # imagen = "cambio.png"
        titulo = "REPORTE DE PEDIDO CLIENTE"
        encabezado ="ID PEDIDO NRO PEDIDO ID CLIENTE ISBN FECHA PEDIDO CANTIDAD SUBTOTAL ESTADO"
        lineas = [encabezado]
        miLibreriaCon = connector.connect(host= "localhost",
                                        user = "root",
                                        password = "",
                                        database = "libreriajsse2614986"
                                        )
        myCursosr = miLibreriaCon.cursor()
        stmt = "SELECT * FROM tbl_pedido_cliente"
        myCursosr.execute(stmt)
        registros = myCursosr.fetchall() #reportlab,html12pdf, fpdf
        
        for registro in registros:
            linea =f"     {registro[0]}        {registro[1]}           {registro[2]}     {registro[3]}  {registro[4]}     {registro[5]}     {registro[6]}   {registro[7]}"
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