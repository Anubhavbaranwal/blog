from sqlalchemy.orm import Session
from .. import models,schemas
from fastapi import HTTPException,status

def get_all_blogs(db: Session, current_user: schemas.User):
    blogs = db.query(models.Blog).filter(models.Blog.published == True).all()
    return blogs


def create_blog(request:models.Blog,db:Session, current_user: schemas.User):
    new_blog = models.Blog(title=request.title,body=request.body,published=request.published,user_id=current_user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_blog(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available")
        # return Response(status_code=status.HTTP_404_NOT_FOUND)
    return blog

def delete_blog(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id {id} is not available")
    blog.delete(synchronize_session=False)
    db.commit()
    return "Blog deleted successfully"


def update_blog(id: int, request: schemas.Blog, db: Session, current_user: schemas.User):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    
    blog.title = request.title
    blog.body = request.body
    blog.published = request.published
    blog.user_id = current_user.id
    
    db.commit()
    db.refresh(blog)
    return blog

