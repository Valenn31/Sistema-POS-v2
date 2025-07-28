"""
Componente del frame superior - Entrada de código de barras
"""
import tkinter as tk
from utils.constants import ENTRADA_CODIGO_WIDTH, TEXTO_ESCANEAR

class FrameSuperior:
    def __init__(self, parent, callback_codigo):
        self.parent = parent
        self.callback_codigo = callback_codigo
        self.frame = None
        self.entrada_codigo = None
        
    def crear(self):
        """Crea el frame superior con la entrada de código"""
        self.frame = tk.Frame(self.parent)
        self.frame.pack(fill="x", pady=5)
        
        tk.Label(self.frame, text=TEXTO_ESCANEAR).pack(side="left", padx=5)
        
        self.entrada_codigo = tk.Entry(self.frame, width=ENTRADA_CODIGO_WIDTH)
        self.entrada_codigo.pack(side="left")
        self.entrada_codigo.bind("<Return>", self._manejar_codigo)
        
        return self.frame
    
    def _manejar_codigo(self, event=None):
        """Maneja la entrada de código por teclado o escáner"""
        codigo = self.entrada_codigo.get()
        if self.callback_codigo(codigo):
            self.entrada_codigo.delete(0, tk.END)
        else:
            self.entrada_codigo.select_range(0, tk.END)
    
    def enfocar(self):
        """Enfoca la entrada de código"""
        if self.entrada_codigo:
            self.entrada_codigo.focus()
    
    def limpiar(self):
        """Limpia la entrada de código"""
        if self.entrada_codigo:
            self.entrada_codigo.delete(0, tk.END)
