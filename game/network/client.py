import requests


class HighScoresClient:
    def __init__(self, ai_game):
        self.ai_game = ai_game
        # self.state = self.ai_game.state

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
            # self.state.logged_in_user = res.json()
            return True

        # TODO(acer0ni): Finish me

    def logout(self):
        ...

    def get_highscores(self):
        res = self.session.get("http://localhost:8000/api/score/highscore")
        if not res.ok:
            return {}
        return res.json()

    # def submit_highscore(self, score):
    #     res = self.session.post(
    #         "https://localhost:8000/api/score/",
    #         json={"score": {score}, "user_id": {self.state.logged_in_user["id"]}},
    #     )
    #     res = res.json()
    #     return res["score"]

    #     ...
