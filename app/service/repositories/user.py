from abc import abstractmethod, ABC

from app.domain.entities.user import UserEntity


class UserRepository(ABC):
    @abstractmethod
    def create(self, user: UserEntity):
        pass

    @abstractmethod
    def get_by_id(self, user_id: int):
        pass
