import random

def roll_dice(num_rolls, num_sides, low_val, step):
    faces = []
    for face in range(num_sides):
        faces.append(low_val + (face * step))

    sum = 0
    for roll in range(num_rolls):
        side = random.randint(0, len(faces) - 1)
        sum += faces[side]
    
    return sum