from fastapi import APIRouter,Depends,status,Response,HTTPException
from .. import schemas,models,hashing
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..repository import blog
from ..oauth2 import get_current_user

router = APIRouter(
    tags=["Blogs"],
    prefix="/blog"
)


@router.get("/",response_model = List[schemas.ShowBlog])
def get_all_blogs(db:Session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all_blogs(db, current_user)



@router.post("/",status_code=status.HTTP_201_CREATED)
def create_blog(request:schemas.Blog,db:Session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
    return blog.create_blog(request, db, current_user)

@router.get("/{id}",response_model=schemas.ShowBlog)
def get_blog(id:int,db:Session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
    return blog.get_blog(id,db)
    

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int,db:Session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
    return blog.delete_blog(id,db)
    

@router.put("/{id}")
def update_blog(id:int,request:schemas.Blog,db:Session = Depends(get_db),current_user: schemas.User = Depends(get_current_user)):
    return blog.update_blog(id, request, db, current_user)
