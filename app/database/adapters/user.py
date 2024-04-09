from app.database.settings import ConnectionDatabase
from app.database.models.user import UserModel

from app.service.repositories.user import UserRepository

from app.domain.entities.user import UserEntity


class UserAlchemyAdapter(UserRepository, ConnectionDatabase):
    def __init__(self):
        super().__init__()

    def create(self, user: UserEntity):
        user = UserModel(
            username=user.username,
            password=user.password,
        )
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        self.session.close()
        return user

    def get_by_id(self, user_id: int):
        user = self.session.query(UserModel).filter(
            UserModel.id == user_id).first()
        self.session.close()
        return user

    def get_by_username(self, username: str):
        user = self.session.query(UserModel).filter(
            UserModel.username == username).first()
        self.session.close()
        return user
