import random
import pytest
from random_minigame import choose_option, roll_dice, coin_flip

class Tests:

    # tests for choose_option

    def test_choose_option_returns_item_from_list(self):
        choices = ["pizza", "burger", "ramen"]
        result = choose_option(choices)
        assert result in choices

    def test_choose_option_single_item(self):
        assert choose_option(["only"]) == "only"

    def test_choose_option_numbers(self):
        result = choose_option([1, 2, 3, 4])
        assert result in [1, 2, 3, 4]

    def test_choose_option_empty_list_raises(self):
        with pytest.raises(ValueError):
            choose_option([])

    def test_choose_option_non_list_raises(self):
        with pytest.raises(TypeError):
            choose_option("not a list")

    # tests for roll_dice

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
            result = roll_dice(num_rolls, num_sides, low_val, step)

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

    def test_coin_flip(self):

        # invalid input
        with pytest.raises(TypeError):
            coin_flip("not an int")
        with pytest.raises(ValueError):
            coin_flip(-1)

        # run coin_flip many times and verify the output
        for i in range(1, 101):
            
            actual = coin_flip(i)
            assert isinstance(actual, str), f"Expected coin_flip() to return a string. Instead, it returned {type(actual)}"
            assert actual in {"heads", "tails", "tie"}, f"Expected coin_flip() to return 'heads', 'tails', or 'tie'. Instead, it returned '{actual}'"
            assert len(actual) > 0, f"Expected coin_flip() not to be empty. Instead, it returned a string with {len(actual)} characters"
