# python -m sim.main

import pygame

from .world import World
from robots import Infantry, Scout, Artillery, Config
import sim.util.draw as draw
from .config import WIDTH, HEIGHT

pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

world = World(WIDTH, HEIGHT)



world.agents.extend(Scout(Config(i, "scout", [100, 100], 50, 120, 100)) for i in range(2))
# world.agents.extend(
#     Infantry(500, 350) for _ in range(15)
# )
# world.agents.extend(
#     Artillery(800, 500) for _ in range(4)
# )

world.targets = [(250, 200), (750, 150), (600, 550)]

colors = {
    Scout: (40, 210, 200),
    Infantry: (80, 140, 255),
    Artillery: (255, 170, 50),
}

running = True

while running:
    dt = min(clock.tick(60) / 1000.0, 0.05)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    world.update(dt)

    screen.fill((25, 30, 38))

    for x, y in world.targets:
        pygame.draw.circle(screen, (240, 75, 75), (int(x), int(y)), 7)

    for agent in world.agents:
        if agent.alive:
            draw.view_cone(screen, agent)

    for agent in world.agents:
        if agent.alive:
            pygame.draw.circle(screen, colors[type(agent)], (int(agent.x), int(agent.y)), 5)
            draw.forward_direction(screen, agent)

    pygame.display.flip()

pygame.quit()