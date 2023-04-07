TYPES = [
    { "id": 1, "type": "Ring", "price_multiplier": 1},
    { "id": 2, "type": "Earrings", "price_multiplier": 2},
    { "id": 3, "type": "Necklace", "price_multiplier": 4}
]
def get_all_types():
    '''gets all types'''
    return TYPES
def get_single_type(id):
    '''gets single type by id'''
    requested_type = None
    for type in TYPES:
        if type["id"] == id:
            requested_type = type
        return requested_type