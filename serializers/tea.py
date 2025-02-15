from pydantic import BaseModel
from typing import Optional, List
from .comment import CommentSchema
from .user import UserResponseSchema

class TeaSchema(BaseModel):
  id: Optional[int] = True
  name: str
  in_stock: bool
  rating: int
  user: UserResponseSchema  # Includes user data associated with the tea
  comments: List[CommentSchema] = []  # Tea's comments

  class Config:
    orm_mode = True

# NEW: add a new schema for creating teas
class TeaCreate(BaseModel):
    name: str
    in_stock: bool
    rating: int
