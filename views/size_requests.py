import sqlite3
import json
from models import Order, Metal, Size, Style
SIZES = [
    { "id": 1, "carats": 0.5, "price": 405 },
    { "id": 2, "carats": 0.75, "price": 782 },
    { "id": 3, "carats": 1, "price": 1470 },
    { "id": 4, "carats": 1.5, "price": 1997 },
    { "id": 5, "carats": 2, "price": 3638 }
]

def get_all_sizes(query_params):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        sort_by = ""
        
        if len(query_params) != 0:
            param = query_params[0]
            [qs_key, qs_value] = param.split("=")

            if qs_key == "_sortBy":
                if qs_value == 'price':
                    sort_by = "ORDER BY price"
        sql_to_execute = f"""
        SELECT
            sz.id,
            sz.carats,
            sz.price
        FROM Sizes sz
        {sort_by}
        """
        db_cursor.execute(sql_to_execute)
        sizes = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            size = Size(row['id'], row['carats'], row['price'])
            sizes.append(size.__dict__)
    return sizes

def get_single_size(id):
    requested_size = None
    
    for size in SIZES:
        if size["id"] == id:
            requested_size = size
            return requested_size
        
def create_size(size):
    max_id = SIZES[-1]["id"]
    new_id = max_id + 1
    size["id"] = new_id
    SIZES.append(size)
    return size

def update_size(id, new_size):
    for index, size in enumerate(SIZES):
        if size["id"] == id:
            SIZES[index] = new_size
            break

def delete_size(id):
    size_index = -1
    
    for index, size in enumerate(SIZES):
        if size["id"] == id:
            size_index = index
            
    if size_index >= 0:
        SIZES.pop(size_index)