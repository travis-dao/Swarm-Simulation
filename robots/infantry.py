from .agent import Agent

# states = patrol, respond, regroup, avoid_obstacle

class Infantry(Agent):
    def __init__(self):
        super().__init__()