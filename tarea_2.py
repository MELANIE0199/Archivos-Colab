# -*- coding: utf-8 -*-
"""Tarea_2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KIvOLiXydWUhMQDTPKVLiwtH5KTlV1Jz
"""

import pandas as pd
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

data = {
    'Columna1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
    'Columna2': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']}

df = pd.DataFrame(data)


df.to_csv('dataset.csv', index=False)


df.to_parquet('dataset.parquet')


engine = create_engine('sqlite:///dataset.db')
df.to_sql('table_name', engine, if_exists='replace', index=False)


csv_data = pd.read_csv('dataset.csv')
print("Head (11) - CSV Dataset:\n", csv_data.head(11))
print("Tail (20) - CSV Dataset:\n", csv_data.tail(20))

parquet_data = pd.read_parquet('dataset.parquet')
print("Head (11) - Parquet Dataset:\n", parquet_data.head(11))
print("Tail (20) - Parquet Dataset:\n", parquet_data.tail(20))

sql_data = pd.read_sql('SELECT * FROM table_name', engine)
print("Head (11) - SQL Dataset:\n", sql_data.head(11))
print("Tail (20) - SQL Dataset:\n", sql_data.tail(20))

csv_data.to_csv('output.txt', index=False, sep='\t')

parquet_data.to_excel('output.xlsx', index=False)

sql_data.to_json('output.json', orient='records')


Base = declarative_base()

class Producto(Base):
    __tablename__ = 'productos'
    id_producto = Column(Integer, primary_key=True)
    descripcion = Column(String)
    precio_costo = Column(Float)
    Precio_venta = Column(Float)
    disponibilidad_actual = Column(Integer)

class Facturacion(Base):
    __tablename__ = 'facturacion'
    no_factura = Column(Integer, primary_key=True)
    id_producto = Column(Integer)
    descripcion = Column(String)
    fecha_venta = Column(Date)
    Precio_venta = Column(Float)
    Compra = Column(Integer)
    Subtotal = Column(Float)
    IVA = Column(Float)
    Total = Column(Float)

engine = create_engine('sqlite:///punto_ventas.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

producto1 = Producto(id_producto=1, descripcion='Producto 1', precio_costo=10.0, Precio_venta=15.0, disponibilidad_actual=100)
producto2 = Producto(id_producto=2, descripcion='Producto 2', precio_costo=20.0, Precio_venta=30.0, disponibilidad_actual=50)


fecha_venta = datetime.strptime('2024-10-20', '%Y-%m-%d').date()


factura1 = Facturacion(no_factura=1, id_producto=1, descripcion='Producto 1', fecha_venta=fecha_venta, Precio_venta=15.0, Compra=2, Subtotal=30.0, IVA=4.5, Total=34.5)
factura2 = Facturacion(no_factura=2, id_producto=2, descripcion='Producto 2', fecha_venta=fecha_venta, Precio_venta=30.0, Compra=1, Subtotal=30.0, IVA=4.5, Total=34.5)


session.add_all([producto1, producto2, factura1, factura2])
session.commit()

print("Base de datos 'punto_ventas' creada y registros insertados.")