import random


def choose_option(choices):
    
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

def coin_flip(num_flips):

    if not isinstance(num_flips, int):
        raise TypeError("num_flips must be an integer")
    if num_flips < 0:
        raise ValueError("num_flips cannot be negative")

    heads = 0
    tails = 0

    for flip in range(num_flips):
        
        if random.randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1

    if heads > tails:
        return "heads"
    elif tails > heads:
        return "tails"
    else:
        return "tie"

def generate_scores(names, low_score, high_score, ties_allowed):
    if low_score > high_score:
        raise ValueError("low_score must be less than or equal to high_score")

    if not ties_allowed:
        available_unique_scores = high_score - low_score + 1
        if len(names) > available_unique_scores:
            raise ValueError(
                "Not enough unique scores for all names when ties are not allowed"
            )

    name_scores = {}
    used_scores = set()

    for name in names:
        if ties_allowed:
            score = random.randint(low_score, high_score)
        else:
            while True:
                score = random.randint(low_score, high_score)
                if score not in used_scores:
                    used_scores.add(score)
                    break

        name_scores[name] = score

    return name_scores

