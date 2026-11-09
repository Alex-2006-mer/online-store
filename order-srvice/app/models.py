from datetime import datetime
from uuid import uuid4

from sqlalchemy.orm import  DeclarativeBase, Mapped, mapped_column



class Base(DeclarativeBase):
    id: Mapped[str] = mapped_column(
        primary_key=True,
        default=lambda: str(uuid4()),
    )


class Orders(Base):
    __tablename__ ="orders"

    user_id: Mapped[str]
    status: Mapped[str]
    total_amount: Mapped[int]
    created_at: Mapped[datetime ]