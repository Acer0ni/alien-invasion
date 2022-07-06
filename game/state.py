class State:
    def __init__(self):
        self.using_local_highscores = False
        self.logged_in_user = None
        self.login_screen = 1
        self.register_screen = 2
        self.logged_in_game_inactive = 3
        self.logged_in_game_active = 4
        self.skipped_login_game_inactive = 5
        self.skipped_login_game_active = 6
        self.gamestate = self.login_screen
