class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        # Screen settings
        self.screen_width = 900
        self.screen_hight = 500
        self.bg_color = (230, 230, 230)

        # Ship speed
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_hight = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
