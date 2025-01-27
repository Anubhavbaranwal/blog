from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI() # Create a FastAPI instance

@app.get("/blog") # Define a route/path with operation GET
def index(limit:int =10,sort:Optional[str]=None): # Define a function that will be called when the route is accessed 
    return {"message":f'blog list {limit}'} # Return a JSON response

@app.get("/blog/{id}") # Define a route/path with operation GET
def show(id:int): 
    return {"data":id} # Return a JSON response

@app.get("/blog/{id}/comments") # Define a route/path with operation GET
def comments(id):
    return {"data":{'1','2'}} # Return a JSON response

class Blog(BaseModel): # Create a class Blog that inherits from BaseModel
    title:str # Define a field title of type string
    body:str # Define a field body of type string
    published:Optional[bool] # Define a field published of type boolean that is optional

@app.post("/blog") # Define a route/path with operation POST
def create_blog(request:Blog):
    return {"data":f'Blog is created {request}'} # Return a JSON response
