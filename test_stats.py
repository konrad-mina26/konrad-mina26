import pytest
from stats import calculate_stats

def test_calculate_stats_basic():
    result = calculate_stats([1, 2, 3, 4])
    assert result["sum"] == 10
    assert result["average"] == 2.5
    assert result["min"] == 1
    assert result["max"] == 4

def test_calculate_stats_single_value():
    result = calculate_stats([5])
    assert result == {
        "sum": 5,
        "average": 5,
        "min": 5,
        "max": 5
    }

def test_calculate_stats_empty_list():
    result = calculate_stats([])
    assert result["sum"] == 0
    assert result["average"] == 0
    assert result["min"] is None
    assert result["max"] is None

def test_calculate_stats_negative_numbers():
    result = calculate_stats([-1, -2, -3])
    assert result["sum"] == -6
    assert result["average"] == -2
    assert result["min"] == -3
    assert result["max"] == -1