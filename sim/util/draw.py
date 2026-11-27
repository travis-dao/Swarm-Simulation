import pygame
import math
from sim.config import WIDTH, HEIGHT

def view_cone(screen, agent):
    half_fov = math.radians(agent.fov / 2)
    heading = agent.heading
    segments = 40

    points = [(agent.x, agent.y)]

    for i in range(segments + 1):
        angle = heading - half_fov + (
            2 * half_fov * i / segments
        )

        x = agent.x + math.cos(angle) * agent.view_range
        y = agent.y + math.sin(angle) * agent.view_range

        points.append((x, y))

    # Draw translucent cone
    cone_surface = pygame.Surface(
        (WIDTH, HEIGHT), pygame.SRCALPHA
    )

    pygame.draw.polygon(
        cone_surface,
        (40, 210, 200, 45),
        points,
    )

    # Draw cone outline
    pygame.draw.lines(
        cone_surface,
        (40, 210, 200, 140),
        False,
        points[1:],
        1,
    )

    pygame.draw.line(
        cone_surface,
        (40, 210, 200, 140),
        points[0],
        points[1],
        1,
    )

    pygame.draw.line(
        cone_surface,
        (40, 210, 200, 140),
        points[0],
        points[-1],
        1,
    )

    screen.blit(cone_surface, (0, 0))

def forward_direction(screen, agent, length=18,
                           color=(245, 245, 245)):
    start = (int(agent.x), int(agent.y))

    end_x = agent.x + math.cos(agent.heading) * length
    end_y = agent.y + math.sin(agent.heading) * length
    end = (int(end_x), int(end_y))

    pygame.draw.line(screen, color, start, end, 2)