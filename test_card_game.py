import card_game as game
import pytest

def test_function_returns_0():
    result = game.small_function('empty')
    assert result == 1

def test_function_returns_1():
    result = game.small_function('boss')
    assert result == 0
