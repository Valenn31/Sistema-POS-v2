"""
Componente del frame de productos - Lista de productos disponibles
"""
import tkinter as tk

class FrameProductos:
    def __init__(self, parent, callback_producto):
        self.parent = parent
        self.callback_producto = callback_producto
        self.frame = None
        
    def crear(self):
        """Crea el frame para mostrar los productos disponibles"""
        self.frame = tk.Frame(self.parent)
        self.frame.pack(side="left", fill="both", expand=True)
        return self.frame
    
    def cargar_productos(self, productos):
        """Carga los botones de productos en la interfaz"""
        # Limpiar productos existentes
        for widget in self.frame.winfo_children():
            widget.destroy()
        
        # Crear botón para cada producto
        for producto in productos:
            btn = tk.Button(
                self.frame, 
                text=str(producto),
                command=lambda p=producto: self.callback_producto(p),
                anchor="w", 
                justify="left"
            )
            btn.pack(fill="x", padx=2, pady=1)
    
    def actualizar_productos(self, productos):
        """Actualiza la lista de productos mostrados"""
        self.cargar_productos(productos)
