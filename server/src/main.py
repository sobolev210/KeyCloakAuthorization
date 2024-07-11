from fastapi import FastAPI, Depends

from src.dependencies import get_user_id_from_token

app = FastAPI()


@app.get("/")
def root_endpoint(user_id: str = Depends(get_user_id_from_token)):
    return {"user_id": user_id}
