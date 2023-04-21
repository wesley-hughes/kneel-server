import sqlite3
import json
from models import Order, Metal, Size, Style
STYLES = [
    { "id": 1, "style": "Classic", "price": 500 },
    { "id": 2, "style": "Modern", "price": 710 },
    { "id": 3, "style": "Vintage", "price": 965 }
]

def get_all_styles(query_params):
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
            st.id,
            st.style,
            st.price
        FROM Styles st
        {sort_by}
        """
        db_cursor.execute(sql_to_execute)
        styles = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            style = Style(row['id'], row['style'], row['price'])
            styles.append(style.__dict__)
    return styles

def get_single_style(id):
    requested_style = None
    
    for style in STYLES:
        if style["id"] == id:
            requested_style = style
            return requested_style
        
def create_style(style):
    max_id = STYLES[-1]["id"]
    new_id = max_id + 1
    style["id"] = new_id
    STYLES.append(style)
    return style

def update_style(id, new_style):
    for index, style in enumerate(STYLES):
        if style["id"] == id:
            STYLES[index] = new_style
            break

def delete_style(id):
    style_index = -1
    
    for index, style in enumerate(STYLES):
        if style["id"] == id:
                style_index = index
                
    if style_index >= 0:
        STYLES.pop(style_index)