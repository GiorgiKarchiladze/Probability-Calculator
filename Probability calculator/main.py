import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for colour, count in kwargs.items():
            for i in range(count):
                self.contents.append(colour)

    def draw(self, count):
        drawn_contents = []
        if count <= len(self.contents):
            for i in range(count):
                drawn_contents.append(item := random.choice(self.contents))
                self.contents.remove(item)
        else:
            drawn_contents = copy.deepcopy(self.contents)
            self.contents = []

        return drawn_contents


def color_list_to_dict(color_list):
    return {color: color_list.count(color) for color in set(color_list)}


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for _ in range(num_experiments):
        local_hat = copy.deepcopy(hat)
        drawn_balls = local_hat.draw(num_balls_drawn)
        drawn_dict = color_list_to_dict(drawn_balls)

        if all(drawn_dict.get(color, 0) >= count for color, count in expected_balls.items()):
            success += 1

    return success / num_experiments


hat1 = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat1, expected_balls={'red': 2, 'green': 1}, num_balls_drawn=5, num_experiments=2000)
print(probability)
