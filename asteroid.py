import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        split_angle = random.uniform(20, 50)
        asteroid1_vector = self.velocity.rotate(split_angle)
        asteroid2_vetor = self.velocity.rotate(-split_angle)
        new_asteroids_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroids_radius)
        new_asteroid1.velocity = asteroid1_vector * 1.2
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroids_radius)
        new_asteroid2.velocity = asteroid2_vetor * 1.2