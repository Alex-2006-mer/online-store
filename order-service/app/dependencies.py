from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.catalog_client import CatalogClient
from app.config import settings
from app.database import get_db
from app.service import OrderService


def get_catalog_client() -> CatalogClient:
    return CatalogClient(
        base_url=settings.catalog_service_url,
        # timeout_secinds=settings.http_timeout_seconds,
    )


def get_order_service(
        db: Annotated[Session, Depends(get_db)],
        catalog_client: Annotated[CatalogClient, Depends(get_catalog_client)]
) -> OrderService:
    return OrderService(db, catalog_client)