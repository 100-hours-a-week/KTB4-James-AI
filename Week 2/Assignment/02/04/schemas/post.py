from pydantic import BaseModel, Field
class PostCreate(BaseModel):
    author:str=Field(min_length=2,max_length=30)
    title:str=Field(min_length=1,max_length=120)
    content:str=Field(min_length=1,max_length=5000)
