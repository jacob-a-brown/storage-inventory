from utils.db import Base
from sqlalchemy import (ForeignKey, String)
from sqlalchemy.orm import (Mapped, mapped_column, relationship)


class Container(Base):
    __tablename__ = "containers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    type: Mapped[str] = mapped_column(String(30))
    parent_id: Mapped[int | None] = mapped_column(ForeignKey("containers.id"), nullable=True)
    parent: Mapped["Container | None"] = relationship("Container", back_populates="children", remote_side=[id])
    children: Mapped[list["Container"]] = relationship("Container", back_populates="parent")
