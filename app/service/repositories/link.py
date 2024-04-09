from abc import abstractmethod, ABC

from app.domain.entities.link import LinkEntity


class LinkRepository(ABC):
    @abstractmethod
    def create(self, link: LinkEntity):
        pass

    @abstractmethod
    def get_by_id(self, link_id: int):
        pass
