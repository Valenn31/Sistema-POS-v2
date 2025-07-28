"""
Vista principal del sistema - Ventana de bienvenida
"""
import tkinter as tk
from controllers.app_controller import AppController
from utils.constants import (
    MAIN_WINDOW_SIZE, FONT_TITLE, TEXTO_BIENVENIDA, 
    TEXTO_ABRIR_POS, TEXTO_SISTEMA_POS
)

class MainView:
    def __init__(self):
        self.root = None
        self.app_controller = AppController()
    
    def crear_ventana_principal(self):
        """Crea la ventana principal del sistema"""
        self.root = tk.Tk()
        self.root.title(TEXTO_SISTEMA_POS)
        self.root.geometry(MAIN_WINDOW_SIZE)
        
        tk.Label(
            self.root, 
            text=TEXTO_BIENVENIDA, 
            font=FONT_TITLE
        ).pack(pady=10)
        
        tk.Button(
            self.root, 
            text=TEXTO_ABRIR_POS, 
            command=self._abrir_pos
        ).pack()
    
    def _abrir_pos(self):
        """Abre la interfaz del punto de venta usando AppController"""
        self.app_controller.crear_pos()
    
    def iniciar(self):
        """Inicia la aplicación"""
        self.crear_ventana_principal()
        self.root.mainloop()
