from app.database.adapters.user import UserAlchemyAdapter

from app.interactors.response_api_interactor import ResponseSuccess

from app.domain.entities.user import UserEntity


class GetReadUserResponseModel:
    def __init__(self, user: UserEntity):
        self.user = user

    def __call__(self):
        return ResponseSuccess(self.user.to_json())


class GetReadUserRequestModel:
    def __init__(self, user_id):
        self.user_id = user_id


class GetReadUserInteractor:
    def __init__(self,
                 request: GetReadUserRequestModel,
                 user_adapter: UserAlchemyAdapter()):
        self.request = request
        self.user_adapter = user_adapter

    def _get_user(self):
        return self.user_adapter.get_by_id(user_id=self.request.user_id)

    def run(self):
        user = self._get_user()
        response = GetReadUserResponseModel(user)
        return response
