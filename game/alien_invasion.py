import sys
from time import sleep
import pygame
from game.network.client import HighScoresClient
from game.settings import Settings
from game.stats import GameStats
from game.scoreboard import Scoreboard
from game.sprites.ship import Ship
from game.sprites.bullet import Bullet
from game.sprites.alien import Alien
from game.ui.button import Button
from game.screens.login import LoginScreen
from game.state import State
from game.network.client import HighScoresClient


class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """init the game ,and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.client = HighScoresClient(self)

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("alien invasion")

        # Create an instance to store game statistics, and create a scoreboard
        self.stats = GameStats(self)
        self.state = State()
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Make the Play button
        self.play_button = Button(self, 375, 375, "Play")
        self.login_screen = LoginScreen(self)

    def run_game(self):
        """start the main loop for the game"""
        while True:
            self._check_events()

            if self.state.gamestate in [
                self.state.logged_in_game_active,
                self.state.skipped_login_game_active,
            ]:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            # redraw the screen during each pass through the loop.

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_mouse_events(mouse_pos)

    def _check_mouse_events(self, mouse_pos):
        if self.state.gamestate in [
            self.state.logged_in_game_inactive,
            self.state.skipped_login_game_inactive,
        ]:
            self._check_play_button(mouse_pos)
        if self.state.gamestate == self.state.login_screen:
            self._check_active_field(mouse_pos)
            if self.login_screen.login_button.rect.collidepoint(mouse_pos):
                print("login button works")

                req = self.client.authenticate(
                    self.login_screen.username_field.text,
                    self.login_screen.password_field.text,
                )
                if not req:
                    # figure out a way to have an error message pop up
                    pass
                else:
                    self.state.gamestate = self.state.logged_in_game_inactive

            if self.login_screen.skip_button.rect.collidepoint(mouse_pos):
                print("skip button works")
                self.state.gamestate = self.state.skipped_login_game_inactive
            req = self.client.get_highscores()
            if req:
                self.stats.high_score = req["score"]
                self.sb.prep_high_score()

    def check_login_state(self):
        if self.state.gamestate in [
            self.state.logged_in_game_inactive,
            self.state.logged_in_game_inactive,
        ]:
            return True
        else:
            return False

    def _check_active_field(self, mouse_pos):
        if self.login_screen.username_field.input_rect.collidepoint(mouse_pos):
            self.login_screen.username_field.is_active = True
        else:
            self.login_screen.username_field.is_active = False
        if self.login_screen.password_field.input_rect.collidepoint(mouse_pos):
            self.login_screen.password_field.is_active = True
        else:
            self.login_screen.password_field.is_active = False

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and self.state.gamestate in [
            self.state.logged_in_game_inactive,
            self.state.skipped_login_game_inactive,
        ]:
            # REset the game statistics
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            status = self.check_login_state()
            if status:
                self.state.gamestate = self.state.logged_in_game_active
            else:
                self.state.gamestate = self.state.skipped_login_game_active

            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """responds to keypresses"""
        if self.state.gamestate in [
            self.state.logged_in_game_active,
            self.state.skipped_login_game_active,
        ]:
            if event.key == pygame.K_RIGHT:
                # move the ship to the right
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                self._fire_bullet()
        elif self.state.gamestate == self.state.login_screen:
            if self.login_screen.username_field.is_active:
                if event.key == pygame.K_BACKSPACE:
                    self.login_screen.username_field.text = (
                        self.login_screen.username_field.text[:-1]
                    )
                else:
                    self.login_screen.username_field.text += event.unicode
            elif self.login_screen.password_field.is_active:
                if event.key == pygame.K_BACKSPACE:
                    self.login_screen.password_field.text = (
                        self.login_screen.password_field.text[:-1]
                    )
                else:
                    self.login_screen.password_field.text += event.unicode

    def _check_keyup_events(self, event):
        """responds to key releases"""
        if self.state.gamestate in [
            self.state.logged_in_game_active,
            self.state.skipped_login_game_active,
        ]:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            if event.key == pygame.K_LEFT:
                self.ship.moving_left = False

    def _fire_bullet(self):
        """create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disapeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Resposnd to bullet-alien collisions"""
        # remove any bullets and aliens that have collided
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

    def _update_screen(self):
        """updates images on the screen and flip the the new screen"""
        if self.state.gamestate == self.state.login_screen:
            self.login_screen.display_login_page()
        elif self.state.gamestate in [
            self.state.logged_in_game_active,
            self.state.skipped_login_game_active,
            self.state.logged_in_game_inactive,
            self.state.skipped_login_game_inactive,
        ]:
            self.draw_game()

    def draw_game(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive
        if self.state.gamestate in [
            self.state.logged_in_game_inactive,
            self.state.skipped_login_game_inactive,
        ]:
            self.play_button.rect.center = self.screen.get_rect().center
            self.play_button.draw_button()
        pygame.display.flip()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of alines in a row
        # space between each alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fir on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (3 * alien_height) - ship_height
        )
        number_rows = available_space_y // (2 * alien_height)

        # create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                # create an alien and put it in the row
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """
        Check if the fleet is at an edge,
        then update the positions of all aliens in the fleet.
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left, and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(0.5)
        else:
            logged_in = self.check_login_state()
            if logged_in:
                self.state.gamestate = self.state.logged_in_game_inactive
                # self.client.submit_highscore(self.stats.score)
            else:
                self.state.gamestate = self.state.skipped_login_game_inactive
                # save score locally
                self.sb.check_high_score()

            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship for hit.
                self._ship_hit()
                break


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
