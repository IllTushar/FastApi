from turtle import title
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

class Blog(BaseModel):
    title:str
    name :str
    published:Optional[bool]



@app.post('/blog')
def login(blog: Blog):
    return {'data':f'The title is {blog.title} {blog.name}'}


