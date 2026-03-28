import pytest
import random

# need to change this to be our project:
# from examplepackagefb1258 import random_minigame

class Tests:
        def example_fixture(self):
            """
            An example of a pytest fixture - a function that can be used for setup and teardown before and after test functions are run.
            """

            # place any setup you want to do before any test function that uses this fixture is run

            yield  # at the yield point, the test function will run and do its business

            # place with any teardown you want to do after any test function that uses this fixture has compl
        
        def test_sanity_check(self, example_fixture):
            """
            Test debugging... making sure that we can run a simple test that always passes.
            Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
            From the main project directory, run the `python3 -m pytest` command to run all tests.
            """
            expected = True  # the value we expect to be present
            actual = True  # the value we see in reality
            assert actual == expected, "Expected True to be equal to True!"

        def test_roll_die(self):
              # since we are rolling the dice randomly, we should check a bunch of times
              for i in range(1, 101):
                    # randomly choose the details of the dice roll(s)
                    num_rolls = random.randint(1, 10)
                    num_sides = random.randint(1, 10)
                    low_val = random.randint(1, i)
                    step = random.randint(1, i)
                    
                    # get result
                    result = random_minigame.roll_die(num_rolls, num_sides, low_val)
                    
                    # calculate which numbers are on the sides of the dice
                    numbers = []
                    for val in range(1, num_sides + 1):
                        numbers.append(val + low_val - 1)
                    
                    # calculate all possible results
                    possible_results = []
                    for 

                    assert (
                        result > low_val * num_rolls - 1
                    ), f"Expected roll_die() to return a value greater than {low_val*num_rolls - 1}. Instead, it returned {result}"

                    assert (
                        result < (low_val + num_sides - 1) * num_rolls + 1
                    ), f"Expected roll_die() to return a value less than {(low_val + num_sides - 1) * num_rolls + 1}. Instead it returned {result}"

                    assert (
                        
                    ), f"Expected roll_die() to return a linear combination of the numbers from {low_val} to {low_val + num_sides - 1}. Instead, it returned {result}"