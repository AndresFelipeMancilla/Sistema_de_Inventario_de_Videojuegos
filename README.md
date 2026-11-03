# Sistema de Inventario de Videojuegos

Aplicación de consola desarrollada en Python utilizando una arquitectura por capas (Modelo, DAO, Servicios y Base de Datos) conectada a SQLite, aplicando buenas prácticas y el patrón DAO

## Estructura del Proyecto
- `modelo.py`: Define la clase `Producto`
- `base_datos.py`: Gestiona la conexion con SQLite y crea automáticamente la tabla
- `producto_dao.py`: Contiene las consultas SQL
- `producto_servicio.py`: Maneja las reglas de negocio y las validaciones
- `main.py`: Contiene el menu interactivo de consola

## Cómo Ejecutar
Asegúrate de tener Python instalado y ejecuta el archivo principal:
```bash
python main.py