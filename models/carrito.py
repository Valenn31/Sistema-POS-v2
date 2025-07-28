"""
Modelo para el manejo del carrito de compras
"""

class Carrito:
    def __init__(self):
        self.items = []
    
    def agregar_producto(self, producto):
        """Agrega un producto al carrito"""
        self.items.append(producto)
    
    def calcular_total(self):
        """Calcula el total del carrito"""
        return sum(item.precio for item in self.items)
    
    def obtener_items(self):
        """Obtiene todos los items del carrito"""
        return self.items
    
    def limpiar(self):
        """Limpia el carrito"""
        self.items.clear()
    
    def esta_vacio(self):
        """Verifica si el carrito está vacío"""
        return len(self.items) == 0
    
    def generar_ticket(self):
        """Genera el texto del ticket de compra"""
        if self.esta_vacio():
            return "No hay productos en el carrito."
        
        lineas = []
        for item in self.items:
            lineas.append(f"{item.nombre} - ${item.precio:.2f}")
        
        lineas.append("")
        lineas.append(f"TOTAL: ${self.calcular_total():.2f}")
        
        return "\n".join(lineas)
