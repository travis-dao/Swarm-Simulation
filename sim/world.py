from robots import Agent

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.agents: list[Agent] = []
        self.targets = []
        self.known_targets = []

    def broadcast_target(self, target, sender):
        if target not in self.known_targets:
            self.known_targets.append(target)

    def update(self, dt):
        for agent in self.agents:
            if agent.alive:
                agent.update(self, dt)