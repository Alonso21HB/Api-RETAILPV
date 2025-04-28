from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud, schemas, models  # Importar el CRUD y los esquemas de datos
from database import get_db, get_db_mysql  # Funciones para obtener las sesiones de las bases de datos
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

app = FastAPI()

# --- Rutas para obtener datos de SQL Server ---

# Ruta para obtener clientes
@app.get("/clientes/", response_model=List[schemas.Cliente])
def get_clientes(db: Session = Depends(get_db)):
    try:
        clientes = crud.get_clientes(db=db)
        return JSONResponse(content=jsonable_encoder(clientes), media_type="application/json; charset=utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener clientes: {str(e)}")

# Ruta para obtener productos
@app.get("/productos/", response_model=List[schemas.Producto])
def get_productos(db: Session = Depends(get_db)):
    try:
        productos = crud.get_productos(db=db)
        return JSONResponse(content=jsonable_encoder(productos), media_type="application/json; charset=utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener productos: {str(e)}")

# Ruta para obtener sucursales
@app.get("/sucursales/", response_model=List[schemas.Sucursal])
def get_sucursales(db: Session = Depends(get_db)):
    try:
        sucursales = crud.get_sucursales(db=db)
        return JSONResponse(content=jsonable_encoder(sucursales), media_type="application/json; charset=utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener sucursales: {str(e)}")

# Ruta para obtener pagos
@app.get("/pagos/", response_model=List[schemas.Pago])
def get_pagos(db: Session = Depends(get_db)):
    try:
        pagos = crud.get_pagos(db=db)
        return JSONResponse(content=jsonable_encoder(pagos), media_type="application/json; charset=utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener pagos: {str(e)}")

# Ruta para obtener promociones
@app.get("/promociones/", response_model=List[schemas.Promocion])
def get_promociones(db: Session = Depends(get_db)):
    try:
        promociones = crud.get_promociones(db=db)
        return JSONResponse(content=jsonable_encoder(promociones), media_type="application/json; charset=utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener promociones: {str(e)}")

# Ruta para obtener proveedores
@app.get("/proveedores/", response_model=List[schemas.Proveedor])
def get_proveedores(db: Session = Depends(get_db)):
    try:
        proveedores = crud.get_proveedores(db=db)
        return JSONResponse(content=jsonable_encoder(proveedores), media_type="application/json; charset=utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener proveedores: {str(e)}")

# Ruta para obtener tiempos
@app.get("/tiempos/", response_model=List[schemas.Tiempo])
def get_tiempos(db: Session = Depends(get_db)):
    try:
        tiempos = crud.get_tiempos(db=db)
        return JSONResponse(content=jsonable_encoder(tiempos), media_type="application/json; charset=utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener tiempos: {str(e)}")

# Ruta para obtener hechos de ventas
@app.get("/hechos_ventas/", response_model=List[schemas.HechosVentas])
def get_hechos_ventas(db: Session = Depends(get_db)):
    try:
        hechos_ventas = crud.get_hechos_ventas(db=db)
        return JSONResponse(content=jsonable_encoder(hechos_ventas), media_type="application/json; charset=utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener hechos de ventas: {str(e)}")

# Ruta para obtener categorías
@app.get("/categorias/", response_model=List[schemas.Categoria])
def get_categorias(db: Session = Depends(get_db)):
    try:
        categorias = crud.get_categorias(db=db)
        return JSONResponse(content=jsonable_encoder(categorias), media_type="application/json; charset=utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener categorías: {str(e)}")

# Ruta para obtener empleados
@app.get("/empleados/", response_model=List[schemas.Empleado])
def get_empleados(db: Session = Depends(get_db)):
    try:
        empleados = crud.get_empleados(db=db)
        return JSONResponse(content=jsonable_encoder(empleados), media_type="application/json; charset=utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener empleados: {str(e)}")


# --- Ruta para sincronizar datos de SQL Server a MySQL ---

@app.post("/sincronizar")
def sincronizar_datos(
    db_local: Session = Depends(get_db),
    db_remoto: Session = Depends(get_db_mysql)
):
    try:
        # Lógica para sincronizar los datos
        tablas = [
            {"modelo": models.Cliente, "nombre": "Cliente"},
            {"modelo": models.Producto, "nombre": "Producto"},
            {"modelo": models.Sucursal, "nombre": "Sucursal"},
            {"modelo": models.Pago, "nombre": "Pago"},
            {"modelo": models.Promocion, "nombre": "Promocion"},
            {"modelo": models.Proveedor, "nombre": "Proveedor"},
            {"modelo": models.Tiempo, "nombre": "Tiempo"},
            {"modelo": models.Venta, "nombre": "HechosVentas"},
            {"modelo": models.Categoria, "nombre": "Categoria"},
            {"modelo": models.Empleado, "nombre": "Empleado"}
        ]

        resultados = {}

        for tabla in tablas:
            modelo = tabla["modelo"]
            nombre_tabla = tabla["nombre"]

            # Obtener los datos desde SQL Server
            datos_locales = db_local.query(modelo).all()

            # Obtener las IDs de los registros existentes en MySQL
            pk_column = list(modelo.__table__.primary_key.columns)[0]
            ids_remotos = {getattr(e, pk_column.name) for e in db_remoto.query(pk_column).all()}

            # Filtrar los nuevos registros que no existen en MySQL
            nuevos = [
                modelo(**{column.name: getattr(fila, column.name) for column in modelo.__table__.columns})
                for fila in datos_locales
                if getattr(fila, pk_column.name) not in ids_remotos
            ]

            # Si hay registros nuevos, los insertamos en MySQL
            if nuevos:
                db_remoto.add_all(nuevos)
                db_remoto.commit()

            resultados[nombre_tabla] = f"{len(nuevos)} nuevos registros sincronizados."

        return JSONResponse(content=jsonable_encoder(resultados), media_type="application/json; charset=utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al sincronizar datos: {str(e)}")
