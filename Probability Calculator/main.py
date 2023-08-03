# main.py
import prob_calculator

hat = prob_calculator.Hat(blue=5, red=4, green=2)

# Example experiment
probability = prob_calculator.experiment(hat=hat,
                                         expected_balls={"red": 1, "green": 2},
                                         num_balls_drawn=4,
                                         num_experiments=10000)

print(probability)  # This will output an approximate probability based on 10000 experiments
