#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'cesar'

import sys
import sqlite3


def getCategory(categoryId):
    conn = sqlite3.connect('categories_ht.db')
    c = conn.cursor()
    category = None
    c.execute("SELECT * FROM categories WHERE id = " +  categoryId)
    category = c.fetchone()
    conn.commit()
    conn.close()

    return category

def getCategorySons(categoryId):
    conn = sqlite3.connect('categories_ht.db')
    c = conn.cursor()
    categories = None
    c.execute("SELECT * FROM categories WHERE categoryParentID = " +  str(categoryId))
    categories = c.fetchall()
    conn.commit()
    conn.close()

    return categories

def render_category_list(f, category):
    list_header = "<ul>"
    f.write(list_header)

    name = category[1]
    list_item = "<li>" + name.encode('utf-8') + "</li>"
    f.write(list_item)

    categoryId = category[0]
    sons = getCategorySons(categoryId)
    if len(sons)>0:
        for son in sons:
            render_category_list(f,son)

    list_footer = "</ul>"
    f.write(list_footer)



def start():
    categoryId = sys.argv[1]
    category = getCategory(categoryId)
    if category is None:
        print('No category with ID:' + categoryId())
    else:
        html_file_name = categoryId + '.html'
        f = open( html_file_name,'w')

        header = """<!DOCTYPE html>
        <head>
        <meta charset="utf-8">
        <link href="http://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" type="text/css">
        <link rel="stylesheet" type="text/css" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
        </head>
        <body>
        <h2>Ebay Categories List</h2>"""
        f.write(header)


        render_category_list(f, category)

        footer = """</body>
        </html>"""
        f.write(footer)
        f.close()
        print(html_file_name)
try:
    start()
except Exception as e:
    # print e
    print('Error no se pudo realizar la operacion')