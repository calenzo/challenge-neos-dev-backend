from app.database.adapters.link import LinkAlchemyAdapter
from app.database.models.link import LinkModel
from app.domain.entities.link import LinkEntity
from app.interactors.response_api_interactor import ResponseSuccess
from app.schemas.link_schemas import CreateLinkSchema


class CreateLinkResponseModel:
    def __init__(self, link: LinkModel):
        self.link = link

    def __call__(self):
        return ResponseSuccess(self.link.to_json())


class CreateLinkRequestModel:
    def __init__(self,
                 user_id,
                 link_schema: CreateLinkSchema,):
        self.user_id = user_id
        self.message = link_schema.message
        self.phone_number = link_schema.phone_number


class CreateLinkInteractor:
    def __init__(self,
                 request: CreateLinkRequestModel,
                 adapter: LinkAlchemyAdapter):
        self.request = request
        self.adapter = adapter

    def _create_link(self, link_entity: LinkEntity):
        return self.adapter.create(link_entity)

    def run(self):
        link_entity = LinkEntity(
            user_id=self.request.user_id,
            message=self.request.message,
            phone_number=self.request.phone_number,
        )
        link = self._create_link(link_entity)
        response = CreateLinkResponseModel(link)
        return response
