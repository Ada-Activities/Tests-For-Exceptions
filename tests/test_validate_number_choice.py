from main import validate_number_choice
import pytest

# It's important to test that "good" input works
def test_validate_number_choice_returns_int_when_in_range():
    # Arrange - none required

    # Act - combined with assert

    # Assert
    assert validate_number_choice("1", 1, 10) == 1
    assert validate_number_choice("5", 1, 10) == 5
    assert validate_number_choice("10", 1, 10) == 10

# It's equally important to validate that any expected errors are also raised. 
# The errors raised by your functions are just as much a part of their behavior as the happy paths are.

def test_validate_number_choice_raises_for_non_int():
    # Arrange - none required

    # Act - under assert wrapper

    # Assert
    with pytest.raises(ValueError):
        validate_number_choice("a", 1, 10)

def test_validate_number_choice_raises_for_above_range():
    # Arrange - none required

    # Act - under assert wrapper

    # Assert
    with pytest.raises(ValueError):
        validate_number_choice("11", 1, 10)

def test_validate_number_choice_raises_for_below_range():
    # Arrange - none required

    # Act - under assert wrapper

    # Assert
    with pytest.raises(ValueError):
        validate_number_choice("0", 1, 10)

# There can ALWAYS be more tests! 
# What about testing the range values themselves? Are they respected? 
# We can't be certain about that from just the tests here!