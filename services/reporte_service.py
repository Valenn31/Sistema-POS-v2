"""
Servicio de reportes para el sistema POS
Preparado para futuras funcionalidades de análisis y reportes
"""
from models.producto import Producto
from database.db import get_connection

class ReporteService:
    @staticmethod
    def obtener_productos_sin_stock():
        """Obtiene productos sin stock disponible"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, codigo, nombre, precio, stock FROM productos WHERE stock <= 0")
        productos_data = cursor.fetchall()
        conn.close()
        return productos_data
    
    @staticmethod
    def contar_productos_disponibles():
        """Cuenta los productos con stock disponible"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM productos WHERE stock > 0")
        count = cursor.fetchone()[0]
        conn.close()
        return count
    
    @staticmethod
    def obtener_valor_total_inventario():
        """Calcula el valor total del inventario"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(precio * stock) FROM productos WHERE stock > 0")
        result = cursor.fetchone()[0]
        conn.close()
        return result if result else 0.0
