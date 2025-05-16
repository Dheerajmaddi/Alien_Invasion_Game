import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        # Add a clock to monitor the time
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption('Alien Invasion')

        # Create a ship instance
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            # Add ship element to screen
            self.ship.blitme()
            
            # Make the most recently drawn screen available.
            pygame.display.flip()
            # Make the clock tick
            self.clock.tick(60)


if __name__ == '__main__':
    # Make a game instance, and run the game.
    alien_invasion_game = AlienInvasion()
    alien_invasion_game.run_game()
