from sqlalchemy import and_

from app.database.settings import ConnectionDatabase
from app.database.models.link import LinkModel

from app.service.repositories.link import LinkRepository

from app.domain.entities.link import LinkEntity


class LinkAlchemyAdapter(LinkRepository, ConnectionDatabase):
    def __init__(self):
        super().__init__()

    def create(self, link_entity: LinkEntity):
        link = LinkModel(
            phone_number=link_entity.phone_number,
            message=link_entity.message,
            user_id=link_entity.user_id,
        )
        self.session.add(link)
        self.session.commit()
        self.session.refresh(link)
        self.session.close()
        return link

    def get_by_id(self, link_id: int):
        link = self.session.query(LinkModel).filter(
            LinkModel.id == link_id).first()
        self.session.close()
        return link

    def get_by_user_id(self, user_id: int):
        link = self.session.query(LinkModel).filter(
            LinkModel.user_id == user_id).first()
        self.session.close()
        return link

    def get_all_by_user_id(self, user_id: int):
        link = self.session.query(LinkModel).filter(
            LinkModel.user_id == user_id).all()
        self.session.close()
        return link

    def delete(self, link_id: int):
        link = self.session.query(LinkModel).filter(
            LinkModel.id == link_id).first()
        self.session.delete(link)
        self.session.commit()
        self.session.close()
        return link
