"""
Vista principal del sistema POS
"""
import tkinter as tk

class POSView:
    def __init__(self, controller):
        self.controller = controller
        self.ventana = None
        self.entrada_codigo = None
        self.lista_carrito = None
        self.total_var = None
        self.frame_productos = None
        
    def crear_interfaz(self):
        """Crea la interfaz principal del POS"""
        self.ventana = tk.Toplevel()
        self.ventana.title("Punto de Venta")
        self.ventana.geometry("600x400")
        
        # Variable para mostrar el total
        self.total_var = tk.StringVar(value="0.00")
        
        self._crear_frame_superior()
        self._crear_frame_productos()
        self._crear_frame_carrito()
        self._cargar_productos()
        
        # Enfocar la entrada de código
        self.entrada_codigo.focus()
    
    def _crear_frame_superior(self):
        """Crea el frame superior con la entrada de código"""
        frame_superior = tk.Frame(self.ventana)
        frame_superior.pack(fill="x", pady=5)
        
        tk.Label(frame_superior, text="Escanear o ingresar código:").pack(side="left", padx=5)
        self.entrada_codigo = tk.Entry(frame_superior, width=20)
        self.entrada_codigo.pack(side="left")
        self.entrada_codigo.bind("<Return>", self._manejar_codigo)
    
    def _crear_frame_productos(self):
        """Crea el frame para mostrar los productos disponibles"""
        self.frame_productos = tk.Frame(self.ventana)
        self.frame_productos.pack(side="left", fill="both", expand=True)
    
    def _crear_frame_carrito(self):
        """Crea el frame del carrito de compras"""
        frame_derecho = tk.Frame(self.ventana)
        frame_derecho.pack(side="right", fill="y")
        
        tk.Label(frame_derecho, text="Carrito").pack()
        self.lista_carrito = tk.Listbox(frame_derecho, width=30)
        self.lista_carrito.pack()
        
        tk.Label(frame_derecho, text="Total: $").pack()
        tk.Label(frame_derecho, textvariable=self.total_var, font=("Arial", 14, "bold")).pack()
        
        tk.Button(frame_derecho, text="Cobrar", command=self._cobrar, 
                 bg="green", fg="white").pack(pady=10)
    
    def _cargar_productos(self):
        """Carga los botones de productos en la interfaz"""
        productos = self.controller.obtener_productos()
        for producto in productos:
            btn = tk.Button(self.frame_productos, 
                          text=str(producto),
                          command=lambda p=producto: self.controller.agregar_producto_al_carrito(p),
                          anchor="w", justify="left")
            btn.pack(fill="x")
    
    def _manejar_codigo(self, event=None):
        """Maneja la entrada de código por teclado o escáner"""
        codigo = self.entrada_codigo.get()
        if self.controller.buscar_producto_por_codigo(codigo):
            self.entrada_codigo.delete(0, tk.END)
        else:
            self.entrada_codigo.select_range(0, tk.END)
    
    def _cobrar(self):
        """Maneja el proceso de cobro"""
        self.controller.procesar_cobro()
    
    def actualizar_carrito(self, carrito):
        """Actualiza la visualización del carrito"""
        items = carrito.obtener_items()
        
        # Actualizar lista del carrito
        self.lista_carrito.delete(0, tk.END)
        for item in items:
            self.lista_carrito.insert(tk.END, f"{item.nombre} - ${item.precio:.2f}")
        
        # Actualizar total
        total = carrito.calcular_total()
        self.total_var.set(f"{total:.2f}")
    
    def limpiar_carrito(self):
        """Limpia la visualización del carrito"""
        self.lista_carrito.delete(0, tk.END)
        self.total_var.set("0.00")
