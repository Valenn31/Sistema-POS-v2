"""
Componente del frame del carrito - Carrito de compras y cobro
"""
import tkinter as tk
from utils.constants import (
    CARRITO_WIDTH, FONT_TOTAL, COLOR_COBRAR_BG, COLOR_COBRAR_FG,
    TEXTO_CARRITO, TEXTO_TOTAL, TEXTO_COBRAR
)

class FrameCarrito:
    def __init__(self, parent, callback_cobrar):
        self.parent = parent
        self.callback_cobrar = callback_cobrar
        self.frame = None
        self.lista_carrito = None
        self.total_var = None
        
    def crear(self):
        """Crea el frame del carrito de compras"""
        self.frame = tk.Frame(self.parent)
        self.frame.pack(side="right", fill="y")
        
        # Variable para mostrar el total
        self.total_var = tk.StringVar(value="0.00")
        
        # Título del carrito
        tk.Label(self.frame, text=TEXTO_CARRITO).pack()
        
        # Lista del carrito
        self.lista_carrito = tk.Listbox(self.frame, width=CARRITO_WIDTH)
        self.lista_carrito.pack(pady=(0, 10))
        
        # Etiqueta del total
        tk.Label(self.frame, text=TEXTO_TOTAL).pack()
        
        # Valor del total
        tk.Label(
            self.frame, 
            textvariable=self.total_var, 
            font=FONT_TOTAL
        ).pack()
        
        # Botón de cobrar
        tk.Button(
            self.frame, 
            text=TEXTO_COBRAR, 
            command=self.callback_cobrar,
            bg=COLOR_COBRAR_BG, 
            fg=COLOR_COBRAR_FG
        ).pack(pady=10)
        
        return self.frame
    
    def actualizar_carrito(self, items, total):
        """Actualiza la visualización del carrito"""
        # Limpiar lista actual
        self.lista_carrito.delete(0, tk.END)
        
        # Agregar items al carrito
        for item in items:
            self.lista_carrito.insert(tk.END, f"{item.nombre} - ${item.precio:.2f}")
        
        # Actualizar total
        self.total_var.set(f"{total:.2f}")
    
    def limpiar_carrito(self):
        """Limpia la visualización del carrito"""
        self.lista_carrito.delete(0, tk.END)
        self.total_var.set("0.00")
