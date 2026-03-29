import random


def choose_option(choices):
    """
    Randomly choose one option from a non-empty list.

    Args:
        choices (list): A list of possible options.

    Returns:
        One randomly selected item from the list.

    Raises:
        TypeError: If choices is not a list.
        ValueError: If choices is empty.
    """
    if not isinstance(choices, list):
        raise TypeError("choices must be a list")
    if not choices:
        raise ValueError("choices cannot be empty")

    return random.choice(choices)

def roll_dice(num_rolls, num_sides, low_val, step):
    faces = []
    for face in range(num_sides):
        faces.append(low_val + (face * step))

    total = 0
    for roll in range(num_rolls):
        side = random.randint(0, len(faces) - 1)
        total += faces[side]
    
    return total

