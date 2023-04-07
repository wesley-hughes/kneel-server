METALS = [
    { "id": 1, "metal": "Sterling Silver", "price": 12.42 },
    { "id": 2, "metal": "14K Gold", "price": 736.4 },
    { "id": 3, "metal": "24K Gold", "price": 1258.9 },
    { "id": 4, "metal": "Platinum", "price": 795.45 },
    { "id": 5, "metal": "Palladium", "price": 1241.0 }
]

def get_all_metals():
    '''this gets all metals'''
    return METALS
def get_single_metal(id):
    '''this gets single metal by id'''
    requested_metal = None
    for metal in METALS:
        if metal["id"] == id:
            requested_metal = metal

        return requested_metal