from typing import Dict
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
        res = self.session.post(
            "http://localhost:8000/api/auth/login",
            json={"username": user, "password": password},
            headers=self.headers,
        )
        return res.status_code == 200

        # TODO(acer0ni): Finish me

    def register(self, user: str, password: str):
        csrf_token = self.session.get("http://localhost:8000/api/auth/csrf")
        self.headers["X-CSRFToken"] = csrf_token.cookies.get("csrftoken")
        res = self.session.post(
            "http://localhost:8000/api/auth/register",
            json={"username": user, "password": password},
            headers=self.headers,
        )
        return res.status_code == 200

    def logout(self):
        ...

    def get_highscores(self):
        res = self.session.get("http://localhost:8000/api/score/highscore")
        if not res.ok:
            return {}
        return res.json()

    def submit_highscore(self, score) -> Dict[str, int]:
        csrf_token = self.session.get("http://localhost:8000/api/auth/csrf")
        self.headers["X-CSRFToken"] = csrf_token.cookies.get("csrftoken")
        res = self.session.post(
            "http://localhost:8000/api/score/",
            json={
                "score": score,
            },
            headers=self.headers,
        )
        return res.json()
