#
# @autor: Jhon Sebastian Serna
# @fecha: 2023/11/17
# @descripción: programa principal de la aplicacion de escritorio
#

# librerias propias de python
from mysql import connector

# librerias QtDesigner
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

# Importaciones de módulos
from modulo_esc.crudAutor import DlgCrudAutores
from modulo_esc.crudClientes import DlgCrudClientes
from modulo_esc.crudPedidos import DlgCrudPedidos
from modulo_esc.crudLibros import DlgCrudLibros
from modulo_esc.crudCategoria import DlgCrudCategorias


class DlgPrincipal(QMainWindow):
    def __init__(self,dlgIniciar,usuario):
        super(DlgPrincipal,self).__init__()
        loadUi('uis/paginaPrincipal.ui',self)
        self.dlgIniciar=dlgIniciar
        self.usuario = usuario
        self.lblUsuario.setText(usuario["usuario"])
        
        self.btnAutores.clicked.connect(self.autores)
        self.btnClientes.clicked.connect(self.clientes)
        self.btnPedidos.clicked.connect(self.pedidos)
        self.btnLibros.clicked.connect(self.libros)
        self.btnCategorias.clicked.connect(self.categorias)
        
        
    def clientes(self):
        self.dlgClientes = DlgCrudClientes(self)
        self.dlgClientes.show()  
        
        
    def autores(self):
        self.dlgAutores = DlgCrudAutores(self)
        self.dlgAutores.show()
    
    
    def categorias(self):
        self.dlgCategorias = DlgCrudCategorias(self)
        self.dlgCategorias.show()
          
        
    def libros(self):
        self.dlgLibros = DlgCrudLibros(self)
        self.dlgLibros.show()
        
    
    def pedidos(self):
        self.dlgPedidos = DlgCrudPedidos(self)
        self.dlgPedidos.show()