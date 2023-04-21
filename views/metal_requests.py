import sqlite3
import json
from models import Order, Metal, Size, Style
METALS = [
    { "id": 1, "metal": "Sterling Silver", "price": 12.42 },
    { "id": 2, "metal": "14K Gold", "price": 736.4 },
    { "id": 3, "metal": "24K Gold", "price": 1258.9 },
    { "id": 4, "metal": "Platinum", "price": 795.45 },
    { "id": 5, "metal": "Palladium", "price": 1241.0 }
]

def get_all_metals(query_params):
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
            m.id,
            m.metal,
            m.price
        FROM Metals m
        {sort_by}
        """
        db_cursor.execute(sql_to_execute)
        metals = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            metal = Metal(row['id'], row['metal'], row['price'])
            metals.append(metal.__dict__)
    return metals

def get_single_metal(id):
    requested_metal = None

    for metal in METALS:
        if metal["id"] == id:
            requested_metal = metal
            return requested_metal
        
def create_metal(metal):
    max_id = METALS[-1]["id"]
    new_id = max_id + 1
    metal["id"] = new_id
    METALS.append(metal)
    return metal

def update_metal(id, new_metal):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Metals
            SET
                price = ?
        WHERE id = ?
        """, (new_metal['price'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True

def delete_metal(id):
    metal_index = -1
    
    for index, metal in enumerate(METALS):
        if metal["id"] == id:
            metal_index = index
            
    if metal_index >= 0:
        METALS.pop(metal_index)