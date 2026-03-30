import random


def choose_option(choices):
    
    if not isinstance(choices, list):
        raise TypeError("choices must be a list")
    if not choices:
        raise ValueError("choices cannot be empty")

    return random.choice(choices)

def roll_dice(num_rolls, num_sides, low_val, step):

    #check to make sure the inputs are integers
    if not isinstance(num_rolls, int):
        raise TypeError("num_rolls must be an integer")
    
    elif not isinstance(num_sides, int):
        raise TypeError("num_sides must be an integer")
    
    elif not isinstance(low_val, int):
        raise TypeError("low_val must be an integer")
    
    elif not isinstance(step, int):
        raise TypeError("step must be an integer")
    
    # check to make sure the inputs are valid integers
    if (num_rolls < 1):
        raise TypeError("num_rolls must be greater than 0")
    
    elif (num_sides < 1):
        raise TypeError("num_sides must be greater than 0")
    
    elif (low_val < 0):
        raise TypeError("low_val must be greater than or equal to 0")
    
    elif (step < 1):
        raise TypeError("step must be greater than 0")

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

def generate_teams(names, num_teams):
    """
    Distributes `names` into teams in a randomized order.
    names: list of member names. 
    num_teams: int number of teams to create.
    Returns a dictionary that maps team number to a list of members.
    """
    if num_teams < 1:
        raise ValueError("num_teams must be >= 1")

    members = list(names)
    random.shuffle(members)

    teams = {}
    i = 1
    while i <= num_teams:
        teams[i] = []
        i += 1

    team_no = 1
    for member in members:
        teams[team_no].append(member)
        team_no += 1
        if team_no > num_teams:
            team_no = 1

    return teams
