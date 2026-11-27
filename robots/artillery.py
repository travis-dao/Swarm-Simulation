from .agent import Agent, Config

# states = hold, reposition, support

class Artillery(Agent):
    def __init__(self, cfg: Config):
        super().__init__(cfg)

    def update(self, world, dt):
        pass