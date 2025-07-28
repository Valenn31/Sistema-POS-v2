"""
Controlador principal para el sistema POS
"""
from tkinter import messagebox
from models.producto import Producto
from models.carrito import Carrito

class POSController:
    def __init__(self, view):
        self.view = view
        self.carrito = Carrito()
        self.productos = []
        self.cargar_productos()
    
    def cargar_productos(self):
        """Carga todos los productos disponibles"""
        self.productos = Producto.obtener_todos()
    
    def obtener_productos(self):
        """Retorna la lista de productos"""
        return self.productos
    
    def agregar_producto_al_carrito(self, producto):
        """Agrega un producto al carrito y actualiza la vista"""
        self.carrito.agregar_producto(producto)
        self.view.actualizar_carrito(self.carrito)
    
    def buscar_producto_por_codigo(self, codigo):
        """Busca un producto por código y lo agrega al carrito si existe"""
        if not codigo.strip():
            return False
        
        producto = Producto.buscar_por_codigo(codigo.strip())
        if producto:
            self.agregar_producto_al_carrito(producto)
            return True
        else:
            messagebox.showwarning("Producto no encontrado", f"No se encontró el código: {codigo}")
            return False
    
    def procesar_cobro(self):
        """Procesa el cobro y genera el ticket"""
        if self.carrito.esta_vacio():
            messagebox.showinfo("POS", "No hay productos en el carrito.")
            return
        
        ticket_texto = self.carrito.generar_ticket()
        messagebox.showinfo("Ticket", ticket_texto)
        
        # Limpiar carrito después del cobro
        self.carrito.limpiar()
        self.view.limpiar_carrito()
    
    def obtener_total_carrito(self):
        """Obtiene el total actual del carrito"""
        return self.carrito.calcular_total()
