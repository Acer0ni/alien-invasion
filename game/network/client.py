from typing import Dict
import requests


class HighScoresClient:
    def __init__(self, ai_game):

        self.session = requests.Session()
        self.headers = {"accept": "application/json"}
        self.url = ai_game.settings.hs_server_url
        self.online = self.ping()

    def authenticate(self, user: str, password: str) -> bool:
        if not user or not password:
            return False
        if not self.online:
            return False
        csrf_token = self.session.get(f"{self.url}/api/auth/csrf")
        self.headers["X-CSRFToken"] = csrf_token.cookies.get("csrftoken")
        res = self.session.post(
            f"{self.url}/api/auth/login",
            json={"username": user, "password": password},
            headers=self.headers,
        )
        return res.status_code == 200

    def ping(self):
        try:
            self.session.get(f"{self.url}/api/auth/csrf")
        except requests.ConnectionError:
            return False
        return True

    def register(self, user: str, password: str):
        if not self.online:
            return False
        csrf_token = self.session.get(f"{self.url}/api/auth/csrf")
        self.headers["X-CSRFToken"] = csrf_token.cookies.get("csrftoken")
        res = self.session.post(
            f"{self.url}/api/auth/register",
            json={"username": user, "password": password},
            headers=self.headers,
        )
        return res.status_code == 200

    def logout(self):
        ...

    def get_highscores(self):
        if not self.online:
            return False
        res = self.session.get(f"{self.url}/api/score/highscore")
        if not res.ok:
            return {}
        return res.json()

    def submit_highscore(self, score) -> Dict[str, int]:
        if not self.online:
            return False
        csrf_token = self.session.get(f"{self.url}/api/auth/csrf")
        self.headers["X-CSRFToken"] = csrf_token.cookies.get("csrftoken")
        res = self.session.post(
            f"{self.url}/api/score/",
            json={
                "score": score,
            },
            headers=self.headers,
        )
        return res.json()
