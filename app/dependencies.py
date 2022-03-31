import requests


class User:
    def __init__(self):
        response = requests.get("http://localhost:1234/foo/bar")
        self.user = response.json()

    def get_current_user(self):
        def wrapper(self):
            return self.user

        return wrapper


user = User()
