from contextlib import asynccontextmanager


from fastapi import FastAPI, Depends


from sqlalchemy.orm import Session



from app.database import get_db

from app.models import Base
from app.database import engine
from app.schemas import OrderReadShema


@asynccontextmanager
async def lifespan(_: FastAPI):

    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)

@app.get("orders/{order_id}", response_model=OrderReadShema)
def get_order(
        order_id,
        db:Session = Depends(get_db),
):
    ...