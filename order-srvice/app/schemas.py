from pydantic import BaseModel, ConfigDict


class OrderItemCreateShema(BaseModel):
    product_name: str
    quantity: int


class OrderItemReadShema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    product_id: str
    product_name: str
    quantity: int
    unit_price: int


class OrderReadShema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    user_id: str
    status: str
    total_amount: int
    items: list[OrderItemReadShema]


class OrderCreateShema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: str
    items: list[OrderItemCreateShema]