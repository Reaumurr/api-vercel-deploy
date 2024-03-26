from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"This is the main endpoint of this API"}

@app.get("/names/{name}")
def read_name(name):
    return {"Name": name, "Message": f"Hello, My Name is {name}"}

@app.get("/items/{id}")
def read_items(id):
    return {"id":id}