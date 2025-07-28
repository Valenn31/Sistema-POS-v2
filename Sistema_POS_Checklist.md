
# ✅ Sistema POS – Checklist Funcionalidades

---

## 🥇 Funciones básicas mínimas (MVP)

### Punto de venta (Interfaz principal)
- [ ] Escanear códigos de barra
- [ ] Buscar productos por nombre
- [ ] Agregar/quitar productos del ticket
- [ ] Cambiar precio unitario del producto
- [ ] Aplicar descuentos / recargos
- [ ] Ver total en tiempo real
- [ ] Cobro (efectivo)
- [ ] Cobro mixto (efectivo + tarjeta)
- [ ] Cargar cliente opcional en ticket
- [ ] Seleccionar tipo de comprobante (Ticket, Factura X, etc.)
- [ ] Imprimir ticket (básico)
- [ ] Abrir caja automática al iniciar POS

### Productos
- [ ] Crear producto nuevo
- [ ] Editar producto
- [ ] Eliminar / Discontinuar producto
- [ ] Control de stock (actual, mínimo, máximo)
- [ ] Asignar producto a departamento/rubro
- [ ] Carga rápida de stock (lectura + cantidad)
- [ ] Precios por lista (minorista, mayorista, etc.)

### Base técnica
- [ ] Creación y conexión con base SQLite
- [ ] Estructura modular (MVC)
- [ ] Gestión de usuarios (admin por defecto)
- [ ] Login con roles

---

## 🥈 Gestión comercial

### Clientes y proveedores
- [ ] Crear cliente
- [ ] Crear proveedor
- [ ] Consultar historial
- [ ] Registrar deudas
- [ ] Ver resumen de cuentas
- [ ] Exportar deudas a Excel

### Compras
- [ ] Registrar nueva compra (productos, proveedor, precios con/sin IVA)
- [ ] Panel con historial de compras
- [ ] Stock automático tras compra

### Ventas
- [ ] Historial de ventas
- [ ] Filtro por fecha
- [ ] Totales por día
- [ ] Descuentos / recargos globales
- [ ] Resumen por método de pago

---

## 🥉 Herramientas administrativas y contables

### Informes
- [ ] Informe de ventas por rubro
- [ ] Informe por artículo
- [ ] Informe por método de pago
- [ ] Informe por fechas

### Caja
- [ ] Apertura y cierre de caja
- [ ] Registro de ingresos/egresos manuales
- [ ] Ver movimientos de caja del día

### Configuración general
- [ ] Datos del local (razón social, CUIT, dirección, etc.)
- [ ] Logo
- [ ] Listas de precios configurables
- [ ] Tarjetas aceptadas
- [ ] Número de punto de venta
- [ ] N° comprobante inicial
- [ ] Texto personalizado en ticket (“Gracias por su compra”)

---

## 🛠️ Opcionales / avanzadas

### Impresora y etiquetas
- [ ] Selección de dispositivo
- [ ] Ancho de ticket (58mm / 80mm)
- [ ] Opción “solo texto”
- [ ] Crear etiquetas con código de barras
- [ ] Etiquetas por producto (preview, cantidad)
- [ ] Impresión de facturas

### Facturación electrónica
- [ ] Activar integración AFIP
- [ ] Consulta de estado del servicio
- [ ] Emitir factura electrónica al cerrar venta

### Importación / Exportación
- [ ] Importar productos desde Excel
- [ ] Exportar productos a Excel
- [ ] Actualización masiva de precios por rubro o % general

### Publicación web
- [ ] Opción de publicar productos en la web
- [ ] Departamento "publicado" sí/no
