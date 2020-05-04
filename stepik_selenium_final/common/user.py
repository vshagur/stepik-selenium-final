from uuid import uuid4


class User:
    def __init__(self, name=None, email=None, password=None):
        self.name = name or str(uuid4())[24:]
        self.email = email or f'{self.name}@example.com'
        self.password = password or str(uuid4())[24:]
