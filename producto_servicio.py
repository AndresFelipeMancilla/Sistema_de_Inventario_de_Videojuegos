#aplicar las reglas del negocio
from modelo import Producto

class ProductoServicio:
    def __init__(self, dao):
        self.dao = dao

    # 1. REGISTRAR PRODUCTO
    def registrar(self, nombre, precio, stock):
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        producto = Producto(None, nombre.strip(), precio, stock)
        return self.dao.crear(producto)

    # 2. Listado de Inventario
    def listar_inventario(self):
        return self.dao.obtener_todos()

    # 3. Buscar Producto Usando ID
    def buscar_por_id(self, producto_id):
        producto = self.dao.obtener_por_id(producto_id)
        if not producto:
            raise ValueError(f"El videojuego con ID {producto_id} no existe.")
        return producto

    # 4. Actualizar Producto
    def actualizar(self, producto_id, nombre, precio, stock):
        # Verificar si existe
        self.buscar_por_id(producto_id)
        if not nombre or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        producto_actualizado = Producto(producto_id, nombre.strip(), precio, stock)
        self.dao.actualizar(producto_actualizado)
        return producto_actualizado

    # 5. Eliminar Producto
    def eliminar(self, producto_id):
        self.buscar_por_id(producto_id)
        self.dao.eliminar(producto_id)

    # 6. Vender Unidades
    def vender(self, producto_id, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser mayor a cero.")
        producto = self.buscar_por_id(producto_id)
        if cantidad > producto.stock:
            raise ValueError(f"No se puede vender más unidades de las disponibles. Stock actual: {producto.stock}")
        producto.stock -= cantidad
        self.dao.actualizar(producto)
        return producto