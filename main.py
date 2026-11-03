# mostrar el menu y recibir datos
from base_datos import inicializar_bd
from producto_dao import ProductoDAO
from producto_servicio import ProductoServicio

def main():
    # Inicializar base de datos
    inicializar_bd()
    dao = ProductoDAO()
    servicio = ProductoServicio(dao)

    while True:
        print("\n========================================")
        print("! Sistema de Inventario de Videojuegos !")
        print("========================================")
        print("1. Registrar Videojuego")
        print("2. Mostrar Inventario")
        print("3. Buscar Videojuego Usando ID")
        print("4. Actualizar Videojuego")
        print("5. Eliminar Videojuego")
        print("6. Vender Unidades")
        print("7. Salir")
        opcion = input("\nSeleccione una Opcion (1-7): ").strip()

        if opcion == "1":
            try:
                nombre = input("Ingrese el nombre del videojuego: ")
                precio = int(input("Ingrese el precio: "))
                stock = int(input("Ingrese la cantidad disponible (stock): "))
                servicio.registrar(nombre, precio, stock)
                print("\n¡Producto guardado correctamente!")
            except ValueError as e:
                print(f"\n[Error de validación]: {e}")

        elif opcion == "2":
            productos = servicio.listar_inventario()
            if not productos:
                print("\nEl inventario está vacío.")
            else:
                print("\n--- LISTA DE VIDEOJUEGOS ---")
                for p in productos:
                    print(f"ID: {p.id} | Nombre: {p.nombre} | Precio: ${p.precio} | Stock: {p.stock}")

        elif opcion == "3":
            try:
                p_id = int(input("Ingrese el ID del videojuego a buscar: "))
                p = servicio.buscar_por_id(p_id)
                print(f"\n[Producto Encontrado] -> ID: {p.id} | Nombre: {p.nombre} | Precio: ${p.precio} | Stock: {p.stock}")
            except ValueError as e:
                print(f"\n[Error]: {e}")

        elif opcion == "4":
            try:
                p_id = int(input("Ingrese el ID del videojuego a actualizar: "))
                # Verificamos que exista primero
                servicio.buscar_por_id(p_id)
                nombre = input("Ingrese el nuevo nombre: ")
                precio = int(input("Ingrese el nuevo precio: "))
                stock = int(input("Ingrese el nuevo stock: "))
                servicio.actualizar(p_id, nombre, precio, stock)
                print("\n¡Producto actualizado correctamente!")
            except ValueError as e:
                print(f"\n[Error]: {e}")

        elif opcion == "5":
            try:
                p_id = int(input("Ingrese el ID del videojuego a eliminar: "))
                servicio.eliminar(p_id)
                print("\n¡El producto ha sido eliminado del inventario!")
            except ValueError as e:
                print(f"\n[Error]: {e}")

        elif opcion == "6":
            try:
                p_id = int(input("Ingrese el ID del videojuego a vender: "))
                cantidad = int(input("Ingrese la cantidad que desea vender: "))
                p_actualizado = servicio.vender(p_id, cantidad)
                print(f"\nVenta realizada con éxito. El nuevo stock de '{p_actualizado.nombre}' es: {p_actualizado.stock}")
            except ValueError as e:
                print(f"\n[Error]: {e}")

        elif opcion == "7":
            print("\nSaliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("\n[Opción inválida]. Por favor, ingrese un número entre 1 y 7.")

if __name__ == "__main__":
    main()