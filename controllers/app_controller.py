"""
Controlador principal de la aplicación
Maneja la coordinación entre vistas y controladores
"""
from views.pos_view import POSView
from controllers.pos_controller import POSController

class AppController:
    def __init__(self):
        self.pos_view = None
        self.pos_controller = None
    
    def crear_pos(self):
        """Crea y configura el sistema POS con arquitectura MVC correcta"""
        # Crear vista sin controlador inicialmente
        self.pos_view = POSView()
        
        # Crear controlador pasándole la vista
        self.pos_controller = POSController(self.pos_view)
        
        # Asignar controlador a la vista (completar la conexión bidireccional)
        self.pos_view.set_controller(self.pos_controller)
        
        # Crear la interfaz
        self.pos_view.crear_interfaz()
        
        return self.pos_view, self.pos_controller
