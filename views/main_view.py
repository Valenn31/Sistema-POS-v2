"""
Vista principal del sistema - Ventana de bienvenida
"""
import tkinter as tk
from views.pos_view import POSView
from controllers.pos_controller import POSController

class MainView:
    def __init__(self):
        self.root = None
    
    def crear_ventana_principal(self):
        """Crea la ventana principal del sistema"""
        self.root = tk.Tk()
        self.root.title("Sistema POS")
        self.root.geometry("300x150")
        
        tk.Label(self.root, text="Bienvenido al Sistema POS", 
                font=("Arial", 12)).pack(pady=10)
        
        tk.Button(self.root, text="Abrir Punto de Venta", 
                 command=self._abrir_pos).pack()
    
    def _abrir_pos(self):
        """Abre la interfaz del punto de venta"""
        # Crear vista del POS
        pos_view = POSView(None)  # Temporalmente None
        
        # Crear controlador y asignarlo a la vista
        pos_controller = POSController(pos_view)
        pos_view.controller = pos_controller
        
        # Crear la interfaz
        pos_view.crear_interfaz()
    
    def iniciar(self):
        """Inicia la aplicación"""
        self.crear_ventana_principal()
        self.root.mainloop()
