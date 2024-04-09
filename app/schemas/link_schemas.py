from typing import Optional

from pydantic import BaseModel


class CreateLinkSchema(BaseModel):
    phone_number: str
    message: Optional[str]
