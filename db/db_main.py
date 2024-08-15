import sqlite3
from db import queries

db = sqlite3.connect('db/db.sqlite3')
cursor = db.cursor()


async def sql_create():
    if db:
        print("База данных SQLite3 подключена!")
    cursor.execute(queries.CREATE_TABLE_REGISTRATION)
    cursor.execute(queries.CREATE_TABLE_PRODUCTS)
    cursor.execute(queries.CREATE_TABLE_PRODUCT_DETAILS)
    db.commit()


async def sql_insert_registration(telegram_id, firstname):
    cursor.execute(queries.INSERT_INTO_TABLE_REGISTRATION, (
        telegram_id, firstname
    ))
    db.commit()

async def sql_insert_products(name, size, price, id_product, photo):
    cursor.execute(queries.INSERT_PRODUCTS, (
        name,
        size,
        price,
        id_product,
        photo
    ))
    db.commit()

async def sql_insert_product_details(infoproduct,id_product,category):
    cursor.execute(queries.INSERT_PRODUCT_DETAILS, (
        infoproduct,
        id_product,
        category
    ))
    db.commit()

def sql_get_info(id):
    cursor.execute(queries.OUTPUT_PRODUCT,(id,))
    result = cursor.fetchone()
    if result:
        return(result)
    db.commit()
