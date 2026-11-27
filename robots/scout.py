from .agent import Agent, Config

import random

# states = explore, observe, report

class Scout(Agent):
    def __init__(self, cfg: Config):
        super().__init__(cfg)
        self.destination = None

    def update(self, world, dt):
        # view range
        targets = self.scan(world)

        for target in targets:
            world.broadcast_target(target, self.id)

        # explore
        if self.destination is None or self.dist_to(self.destination) < 10:
            self.destination = (random.uniform(0, world.width), random.uniform(0, world.height))

        self.move_toward(self.destination, dt)