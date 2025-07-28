"""
Vista principal del sistema POS - Refactorizada con componentes
"""
import tkinter as tk
from views.components.frame_superior import FrameSuperior
from views.components.frame_productos import FrameProductos
from views.components.frame_carrito import FrameCarrito
from utils.constants import POS_WINDOW_SIZE, TEXTO_PUNTO_VENTA

class POSView:
    def __init__(self, controller=None):
        self.controller = controller
        self.ventana = None
        
        # Componentes de la interfaz
        self.frame_superior = None
        self.frame_productos = None
        self.frame_carrito = None
        
    def set_controller(self, controller):
        """Asigna el controlador a la vista"""
        self.controller = controller
        
    def crear_interfaz(self):
        """Crea la interfaz principal del POS usando componentes"""
        self.ventana = tk.Toplevel()
        self.ventana.title(TEXTO_PUNTO_VENTA)
        self.ventana.geometry(POS_WINDOW_SIZE)
        
        self._crear_componentes()
        self._cargar_datos_iniciales()
        
        # Enfocar la entrada de código
        self.frame_superior.enfocar()
    
    def _crear_componentes(self):
        """Crea todos los componentes de la interfaz"""
        # Frame superior con entrada de código
        self.frame_superior = FrameSuperior(
            self.ventana, 
            self._manejar_codigo
        )
        self.frame_superior.crear()
        
        # Frame de productos
        self.frame_productos = FrameProductos(
            self.ventana,
            self._agregar_producto
        )
        self.frame_productos.crear()
        
        # Frame del carrito
        self.frame_carrito = FrameCarrito(
            self.ventana,
            self._cobrar
        )
        self.frame_carrito.crear()
    
    def _cargar_datos_iniciales(self):
        """Carga los datos iniciales en la interfaz"""
        if self.controller:
            productos = self.controller.obtener_productos()
            self.frame_productos.cargar_productos(productos)
    
    def _manejar_codigo(self, codigo):
        """Callback para manejar entrada de código"""
        if self.controller:
            return self.controller.buscar_producto_por_codigo(codigo)
        return False
    
    def _agregar_producto(self, producto):
        """Callback para agregar producto al carrito"""
        if self.controller:
            self.controller.agregar_producto_al_carrito(producto)
    
    def _cobrar(self):
        """Callback para procesar el cobro"""
        if self.controller:
            self.controller.procesar_cobro()
    
    def actualizar_carrito(self, carrito):
        """Actualiza la visualización del carrito"""
        items = carrito.obtener_items()
        total = carrito.calcular_total()
        self.frame_carrito.actualizar_carrito(items, total)
    
    def limpiar_carrito(self):
        """Limpia la visualización del carrito"""
        self.frame_carrito.limpiar_carrito()
    
    def actualizar_productos(self):
        """Actualiza la lista de productos mostrados"""
        if self.controller:
            productos = self.controller.obtener_productos()
            self.frame_productos.actualizar_productos(productos)
