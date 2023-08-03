# prob_calculator.py
import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for ball, count in balls.items():
            self.contents.extend([ball] * count)

    def draw(self, num_balls):
        drawn_balls = random.sample(self.contents, min(num_balls, len(self.contents)))
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        copied_hat = copy.deepcopy(hat)
        drawn_balls = copied_hat.draw(num_balls_drawn)

        expected_balls_copy = copy.deepcopy(expected_balls)
        for ball in drawn_balls:
            if ball in expected_balls_copy:
                expected_balls_copy[ball] -= 1

        success = all(expected <= 0 for expected in expected_balls_copy.values())
        if success:
            success_count += 1

    probability = success_count / num_experiments
    return probability
