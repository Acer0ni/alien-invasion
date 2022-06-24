import requests


class HighScoresClient:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {"accept": "application/json"}

    def authenticate(self, user: str, password: str) -> bool:
        print(f"username: {user}")
        print(f"pwd: {password}")
        if not user or not password:
            return False

        csrf_token = self.session.get("http://localhost:8000/api/auth/csrf")
        self.headers["X-CSRFToken"] = csrf_token.cookies.get("csrftoken")
        res = self.session.post(
            "http://localhost:8000/api/auth/login",
            json={"username": user, "password": password},
            headers=self.headers,
        )
        if res.status_code != 200:
            return False
        else:
            return True

        # TODO(acer0ni): Finish me

    def logout(self):
        ...

    def get_highscores(self):
        res = self.session.get("http://localhost:8000/api/score/highscore")
        if not res.ok:
            return {}
        return res.json()

    def submit_highscore(self, score):
        ...
