DATABASE = {
    "METALS": [
        {"id": 1, "metal": "Sterling Silver", "price": 12.42},
        {"id": 2, "metal": "14K Gold", "price": 736.4},
        {"id": 3, "metal": "24K Gold", "price": 1258.9},
        {"id": 4, "metal": "Platinum", "price": 795.45},
        {"id": 5, "metal": "Palladium", "price": 1241.0}
    ],
    "ORDERS": [
        {
            "id": 1,
            "metalId": 1,
            "sizeId": 1,
            "styleId": 1,
            "typeId": 1,
            "timestamp": 1614659931693
        },
        {
            "id": 2,
            "metalId": 2,
            "sizeId": 2,
            "styleId": 2,
            "typeId": 2,
            "timestamp": 1614659931693
        },
        {
            "id": 3,
            "metalId": 3,
            "sizeId": 3,
            "styleId": 3,
            "typeId": 3,
            "timestamp": 1614659931693
        }
    ],
    "SIZES": [
        {"id": 1, "carets": 0.5, "price": 405},
        {"id": 2, "carets": 0.75, "price": 782},
        {"id": 3, "carets": 1, "price": 1470},
        {"id": 4, "carets": 1.5, "price": 1997},
        {"id": 5, "carets": 2, "price": 3638}
    ],
    "STYLES": [
        {"id": 1, "style": "Classic", "price": 500},
        {"id": 2, "style": "Modern", "price": 710},
        {"id": 3, "style": "Vintage", "price": 965}
    ],
    "TYPES": [
        {"id": 1, "type": "Ring", "price_multiplier": 1},
        {"id": 2, "type": "Earrings", "price_multiplier": 2},
        {"id": 3, "type": "Necklace", "price_multiplier": 4}
    ]
}

def all(resources):
    '''return all of given resource'''
    return DATABASE[resources]
def retrieve(resources, id):
    '''return specific instance of resource by id'''
    requested_resource = None
    for resource in DATABASE[resources]:
        if resource["id"] == id:
            if resources == "ORDERS":
                requested_resource = resource.copy()
                matched_size = retrieve("SIZES", requested_resource["sizeId"])
                requested_resource["size"] = matched_size
                matched_metal = retrieve("METALS", requested_resource["metalId"])
                requested_resource["metal"] = matched_metal
                matched_style = retrieve("STYLES", requested_resource["styleId"])
                requested_resource["style"] = matched_style
                price = 0
                price += requested_resource["metal"]["price"] + requested_resource["size"]["price"] + requested_resource["style"]["price"]
                requested_resource["price"] = price
            else:
                requested_resource = resource.copy()
    return requested_resource
def create(resources, resource):
    '''for POST requests to a collection'''
    max_id = DATABASE[resources][-1]["id"]
    new_id = max_id + 1
    resource["id"] = new_id
    DATABASE[resources].append(resource)
    return resource
def update(resources, new_resource, id):
    """For PUT requests to a single resource"""
    for index, resource in enumerate(DATABASE[resources]):
        if resource["id"] == id:
            DATABASE[resources][index] = new_resource
            break
def delete(resources, id):
    """For DELETE requests to a single resource"""
    resources_index = -1
    for index, resource in enumerate(DATABASE[resources]):
        if resource["id"] == id:
            resources_index = index
    if resources_index >= 0:
        DATABASE[resources].pop(resources_index)