import pygame
from constants import *
from circleshape import *

class Player(CircleShape) :
    def __init__(self, x, y) :
        super().__init__(x, y, PLAYER_RADIUS)
        self.x = x
        self.y = y
        self.rotation = 0
        self.radius = PLAYER_RADIUS

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
        
    def draw(self, screen) :
        self.screen = screen
        self.points = self.triangle()
        pygame.draw.polygon(screen, "white", self.points, 2)

    def rotate(self, dt) :
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt) :
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt)

    
    