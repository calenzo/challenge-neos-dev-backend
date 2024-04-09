from fastapi import APIRouter, Depends

from app.database.adapters.link import LinkAlchemyAdapter
from app.database.adapters.user import UserAlchemyAdapter

from app.interactors.authenticate_interactor import (
    AuthenticateInteractor,
)
from app.interactors.create_link_interactor import (
    CreateLinkInteractor,
    CreateLinkRequestModel,
)
from app.interactors.delete_link_interactor import (
    DeleteLinkRequestModel,
    DeleteLinkInteractor,
)
from app.interactors.list_links_interactor import (
    ListLinksRequestModel,
    ListLinksInteractor,
)

from app.schemas.link_schemas import CreateLinkSchema

router = APIRouter(prefix='/link')


@router.get("/")
def list_links(
        user_id: int = Depends(AuthenticateInteractor().auth_wrapper),):
    request = ListLinksRequestModel(user_id)
    interactor = ListLinksInteractor(
        request,
        LinkAlchemyAdapter(),
        UserAlchemyAdapter(),
    )

    result = interactor.run()

    return result()


@router.post("/")
def create_link(
        link_schema: CreateLinkSchema,
        user_id: int = Depends(AuthenticateInteractor().auth_wrapper),):
    request = CreateLinkRequestModel(user_id, link_schema)
    interactor = CreateLinkInteractor(request, LinkAlchemyAdapter())

    result = interactor.run()

    return result()


@router.delete("/{link_id}")
def list_links(link_id: int):
    request = DeleteLinkRequestModel(link_id)
    interactor = DeleteLinkInteractor(request, LinkAlchemyAdapter())

    result = interactor.run()

    return result()
