
class UserEntity:
    def __init__(self,
                 id: int = None,
                 username: str = "",
                 password: str = "",
                 is_active: bool = False):
        self.id = id
        self.username = username
        self.password = password
        self.is_active = is_active

    def to_json(self):
        return vars(self)
