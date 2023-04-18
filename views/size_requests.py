SIZES = [
    { "id": 1, "carats": 0.5, "price": 405 },
    { "id": 2, "carats": 0.75, "price": 782 },
    { "id": 3, "carats": 1, "price": 1470 },
    { "id": 4, "carats": 1.5, "price": 1997 },
    { "id": 5, "carats": 2, "price": 3638 }
]

def get_all_sizes():
    return SIZES

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