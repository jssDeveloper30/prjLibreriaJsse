#
# @autor: Jhon Sebastian Serna
# @fecha: 2023/11/17
# @descripción: programa principal de la libreria
#

# módulo de python
import mysql.connector
import sys

# módulos de PyQt
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.uic import loadUi

# importaciones de módulos
# from modulo_esc.crudAutor import DlgCrudAutores
from modulo_esc.principal import DlgPrincipal

class DlgIniciar(QMainWindow):
    def __init__(self):
        super(DlgIniciar, self).__init__()
        loadUi('uis/inicio.ui', self)
        self.btnInicio.clicked.connect(self.iniciarSesion)
        

    def iniciarSesion(self):
        txtUsu = self.txtUsuario.text()
        pwdCla = self.txtClave.text()

        miLibreria = mysql.connector.connect(host='localhost', user='root', password='', database='libreriajsse2614986')
        stmt = f"""SELECT id_usuario, usuario, contrasena FROM usuarios WHERE usuario= '{txtUsu}' AND contrasena = '{pwdCla}'"""
        
        miCursor= miLibreria.cursor()
        miCursor.execute(stmt)
        registro = miCursor.fetchall()
   
        if registro:
            usuario ={'id_usuario': registro[0][0],'usuario': registro[0][1], 'contrasena': registro[0][2]}
            self.dlgPrincipal = DlgPrincipal(self,usuario)
            self.dlgPrincipal.show()
            dlgIniciar.close()
        else:
            self.lblMensaje.setText("Usuario o Contraseña incorrecta..." + str(registro))
    

app = QApplication(sys.argv)
dlgIniciar = DlgIniciar()
dlgIniciar.show()
sys.exit(app.exec_())