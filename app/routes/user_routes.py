from fastapi import APIRouter, Depends

from app.interactors.authenticate_interactor import (
    AuthenticateInteractor,
)

from app.interactors.post_create_user_interactor import (
    PostCreateUserRequestModel,
    PostCreateUserInteractor
)

from app.interactors.get_read_user_interactor import (
    GetReadUserRequestModel,
    GetReadUserInteractor,
)

from app.interactors.post_token_authenticate_interactor import (
    PostTokenAuthenticateRequestModel,
    PostTokenAuthenticateInteractor,
)

from app.schemas.user_schemas import (
    AuthRegister,
    AuthLogin,
)

from app.database.adapters.user import UserAlchemyAdapter

router = APIRouter()


@router.post('/user')
def post_create_user(user: AuthRegister):
    request = PostCreateUserRequestModel(user)
    interactor = PostCreateUserInteractor(request, UserAlchemyAdapter())

    result = interactor.run()

    return result()


@router.get('/user')
def get_read_user(
        user_id: int = Depends(AuthenticateInteractor().auth_wrapper)):
    request = GetReadUserRequestModel(user_id)
    interactor = GetReadUserInteractor(
        request,
        UserAlchemyAdapter(),
    )

    result = interactor.run()

    return result()


@router.post('/auth')
def post_token_authenticate(user: AuthLogin):
    request = PostTokenAuthenticateRequestModel(user)
    interactor = PostTokenAuthenticateInteractor(request, UserAlchemyAdapter())

    result = interactor.run()

    return result()
