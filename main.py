import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from astroridfield import AsteroidField
from shoot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # Initialize pygame
    pygame.init()
    
    # Create a clock to manage FPS
    clock = pygame.time.Clock()
    dt = 0
    
    # Font for displaying FPS
    font = pygame.font.SysFont("Arial", 18)
    
    # Create the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    astroField = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable, astroField)
    Shot.containers = (updatable, drawable, shots)
    
    
    # Create the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    asteroid_field = AsteroidField()
    
    
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return  # Exit the program after closing the window
        
        for update in updatable:
            update.update(dt)
        
        
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game Over!")
                pygame.quit()
                return
            
        for bull in shots:
            for asteroid in asteroids:
                if bull.collides_with(asteroid):
                    bull.kill()
                    asteroid.kill()
                    asteroid.split()
                    break
        
        
        pygame.Surface.fill(screen, (0, 0, 0))
        
        for draw in drawable:
            draw.draw(screen)

        # Calculate and render FPS
        fps = int(clock.get_fps())
        fps_text = font.render(f"FPS: {fps}", True, (255, 255, 255))
        
        # Display FPS on the screen
        screen.blit(fps_text, (10, 10))
        
        # Update the display
        pygame.display.flip()
        
        # Control the frame rate, set to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
