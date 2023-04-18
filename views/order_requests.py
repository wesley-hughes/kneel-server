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
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            o.id,
            o.size_id,
            o.style_id,
            o.metal_id,
            o.timestamp,
            m.id,
            m.metal,
            m.price,
            sz.id,
            sz.carats,
            sz.price,
            st.style,
            st.price
        FROM Orders o
        JOIN Metals m ON m.id = o.metal_id
        JOIN Sizes sz ON sz.id = o.size_id
        JOIN Styles st ON st.id = o.style_id
        """)
        orders = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            order = Order(row['id'], row['metal_id'], row['size_id'], row['style_id'], row['timestamp'])
            metal = Metal(row['metal_id'], row['metal'], row['price'])
            size = Size(row['size_id'], row['carats'], row['price'])
            style = Style(row['style_id'], row['style'], row['price'])
            order.metal = metal.__dict__
            order.size = size.__dict__
            order.style = style.__dict__
            orders.append(order.__dict__)
        return orders
    
def get_single_order(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id,
            o.timestamp
        FROM Orders o
        WHERE o.id = ?
        """, (id, ))
        data = db_cursor.fetchone()
        order = Order(data['id'], data['metal_id'], data['size_id'], data['style_id'], data['timestamp'])
        return order.__dict__
        
def create_order(new_order):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Orders
            ( metal_id, size_id, style_id, timestamp )
        VALUES
            ( ?, ?, ?, ?);
        """, (new_order['metal_id'], new_order['size_id'], new_order['style_id'], new_order['timestamp']))

        id = db_cursor.lastrowid

        new_order['id'] = id

def update_order(id, new_order):
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            ORDERS[index] = new_order
            break

def delete_order(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Orders
        WHERE id = ?
        """, (id, ))