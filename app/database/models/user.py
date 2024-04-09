from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.settings import Base
from app.database.adapters.link import LinkModel


class UserModel(Base):
    __tablename__ = "TB_USER"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255))
    password = Column(String(255))
    is_active = Column(Boolean, default=True)

    link = relationship("LinkModel")

    def to_json(self):
        return vars(self)
