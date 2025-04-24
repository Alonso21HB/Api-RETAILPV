from pydantic import BaseModel
from typing import Optional
import uuid
from datetime import date

# -------------------- Esquema para la tabla pract_03_Data_clientes --------------------
class ClienteCreate(BaseModel):
    id_cliente: Optional[int]  # El cliente puede enviar el ID (opcional)
    nombre: str
    apellido: str
    email: str
    telefono: str
    direccion: str
    fecha_registro: Optional[str] = None  # Fecha opcional

    class Config:
        orm_mode = True

class Cliente(ClienteCreate):
    id_cliente: int  # Este campo solo se incluirá en la respuesta

    class Config:
        orm_mode = True


# -------------------- Esquema para la tabla pract_03_Data_productos --------------------
class ProductoCreate(BaseModel):
    id_producto: Optional[int]  # El cliente puede enviar el ID (opcional)
    nombre: str
    id_categoria: int
    marca: str
    precio: float
    stock: int
    id_proveedor: int
    tamano: str
    SKU: str

    class Config:
        orm_mode = True

class Producto(ProductoCreate):
    id_producto: int  # Este campo solo se incluirá en la respuesta

    class Config:
        orm_mode = True


# -------------------- Esquema para la tabla pract_03_Data_sucursales --------------------
class SucursalCreate(BaseModel):
    id_sucursal: Optional[int]  # El cliente puede enviar el ID (opcional)
    nombre: str
    direccion: str
    ciudad: str
    telefono: str

    class Config:
        orm_mode = True

class Sucursal(SucursalCreate):
    id_sucursal: int  # Este campo solo se incluirá en la respuesta

    class Config:
        orm_mode = True


# -------------------- Esquema para la tabla pract_03_Data_pago --------------------
class PagoCreate(BaseModel):
    id_pago: Optional[int]  # El cliente puede enviar el ID (opcional)
    metodo: str
    monto: float
    fecha_pago: str

    class Config:
        orm_mode = True

class Pago(PagoCreate):
    id_pago: int  # Este campo solo se incluirá en la respuesta

    class Config:
        orm_mode = True


# -------------------- Esquema para la tabla pract_03_Data_promociones --------------------
class PromocionCreate(BaseModel):
    id_promocion: Optional[int]  # El cliente puede enviar el ID (opcional)
    descripcion: str
    descuento: float

    class Config:
        orm_mode = True

class Promocion(PromocionCreate):
    id_promocion: int  # Este campo solo se incluirá en la respuesta

    class Config:
        orm_mode = True


# -------------------- Esquema para la tabla pract_03_Data_proveedores --------------------
class ProveedorCreate(BaseModel):
    id_proveedor: Optional[int]  # El cliente puede enviar el ID (opcional)
    nombre: str
    contacto: str
    telefono: str
    email: str

    class Config:
        orm_mode = True

class Proveedor(ProveedorCreate):
    id_proveedor: int  # Este campo solo se incluirá en la respuesta

    class Config:
        orm_mode = True


# -------------------- Esquema para la tabla pract_03_Data_tiempo --------------------
class TiempoCreate(BaseModel):
    id_tiempo: Optional[int]  # El cliente puede enviar el ID (opcional)
    fecha: str
    anio: int
    mes: int
    dia: int
    trimestre: int

    class Config:
        orm_mode = True

class Tiempo(TiempoCreate):
    id_tiempo: int  # Este campo solo se incluirá en la respuesta

    class Config:
        orm_mode = True


# -------------------- Esquema para la tabla pract_03_Data_hechos_ventas --------------------
class HechosVentasCreate(BaseModel):
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

class HechosVentas(HechosVentasCreate):
    id_venta: int  # Este campo solo se incluirá en la respuesta

    class Config:
        orm_mode = True


# -------------------- Esquema para la tabla pract_03_Data_categoria --------------------
class CategoriaCreate(BaseModel):
    id_categoria: Optional[int]  # El cliente puede enviar el ID (opcional)
    nombre: str
    descripcion_categoria: Optional[str] = None  # Descripción opcional

    class Config:
        orm_mode = True

class Categoria(CategoriaCreate):
    id_categoria: int  # Este campo solo se incluirá en la respuesta

    class Config:
        orm_mode = True


# -------------------- Esquema para la tabla pract_03_Data_empleados --------------------
class EmpleadoCreate(BaseModel):
    id_empleado: Optional[int]  # El cliente puede enviar el ID (opcional)
    nombre: str
    apellido: str
    puesto: str
    salario: float
    id_sucursal: int
    fecha_contratacion: str

    class Config:
        orm_mode = True

class Empleado(EmpleadoCreate):
    id_empleado: int  # Este campo solo se incluirá en la respuesta

    class Config:
        orm_mode = True

# -------------------- Función para generar un ID (si es necesario) --------------------
def generate_cliente_id():
    return uuid.uuid4()  # Si se desea generar un UUID para el ID
