import pytest
from random_minigame import choose_option

def test_choose_option_returns_item_from_list():
    choices = ["pizza", "burger", "ramen"]
    result = choose_option(choices)
    assert result in choices

def test_choose_option_single_item():
    assert choose_option(["only"]) == "only"

def test_choose_option_numbers():
    result = choose_option([1, 2, 3, 4])
    assert result in [1, 2, 3, 4]

def test_choose_option_empty_list_raises():
    with pytest.raises(ValueError):
        choose_option([])

def test_choose_option_non_list_raises():
    with pytest.raises(TypeError):
        choose_option("not a list")