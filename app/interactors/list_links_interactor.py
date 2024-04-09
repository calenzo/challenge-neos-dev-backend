from app.database.adapters.link import LinkAlchemyAdapter
from app.database.adapters.user import UserAlchemyAdapter

from app.database.models.link import LinkModel

from app.interactors.response_api_interactor import ResponseSuccess, ResponseError


class ListLinksResponseModel:
    def __init__(self, links: list[LinkModel]):
        self.links = links

    def __call__(self):
        return ResponseSuccess({
            "list": self.links
        })


class ListLinksRequestModel:
    def __init__(self,
                 user_id,):
        self.user_id = user_id


class ListLinksInteractor:
    def __init__(self,
                 request: ListLinksRequestModel,
                 link_adapter: LinkAlchemyAdapter,
                 user_adapter: UserAlchemyAdapter,):
        self.request = request
        self.link_adapter = link_adapter
        self.user_adapter = user_adapter

    def _check_user_exists(self, user_id: int):
        user = self.user_adapter.get_by_id(user_id)
        if user is None:
            raise ResponseError(message="User don't exists", status_code=404)

    def _get_links(self, user_id):
        return self.link_adapter.get_all_by_user_id(user_id)

    def run(self):
        self._check_user_exists(self.request.user_id)
        links = self._get_links(self.request.user_id)
        response = ListLinksResponseModel(links)
        return response
