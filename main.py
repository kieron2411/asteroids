import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    font = pygame.font.Font(None, 36) 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    play_again = True

    while play_again:
        #initialising variables
        updatable.empty()
        drawable.empty()
        asteroids.empty()
        shots.empty()

        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        asteroid_field = AsteroidField()
        dt = 0
        score = 0
        
        #main game loop
        playing = True
        while playing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                    play_again = False
                
            screen.fill("black")

            for object in updatable:
                object.update(dt)

            for asteroid in asteroids:
                if asteroid.collision(player):
                    print(f"Game over! Score: {int(score // 1)}")
                    playing = False
                
                for shot in shots:
                    if asteroid.collision(shot):
                        shot.kill()
                        asteroid.split()
                        score += 5

            for object in drawable:
                object.draw(screen)
            score_text = font.render(f'Score: {int(score // 1)}', True, (255, 255, 255))
            screen.blit(score_text, (10, 10))
            pygame.display.flip()
            

            #limit the framerate to 60 FPS
            dt = clock.tick(60) / 1000
            score += 1 / 60

        #game over loop
        game_over = True
        while game_over:
            screen.fill((0, 0, 0))
            game_over_text = font.render(f'Game Over! Score: {int(score // 1)}', True, (255, 255, 255))
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 50))
            screen.blit(game_over_text, game_over_rect)

            restart_text = font.render('Press R to Restart', True, (255, 255, 255))
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
            screen.blit(restart_text, restart_rect)

            quit_text = font.render('Press Q to Quit', True, (255, 255, 255))
            quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))
            screen.blit(quit_text, quit_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                    play_again = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # Reset game variables and restart the loop
                        dt = 0
                        score = 0
                        playing = True
                        game_over = False
                    elif event.key == pygame.K_q:
                        game_over = False
                        play_again = False

            pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()