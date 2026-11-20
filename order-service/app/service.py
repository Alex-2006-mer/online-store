
from sqlalchemy.orm import Session

from app.catalog_client import CatalogClient
from app.models import Order, OrderItem
from app.config import NotFoundError
from app.schemas import OrderCreateShema, OrderReadShema


class OrderService:
    def __init__(self, db: Session, catalog_client: CatalogClient):
        self.db = db
        self.catalog_client = catalog_client

    def create(self, order_data: OrderCreateShema) -> OrderReadShema:
        products = []
        for item in order_data.items:
            product = self.catalog_client.get_product(item.product_id)
            products.append({
                "product_id": product['id'],
                "product_name": product['name'],
                "quantity": item.quantity,
                "unit_price": product['price'],
            })
        total_amount = sum(product["unit_price"] * product["quantity"] for product in products)
        order = Order(user_id=order_data.user_id, status="create", total_amount = total_amount)
        self.db.add(order)
        self.db.flush()

        order_items = [OrderItem(order_id=order.id, **product) for product in products]
        self.db.add_all(order_items)
        self.db.commit()
        self.db.refresh(order)

        return OrderReadShema.model_validate(order)



    def get(self, order_id: str):
        order = self.db.get(Order, order_id)
        if order is None:
            return NotFoundError
        return order