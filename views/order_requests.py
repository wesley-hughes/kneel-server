from .metal_requests import get_single_metal
from .size_requests import get_single_size
from .style_requests import get_single_style
from .type_requests import get_single_type
ORDERS = [
    {
        "id": 1,
        "metalId": 1,
        "sizeId": 1,
        "styleId": 1,
        "typeId": 1,
        "timestamp": 1614659931693
    }
]

def get_all_orders():
    '''gets all orders'''
    return ORDERS
def get_single_order(id):
    '''gets single order by id'''
    requested_order = None
    for order in ORDERS:
        if order["id"] == id:
            requested_order = order
            matching_metal = get_single_metal(requested_order["metalId"])
            requested_order["metal"] = matching_metal
            matching_size = get_single_size(requested_order["sizeId"])
            requested_order["size"] = matching_size
            matching_style = get_single_style(requested_order["styleId"])
            requested_order["style"] = matching_style
            matching_type = get_single_type(requested_order["typeId"])
            requested_order["type"] = matching_type
            requested_order.pop("metalId")
            requested_order.pop("sizeId")
            requested_order.pop("styleId")
            requested_order.pop("typeId")
        return requested_order
def create_order(order):
    '''creates new order'''
    max_id = ORDERS[-1]["id"]
    new_id = max_id + 1
    order["id"] = new_id
    ORDERS.append(order)
    return order
def delete_order(id):
    '''docstring'''
    order_index = -1
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            order_index = index
    if order_index >= 0:
        ORDERS.pop(order_index)
def update_order(id, new_order):
    '''docstring'''
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            ORDERS[index] = new_order
            break