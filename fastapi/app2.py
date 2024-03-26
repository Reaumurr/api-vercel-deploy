from fastapi import FastAPI

app = FastAPI()

# df = {
#     1: {"name": "Hana", "age": 10},
#     2: {"name": "Rifdah", "age": 18}
# }

# @app.get('/data')
# def read_data():
#     return df

# @app.put("/items/{item_id}")
# def update_item(item_id: int, update_data: dict):

#     # Perform the update using the data from the request body
#     df[item_id].update(update_data)

#     return {"message": f"Item with ID {item_id} has been updated successfully."}

# data = []

# @app.get('/')
# def cart():
#     if len(data)==0:
#         return "There are no items in your cart"
#     else:
#         return data

# @app.post('/input_data/')
# def add_cart(added_item:dict):
#     id = len(data) + 1
#     added_item['id'] = id
#     data.append(added_item)
#     return added_item

df = {
    1: {"name": "Hana", "age": 10},
    2: {"name": "Rifdah", "age": 18},
    3: {"name": "Sakinah", "age": 27}
}

@app.get('/data')
def read_data():
    return df

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    df.pop(item_id)
    return {"message": f"Item with ID {item_id} has been deleted successfully."}