from pydantic import BaseModel, ConfigDict


class ProductCreateSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str   
    description: str
    price: int
    image: str
    category: str


class ProductReadSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    description: str
    price: int
    image: str
    category: str