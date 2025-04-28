from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from database import Base

# Tabla: pract_03_Data_categoria
class Categoria(Base):
    __tablename__ = "pract_03_Data_categoria"
    id_categoria = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    descripcion_categoria = Column(String(100))
    productos = relationship("Producto", back_populates="categoria")

# Tabla: pract_03_Data_clientes
class Cliente(Base):
    __tablename__ = "pract_03_Data_clientes"
    id_cliente = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    apellido = Column(String(50))
    email = Column(String(50))
    telefono = Column(String(50))
    direccion = Column(String(50))
    fecha_registro = Column(Date)
    ventas = relationship("Venta", back_populates="cliente")

# Tabla: pract_03_Data_empleados
class Empleado(Base):
    __tablename__ = "pract_03_Data_empleados"
    id_empleado = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    apellido = Column(String(50))
    puesto = Column(String(50))
    salario = Column(DECIMAL(10, 1))
    id_sucursal = Column(Integer, ForeignKey('pract_03_Data_sucursales.id_sucursal'))
    fecha_contratacion = Column(Date)
    sucursal = relationship("Sucursal", back_populates="empleados")
    ventas = relationship("Venta", back_populates="empleado")

# Tabla: pract_03_Data_pago
class Pago(Base):
    __tablename__ = "pract_03_Data_pago"
    id_pago = Column(Integer, primary_key=True, index=True)
    metodo = Column(String(50))
    monto = Column(DECIMAL(10, 1))
    fecha_pago = Column(Date)
    ventas = relationship("Venta", back_populates="pago")

# Tabla: pract_03_Data_productos
class Producto(Base):
    __tablename__ = "pract_03_Data_productos"
    id_producto = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    id_categoria = Column(Integer, ForeignKey('pract_03_Data_categoria.id_categoria'))
    marca = Column(String(50))
    precio = Column(DECIMAL(10, 1))
    stock = Column(Integer)
    id_proveedor = Column(Integer, ForeignKey('pract_03_Data_proveedores.id_proveedor'))
    fechaingreso = Column(Date)
    tamano = Column(String(50))
    SKU = Column(String(50))
    categoria = relationship("Categoria", back_populates="productos")
    proveedor = relationship("Proveedor", back_populates="productos")
    ventas = relationship("Venta", back_populates="producto")

# Tabla: pract_03_Data_promociones
class Promocion(Base):
    __tablename__ = "pract_03_Data_promociones"
    id_promocion = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String)
    descuento = Column(Float)
    ventas = relationship("Venta", back_populates="promocion")

# Tabla: pract_03_Data_proveedores
class Proveedor(Base):
    __tablename__ = "pract_03_Data_proveedores"
    id_proveedor = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    contacto = Column(String(50))
    telefono = Column(String(50))
    email = Column(String(50))
    productos = relationship("Producto", back_populates="proveedor")

# Tabla: pract_03_Data_sucursales
class Sucursal(Base):
    __tablename__ = "pract_03_Data_sucursales"
    id_sucursal = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50))
    direccion = Column(String(100))
    ciudad = Column(String(50))
    telefono = Column(String(50))
    empleados = relationship("Empleado", back_populates="sucursal")
    ventas = relationship("Venta", back_populates="sucursal")

# Tabla: pract_03_Data_tiempo
class Tiempo(Base):
    __tablename__ = "pract_03_Data_tiempo"
    id_tiempo = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date)
    anio = Column(Integer)
    mes = Column(Integer)
    dia = Column(Integer)
    trimestre = Column(Integer)
    ventas = relationship("Venta", back_populates="tiempo")

# Tabla: pract_03_Data_Hechos_ventas
class Venta(Base):
    __tablename__ = "pract_03_Hechos_ventas"
    id_venta = Column(Integer, primary_key=True, index=True)
    id_tiempo = Column(Integer, ForeignKey('pract_03_Data_tiempo.id_tiempo'))
    id_cliente = Column(Integer, ForeignKey('pract_03_Data_clientes.id_cliente'))
    id_producto = Column(Integer, ForeignKey('pract_03_Data_productos.id_producto'))
    id_sucursal = Column(Integer, ForeignKey('pract_03_Data_sucursales.id_sucursal'))
    id_empleado = Column(Integer, ForeignKey('pract_03_Data_empleados.id_empleado'))
    id_pago = Column(Integer, ForeignKey('pract_03_Data_pago.id_pago'))
    id_promocion = Column(Integer, ForeignKey('pract_03_Data_promociones.id_promocion'))
    cantidad = Column(Integer)
    subtotal = Column(DECIMAL(10, 1))
    total = Column(DECIMAL(10, 1))

    tiempo = relationship("Tiempo", back_populates="ventas")
    cliente = relationship("Cliente", back_populates="ventas")
    producto = relationship("Producto", back_populates="ventas")
    sucursal = relationship("Sucursal", back_populates="ventas")
    empleado = relationship("Empleado", back_populates="ventas")
    pago = relationship("Pago", back_populates="ventas")
    promocion = relationship("Promocion", back_populates="ventas")
