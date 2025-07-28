
"""
Sistema POS - Punto de entrada principal
Aplicación refactorizada con arquitectura MVC
"""
from views.main_view import MainView
from database.db import create_tables

def main():
    """Función principal del sistema"""
    # Inicializar base de datos
    create_tables()
    
    # Crear y ejecutar la aplicación
    app = MainView()
    app.iniciar()

if __name__ == "__main__":
    main()
