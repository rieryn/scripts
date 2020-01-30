
from selenium import webdriver
import pandas as pd
import sys
import os
import csv
import sqlite3


urls = ["https://www.ssense.com/en-ca/women/designers/loewe"]

class Product(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
def editProductTable(products):
    try:
        sqliteConnection = sqlite3.connect('SQLite.db')
        print("Successfully Connected to SQLite")
        cursor = sqliteConnection.cursor()
        sqlite_select_Query = "select sqlite_version();"
        cursor.execute(sqlite_select_Query)
        record = cursor.fetchall()
        print("SQLite Database Version is: ", record)
        sqlite_create_table_query = '''CREATE TABLE IF NOT EXISTS products_table (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    price REAL NOT NULL);'''
        cursor.execute(sqlite_create_table_query)
        print("products_table found successfuly")

        index = 0
        for product in products:
            index+=1
            print(index,product.name, product.price)
            NAME = product.name
            PRICE = product.price
            cursor.execute("""INSERT INTO products_table
                              (name,price) 
                               VALUES (?, ?)""",
                              [NAME,PRICE])
            print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
        cursor.execute("SELECT * FROM products_table")
        print(cursor.fetchall())
        cursor.close()

    except sqlite3.Error as error:
        print(error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("The SQLite connection is closed")

def getSearchProducts():
    chrome_path = os.path.join(sys.path[0], 'chromedriver.exe')
    driver = webdriver.Chrome(chrome_path)
    for url in urls:
        driver.get(url)
        items = driver.find_elements_by_class_name("browsing-product-item")
        products = []
        for item in items:
            try:
                name = item.find_element_by_class_name("product-name-plp").text
                price = item.find_element_by_class_name("price").text
                products.append(Product(name, price))
            except WebDriverException:
                pass
    return products

#def getDirectLinkProduct():
#def getURLs


editProductTable(getSearchProducts())

