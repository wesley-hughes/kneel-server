import sqlite3
import json
from models import Order, Metal, Size, Style
ORDERS = [
    {
        "id": 1,
        "metal_id": 1,
        "size_id": 2,
        "style_id": 3,
        "timestamp": 1614659931693
    },
    {
        "id": 2,
        "metal_id": 2,
        "size_id": 3,
        "style_id": 1,
        "timestamp": 1616333988188
    },
    {
        "id": 3,
        "metal_id": 3,
        "size_id": 1,
        "style_id": 2,
        "timestamp": 1616334884289
    },
    {
        "id": 4,
        "metal_id": 1,
        "size_id": 3,
        "style_id": 2,
        "timestamp": 1616334980694
    }
]

def get_all_orders():
    '''retrieve all orders from database'''
    with sqlite3.connect("./kneel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id,
            o.timestamp
        FROM Order o
        """)
        orders = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            order = Order(row['id'], row['metal_id'], row['size_id'], row['style_id'], row['timestamp'])
            orders.append(order.__dict__)
        return orders
    
def get_single_order(id):
    requested_order = None
    
    for order in ORDERS:
        if order["id"] == id:
            requested_order = order
            return requested_order
        
def create_order(order):
    if len(ORDERS) == 0:
        max_id = 0
    else:
        max_id = ORDERS[-1]["id"]
    new_id = max_id + 1
    order["id"] = new_id
    ORDERS.append(order)
    return order

def update_order(id, new_order):
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            ORDERS[index] = new_order
            break

def delete_order(id):
    order_index = -1
    
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            order_index = index
            
    if order_index >= 0:
        ORDERS.pop(order_index)