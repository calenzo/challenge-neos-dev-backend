from app.database.adapters.link import LinkAlchemyAdapter


from app.interactors.response_api_interactor import ResponseSuccess, ResponseError


class DeleteResponseModel:
    def __init__(self):
        pass

    def __call__(self):
        return ResponseSuccess({})


class DeleteLinkRequestModel:
    def __init__(self,
                 link_id: int,):
        self.link_id = link_id


class DeleteLinkInteractor:
    def __init__(self,
                 request: DeleteLinkRequestModel,
                 adapter: LinkAlchemyAdapter,):
        self.request = request
        self.adapter = adapter

    def _check_link_exists(self, link_id: int):
        link = self.adapter.get_by_id(link_id)
        if link is None:
            raise ResponseError(message="User don't exists", status_code=404)

    def _delete_link(self, user_id):
        return self.adapter.delete(user_id)

    def run(self):
        self._check_link_exists(self.request.link_id)
        self._delete_link(self.request.link_id)
        response = DeleteResponseModel()
        return response
