from fastapi import APIRouter
from src.service import auth
from src.models import user_model

router_auth = APIRouter(prefix="/auth")


@router_auth.get("/check-user")
def check_user(email: str):
    print("paso por routes")
    return auth.check_user(email)

@router_auth.post("/sing-up")
def sing_up(user: user_model.user_register):
    return auth.sing_up(user)