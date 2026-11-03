# ejecutar las operaciones sql
from base_datos import obtener_conexion
from modelo import Producto

class ProductoDAO:
    
    # 1. crear un producto
    def crear(self, producto):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        
        sql = """ 
            INSERT INTO productos (nombre, precio, stock)
            VALUES (?, ?, ?)
        """
        cursor.execute(sql, (producto.nombre, producto.precio, producto.stock))
        producto.id = cursor.lastrowid
        conexion.commit()
        conexion.close()
        return producto

    # 2. Listar todos los productos
    def obtener_todos(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, precio, stock FROM productos")
        filas = cursor.fetchall()
        conexion.close()
        productos = []
        for fila in filas:
            productos.append(Producto(fila[0], fila[1], fila[2], fila[3]))
        return productos

    # 3. Buscar un Producto por ID
    def obtener_por_id(self, producto_id):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, precio, stock FROM productos WHERE id = ?", (producto_id,))
        fila = cursor.fetchone()
        conexion.close()
        if fila:
            return Producto(fila[0], fila[1], fila[2], fila[3])
        return None

    # 4. Actualizar Producto
    def actualizar(self, producto):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = """
            UPDATE productos 
            SET nombre = ?, precio = ?, stock = ?
            WHERE id = ?
        """
        cursor.execute(sql, (producto.nombre, producto.precio, producto.stock, producto.id))
        conexion.commit()
        conexion.close()

    # 5. Eliminar Producto
    def eliminar(self, producto_id):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
        conexion.commit()
        conexion.close()
        