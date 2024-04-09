from sqlalchemy import Column, Integer, String, ForeignKey

from app.database.settings import Base


class LinkModel(Base):
    __tablename__ = "TB_LINK"

    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String(255))
    message = Column(String(255))

    user_id = Column(Integer, ForeignKey("TB_USER.id"))

    def to_json(self):
        return vars(self)
