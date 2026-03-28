import pytest
import random

# need to change this to be our project:
# from examplepackagefb1258 import random_minigame

class Tests:
        def test_roll_dice(self):
              # since we are rolling the dice randomly, we should check a bunch of times
              for i in range(1, 101):
                    # randomly choose the details of the dice roll(s)
                    num_rolls = random.randint(1, 10)
                    num_sides = random.randint(1, 10)
                    low_val = random.randint(1, 10)
                    step = random.randint(1, 10)

                    min_val = low_val * num_rolls
                    max_val = (low_val + (num_sides - 1) * step) * num_rolls
                    
                    
                    # get result
                    result = random_minigame.roll_dice(num_rolls, num_sides, low_val, step)
                    
                    # calculate which numbers are on the sides of the dice
                    faces = []
                    for val in range(1, num_sides + 1):
                        faces.append(step * (val - 1) + low_val)
                    
                    # calculate all possible results
                    possible_results = {0}
                    for roll in range(num_rolls):
                        new_possible_results = set()
                        for val in possible_results:
                            for face in faces:
                                new_possible_results.add(val + face)
                        possible_results = new_possible_results

                    assert (
                        result >= min_val
                    ), f"Expected roll_dice() to return a value greater than {min_val - 1}. Instead, it returned {result}"

                    assert (
                        result <= max_val
                    ), f"Expected roll_dice() to return a value less than {max_val + 1}. Instead it returned {result}"

                    assert (
                        result in possible_results
                    ), f"Expected roll_dice() to return a linear combination of the faces of the die ({faces}). Instead, it returned {result}"