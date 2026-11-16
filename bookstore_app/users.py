"""User accounts: registration and login."""


class Users:
    def __init__(self):
        self.users = {}   # username -> password

def login(self, username, password):
    """Return True if the username exists and the password matches."""
    stored = self.users.get(username)
    return stored is not None and stored == password
