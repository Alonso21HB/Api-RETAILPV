from pydantic import BaseModel
from typing import Optional
from datetime import date

# -------------------- Esquema para la tabla pract_03_Data_clientes --------------------
class Cliente(BaseModel):
    id_cliente: Optional[int]  # El cliente puede enviar el ID (opcional)
    nombre: str
    apellido: str
    email: str
    telefono: str
    direccion: str
    fecha_registro: date  # Fecha opcional

    class Config:
        orm_mode = True


# -------------------- Esquema para la tabla pract_03_Data_productos --------------------
class Producto(BaseModel):
    id_producto: Optional[int]  # El cliente puede enviar el ID (opcional)
    nombre: str
    id_categoria: int
    marca: str
    precio: float
    stock: int
    id_proveedor: int
    fechaingreso: date
    tamano: str
    SKU: str

    class Config:
        orm_mode = True


# -------------------- Esquema para la tabla pract_03_Data_sucursales --------------------
class Sucursal(BaseModel):
    id_sucursal: Optional[int]  # El cliente puede enviar el ID (opcional)
    nombre: str
    direccion: str
    ciudad: str
    telefono: str

    class Config:
        orm_mode = True


# -------------------- Esquema para la tabla pract_03_Data_pago --------------------
class Pago(BaseModel):
    id_pago: Optional[int]  # El cliente puede enviar el ID (opcional)
    metodo: str
    monto: float
    fecha_pago: date

    class Config:
        orm_mode = True


# -------------------- Esquema para la tabla pract_03_Data_promociones --------------------
class Promocion(BaseModel):
    id_promocion: Optional[int]  # El cliente puede enviar el ID (opcional)
    descripcion: str
    descuento: float

    class Config:
        orm_mode = True


# -------------------- Esquema para la tabla pract_03_Data_proveedores --------------------
class Proveedor(BaseModel):
    id_proveedor: Optional[int]  # El cliente puede enviar el ID (opcional)
    nombre: str
    contacto: str
    telefono: str
    email: str

    class Config:
        orm_mode = True


# -------------------- Esquema para la tabla pract_03_Data_tiempo --------------------
class Tiempo(BaseModel):
    id_tiempo: Optional[int]  # El cliente puede enviar el ID (opcional)
    fecha: date
    anio: int
    mes: int
    dia: int
    trimestre: int

    class Config:
        orm_mode = True


# -------------------- Esquema para la tabla pract_03_Data_hechos_ventas --------------------
class HechosVentas(BaseModel):
    id_venta: Optional[int]  # El cliente puede enviar el ID (opcional)
    id_tiempo: int
    id_cliente: int
    id_producto: int
    id_sucursal: int
    id_empleado: int
    id_pago: int
    id_promocion: int
    cantidad: int
    subtotal: float
    total: float

    class Config:
        orm_mode = True


# -------------------- Esquema para la tabla pract_03_Data_categoria --------------------
class Categoria(BaseModel):
    id_categoria: Optional[int]  # El cliente puede enviar el ID (opcional)
    nombre: str
    descripcion_categoria: Optional[str] = None  # Descripción opcional

    class Config:
        orm_mode = True


# -------------------- Esquema para la tabla pract_03_Data_empleados --------------------
class Empleado(BaseModel):
    id_empleado: Optional[int]  # El cliente puede enviar el ID (opcional)
    nombre: str
    apellido: str
    puesto: str
    salario: float
    id_sucursal: int
    fecha_contratacion: date

    class Config:
        orm_mode = True

