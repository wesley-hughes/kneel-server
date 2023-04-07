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