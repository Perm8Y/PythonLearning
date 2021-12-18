import random

class Hat():

    def __init__(self, **color):
        self.keys = []
        self.values = []
        self.contents = []
        for key, value in color.items():
            self.keys.append(key)
            self.values.append(value)
        for i in range(len(self.values)):
            for j in range(self.values[i]):
                self.contents.append(self.keys[i])
    
    def draw(self, num):
        if num > len(self.contents):
            num = len(self.contents)
        self.draw_hand = []
        for i in range(int(num)):
            self.draw_hand.append(random.choice(self.contents))
        return self.draw_hand

##################################################################################################
##################################################################################################

    
def experiment(hat: Hat, expected_balls: dict, num_balls_drawn: int, num_experiments: int):
    balls = []
    key = list(expected_balls.keys())
    value = list(expected_balls.values())
    for i in range(len(value)):
        for j in range(value[i]):
            balls.append(key[i])

    sum_balls = 0
    for i in range(len(value)):
        sum_balls = sum_balls + value[i]

    success = 0
    for i in range(num_experiments):
        drawn = hat.draw(num_balls_drawn)
        for j in range(len(balls)):
            if balls[j] in drawn:
                drawn.remove(balls[j])
        if len(drawn) == (num_balls_drawn - sum_balls):
            success = success + 1
            continue

    prop = success/num_experiments
    return prop