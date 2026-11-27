from dataclasses import dataclass
import math

@dataclass
class Config:
    id: int
    role: str
    pos: list[float]
    speed: float
    fov: float # deg
    view_range: float
    heading: float = 0.0  # Degrees; 0 = right, 90 = up

class Agent:
    def __init__(self, cfg: Config):
        self.id = cfg.id
        self.role = cfg.role
        self.pos = cfg.pos
        self.speed = cfg.speed
        self.fov = cfg.fov
        self.view_range = cfg.view_range
        self.heading = math.radians(cfg.heading)

        self.state = "idle"
        self.alive = True
        self.goal = None
        self.known_events = {}

    @property
    def x(self):
        return self.pos[0]

    @property
    def y(self):
        return self.pos[1]

    def scan(self, world) -> list:
        """Passively scan and return all visible targets."""
        visible = []
        half_fov = math.radians(self.fov / 2)

        for target in world.agents:
            if target.id == self.id or not target.alive:
                continue

            dx = target.pos[0] - self.x
            dy = target.pos[1] - self.y
            distance = math.hypot(dx, dy)

            if distance > self.view_range:
                continue

            if distance == 0:
                visible.append(target)
                continue

            target_angle = math.atan2(dy, dx)
            angle_diff = math.atan2(math.sin(target_angle - self.heading), math.cos(target_angle - self.heading))

            if abs(angle_diff) <= half_fov:
                visible.append(target)

        return visible


    def dist_to(self, target: list[float]) -> float:
        dx = target[0] - self.pos[0]
        dy = target[1] - self.pos[1]
        return math.hypot(dx, dy)

    def move_toward(self, target, dt):
        dx = target[0] - self.x
        dy = target[1] - self.y
        distance = math.hypot(dx, dy)

        if distance > 0:
            self.heading = math.atan2(dy, dx)
            step = min(self.speed * dt, distance)
            self.pos[0] += dx / distance * step
            self.pos[1] += dy / distance * step

    def update(self, world, dt):
        raise NotImplementedError