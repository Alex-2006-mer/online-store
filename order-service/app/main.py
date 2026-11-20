from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends

from app.database import engine
from app.dependencies import get_order_service
from app.models import Base
from app.schemas import OrderReadShema, OrderCreateShema
from app.service import OrderService


@asynccontextmanager
async def lifespan(_: FastAPI):

    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)

@app.get("/orders/{order_id}", response_model=OrderReadShema)
def get_order(
        order_id,
        order_service: OrderService = Depends(get_order_service),
):
    return order_service.get(order_id)



@app.post("/orders/", response_model=OrderReadShema)
def create_order(
        payload: OrderCreateShema,
        order_service: OrderService = Depends(get_order_service),
):
    return order_service.create(payload)