from contextlib import asynccontextmanager
from http.client import HTTPException

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette import status

from app.config import get_settings
from app.database import get_db
from app.schemas import ProductCreateSchema, ProductReadSchema
from app.models import Base, Product
from app.database import engine


settings = get_settings()

@asynccontextmanager
async def lifespan(_: FastAPI):
    from app.models import Product
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)




@app.get(
    "/products",
         response_model=list[ProductReadSchema],
)

def get_products(
    db: Session = Depends(get_db),
):
    query = select(Product).order_by(Product.name)
    return list[Product](db.scalars(query).all())



@app.get(
    "/products/{product_id}",
         response_model=ProductReadSchema,
)

def get_product(
        product_id: str,
        db: Session = Depends(get_db),
):

    product = db.get(Product, product_id)

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "Товар не найден",
        )

    return product



@app.post(
    "/products",
          response_model=ProductCreateSchema,
          status_code=status.HTTP_201_CREATED,
)
def crete_product(
        pyload: ProductCreateSchema,
        db: Session = Depends(get_db),
):

    new_product = Product(**pyload.model_dump())
    db.add(new_product)
    db.commit()
    return new_product