# blackrhinorandomminigame Python Package

[![Python package](https://github.com/swe-students-spring2026/3-package-black_rhino/actions/workflows/python-package.yml/badge.svg)](https://github.com/swe-students-spring2026/3-package-black_rhino/actions/workflows/python-package.yml)

## Description

A Python package to simplify game-related functions, so that developers don't have to hard-code probability and score-related code. This package includes:

- **Choose Option**: Randomly chooses an element of a list.
- **Roll Dice**: Roll a certain number of dice with custom face values.
- **Coin Flip**: Flips a heads or tails coin a custom number of times, returning heads, tails, or tie.
- **Generate Scores**: Randomly assigns scores to elements of a list.
- **Generate Teams**: Evenly breaks down a list into a custom number of teams.

## PyPi Package

This package on PyPi: [Random Minigame]()

## How to Install and Use This Package

### Installation

1. Install this package using pip:
```bash
pip install blackrhinorandomminigame
```
2. Import this package into your Python file:
```bash
import blackrhinorandomminigame as rm
```

### Usage examples

Here is how to use each function in your own code:

- **Choose Option**: 
```bash
options = ["rock", "paper", "scissors"]
choice = rm.choose_option(options)
print(f"Opponent chose: {choice}")
```
- **Roll Dice**:
```bash
total = rm.roll_dice(num_rolls=2, num_sides=6, low_val=1, step=1)
print(f"Total of dice roll: {total}")
```
- **Coin Flip**:
```bash
result = rm.coin_flip(num_flips=5)
print(f"Coin flip outcome: {result}")
```
- **Generate Scores**:
```bash
players = ["Alice", "Bob", "Charlie", "Diana"]
scores = rm.generate_scores(names=players, low_score=0, high_score=100, ties_allowed=True)
print(f"Scores: {scores}")
```
- **Generate Teams**:
```bash
players = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
teams = rm.generate_teams(names=players, num_teams=2)
print(f"Teams: {teams}")
```

### Function Documentation

| Function | Parameters | Description | Returns |
|----------|------------|-------------|---------|
| `choose_option` | `choices` (list) | Randomly selects an element from a list. Raises TypeError if not a list, ValueError if empty. | Selected element |
| `roll_dice` | `num_rolls` (int), `num_sides` (int), `low_val` (int), `step` (int) | Rolls dice where faces are generated as: low_val, low_val+step, low_val+2*step, etc. | Total sum of all dice rolls |
| `coin_flip` | `num_flips` (int) | Flips a coin the specified number of times. | "heads", "tails", or "tie" |
| `generate_scores` | `names` (list), `low_score` (int), `high_score` (int), `ties_allowed` (bool) | Assigns random scores to each name. If ties_allowed is False, ensures all scores are unique. | Dictionary mapping names to scores |
| `generate_teams` | `names` (list), `num_teams` (int) | Randomly distributes names into the specified number of teams. | Dictionary mapping team numbers to lists of members |

### Complete Example Program

Here is a full Python program demonstrating all functions together: [Example Program](example.py)

## How to Contribute to This Project

Follow these steps to set up the project locally:

1. Clone the Repository:
```bash
git clone https://github.com/swe-students-spring2026/3-package-black_rhino.git cd 3-package-black_rhino
```
2. Set Up Virtual Environment (pipenv):
```bash
pip install pipenv
pipenv shell
pipenv install
```
3. Run Tests:
```bash
pytest
```
4. Build Package:
```bash
python -m build
```
5. Exit the Virtual Environment:
```bash
exit
```

## Teammates

- [Chase Vitale](https://github.com/chasecvitale)
- [Harrison Wong](https://github.com/harrisonmangitwong)
- [Jerry Wang](https://github.com/JerrrryWang)
- [Alan Wu](https://github.com/aw4630)
- [Ethan Tan](https://github.com/ethantyr)