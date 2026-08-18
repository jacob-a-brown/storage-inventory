from utils.db import Base
from sqlalchemy import (ForeignKey, String)
from sqlalchemy.orm import (Mapped, mapped_column, relationship)
from datetime import datetime, date


class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    container_id: Mapped[int] = mapped_column(ForeignKey("containers.id"))
    container: Mapped["Container"] = relationship("Container", back_populates="items")
    name: Mapped[str] = mapped_column(String(30))
    date_added: Mapped[datetime] = mapped_column()
    expiration_date: Mapped[date | None] = mapped_column()
