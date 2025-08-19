# test_my_functions.py

from maximum_of_two_numbers import add, subtract

def test_add_positive_numbers():
    """Test add function with positive numbers."""
    assert add(2, 3) == 5

def test_add_negative_numbers():
    """Test add function with negative numbers."""
    assert add(-1, -5) == -6

def test_subtract_positive_numbers():
    """Test subtract function with positive numbers."""
    assert subtract(10, 4) == 6

def test_subtract_negative_result():
    """Test subtract function resulting in a negative number."""
    assert subtract(2, 7) == -5
