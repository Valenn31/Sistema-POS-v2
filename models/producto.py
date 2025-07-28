"""
Modelo para el manejo de productos en el sistema POS
"""
from database.db import get_connection

class Producto:
    def __init__(self, id=None, codigo=None, nombre=None, precio=None, stock=None):
        self.id = id
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    @classmethod
    def obtener_todos(cls):
        """Obtiene todos los productos con stock disponible"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, codigo, nombre, precio FROM productos WHERE stock > 0")
        productos_data = cursor.fetchall()
        conn.close()
        
        productos = []
        for data in productos_data:
            producto = cls(id=data[0], codigo=data[1], nombre=data[2], precio=data[3])
            productos.append(producto)
        
        return productos
    
    @classmethod
    def buscar_por_codigo(cls, codigo):
        """Busca un producto por su código"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, codigo, nombre, precio FROM productos WHERE codigo = ?", (codigo,))
        data = cursor.fetchone()
        conn.close()
        
        if data:
            return cls(id=data[0], codigo=data[1], nombre=data[2], precio=data[3])
        return None
    
    def to_tuple(self):
        """Convierte el producto a tupla para compatibilidad con código existente"""
        return (self.id, self.codigo, self.nombre, self.precio)
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre} - ${self.precio:.2f}"
