
class LinkEntity:
    def __init__(self,
                 id: int = None,
                 phone_number: str = "",
                 message: str = "",
                 user_id: int = None,):
        self.id = id
        self.phone_number = phone_number
        self.message = message
        self.user_id = user_id
