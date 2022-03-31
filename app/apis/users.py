from fastapi import APIRouter, Depends

from app.dependencies import user

router = APIRouter(dependencies=[Depends(user.get_current_user)])


@router.get("/user/")
def get_user():
    return {"foo": "bar"}
