import requests


class HighScoresClient:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {"accept": "application/json"}

    def authenticate(self, user: str, password: str) -> bool:
        if not user or not password:
            return False

        csrf_token = self.session.get("http://localhost:8000/api/auth/csrf")
        self.headers["X-CSRFToken"] = csrf_token.cookies.get("csrftoken")
        res = self.session.get("")
        # TODO(acer0ni): Finish me

    def logout(self):
        ...

    def get_highscores(self):
        res = self.session.get("http://localhost:8000/api/highscores/")
        if not res.ok:
            return {}
        return res.json()

    def submit_highscore(self, score):
        ...
