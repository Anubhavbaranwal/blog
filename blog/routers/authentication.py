from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas,models,JWTtoken
from sqlalchemy.orm import Session
from ..database import get_db
from ..hashing import Hash
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    tags=["Authentication"],
    # prefix="/auth"
)

@router.post("/login",response_model=schemas.Token)
def login(request: OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Incorrect Password")
    access_token = JWTtoken.create_access_token(
        data={"sub": user.email,"id":user.id}
    )
    return schemas.Token(access_token=access_token, token_type="bearer")