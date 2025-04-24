from sqlalchemy.orm import Session
from models import (
    Cliente, Producto, Sucursal, Pago, Promocion, Proveedor, 
    Tiempo, Venta, Categoria, Empleado
)

# -------------------- CRUD para Clientes --------------------
def create_cliente(db: Session, cliente: Cliente):
    db_cliente = Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def get_clientes(db: Session):
    return db.query(Cliente).order_by(Cliente.id_cliente).all()

# -------------------- CRUD para Productos --------------------
def create_producto(db: Session, producto: Producto):
    db_producto = Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def get_productos(db: Session):
    return db.query(Producto).order_by(Producto.id_producto).all()

# -------------------- CRUD para Sucursales --------------------
def create_sucursal(db: Session, sucursal: Sucursal):
    db_sucursal = Sucursal(**sucursal.dict())
    db.add(db_sucursal)
    db.commit()
    db.refresh(db_sucursal)
    return db_sucursal

def get_sucursales(db: Session):
    return db.query(Sucursal).order_by(Sucursal.id_sucursal).all()

# -------------------- CRUD para Pagos --------------------
def create_pago(db: Session, pago: Pago):
    db_pago = Pago(**pago.dict())
    db.add(db_pago)
    db.commit()
    db.refresh(db_pago)
    return db_pago

def get_pagos(db: Session):
    return db.query(Pago).order_by(Pago.id_pago).all()

# -------------------- CRUD para Promociones --------------------
def create_promocion(db: Session, promocion: Promocion):
    db_promocion = Promocion(**promocion.dict())
    db.add(db_promocion)
    db.commit()
    db.refresh(db_promocion)
    return db_promocion

def get_promociones(db: Session):
    return db.query(Promocion).order_by(Promocion.id_promocion).all()

# -------------------- CRUD para Proveedores --------------------
def create_proveedor(db: Session, proveedor: Proveedor):
    db_proveedor = Proveedor(**proveedor.dict())
    db.add(db_proveedor)
    db.commit()
    db.refresh(db_proveedor)
    return db_proveedor

def get_proveedores(db: Session):
    return db.query(Proveedor).order_by(Proveedor.id_proveedor).all()

# -------------------- CRUD para Tiempo --------------------
def create_tiempo(db: Session, tiempo: Tiempo):
    db_tiempo = Tiempo(**tiempo.dict())
    db.add(db_tiempo)
    db.commit()
    db.refresh(db_tiempo)
    return db_tiempo

def get_tiempos(db: Session):
    return db.query(Tiempo).order_by(Tiempo.id_tiempo).all()

# -------------------- CRUD para Hechos de Ventas --------------------
def create_hechos_ventas(db: Session, hechos: Venta):
    db_hechos_ventas = Venta(**hechos.dict())
    db.add(db_hechos_ventas)
    db.commit()
    db.refresh(db_hechos_ventas)
    return db_hechos_ventas

def get_hechos_ventas(db: Session):
    return db.query(Venta).order_by(Venta.id_venta).all()

# -------------------- CRUD para Categoría --------------------
def create_categoria(db: Session, categoria: Categoria):
    db_categoria = Categoria(**categoria.dict())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def get_categorias(db: Session):
    return db.query(Categoria).order_by(Categoria.id_categoria).all()

# -------------------- CRUD para Empleados --------------------
def create_empleado(db: Session, empleado: Empleado):
    db_empleado = Empleado(**empleado.dict())
    db.add(db_empleado)
    db.commit()
    db.refresh(db_empleado)
    return db_empleado

def get_empleados(db: Session):
    return db.query(Empleado).order_by(Empleado.id_empleado).all()
