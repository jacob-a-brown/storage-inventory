from utils.db import Base
from sqlalchemy import (
    Column,
    UUID,
    String,
    Float,
    Boolean,
    ForeignKey,
    Mapped,
    mapped_column
)

class Container(Base):
    __tablename__ = "containers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    type: Mapped[str] = mapped_column(String(30))