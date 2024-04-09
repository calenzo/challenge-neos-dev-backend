from app.database.adapters.user import UserAlchemyAdapter

from app.interactors.authenticate_interactor import \
    AuthenticateInteractor

from app.interactors.response_api_interactor import (
    ResponseSuccess,
    ResponseError
)

from app.domain.entities.user import UserEntity


class PostCreateUserResponseModel:
    def __init__(self, user):
        self.user = user

    def __call__(self):
        return ResponseSuccess(self.user.to_json())


class PostCreateUserRequestModel:
    def __init__(self, user):
        self.username = user.username
        self.password1 = user.password1
        self.password2 = user.password2


class PostCreateUserInteractor:
    def __init__(self,
                 request: PostCreateUserRequestModel,
                 adapter: UserAlchemyAdapter):
        self.request = request
        self.adapter = adapter

    def _get_user_by_username(self):
        return self.adapter.get_by_username(self.request.username)

    def _check_user_exists(self):
        user = self._get_user_by_username()
        if user:
            raise ResponseError(status_code=400,
                                message="Username already registered")

    def _password_match(self):
        if self.request.password1.lower() != \
                self.request.password2.lower():
            raise ResponseError(status_code=400,
                                message="Password doesn't match")

    def _create_user(self):
        hashed_password = AuthenticateInteractor(). \
            get_password_hash(self.request.password1)

        user_entity = UserEntity(
            username=self.request.username,
            password=hashed_password,
        )

        user = self.adapter.create(user_entity)
        return user

    def run(self):
        self._check_user_exists()
        self._password_match()
        user = self._create_user()
        response = PostCreateUserResponseModel(user)
        return response
