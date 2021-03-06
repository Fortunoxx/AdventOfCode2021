import pytest

from src.day12 import solve_part1 #, solve_part2

day = "12"

@pytest.mark.parametrize("day", [day])
def test_part1(day, expected_value = 10): 
    testdata = {"key": "sample", "file": f"test/data/day{day}.sample.dat"}
    assert solve_part1(testdata) == expected_value

@pytest.mark.parametrize("day", [day])
def test_part1_large(day, expected_value = 19): 
    testdata = {"key": "sample", "file": f"test/data/day{day}.sample-large.dat"}
    assert solve_part1(testdata) == expected_value

@pytest.mark.parametrize("day", [day])
def test_part1_even_larger(day, expected_value = 226): 
    testdata = {"key": "sample", "file": f"test/data/day{day}.sample-even-larger.dat"}
    assert solve_part1(testdata) == expected_value

# @pytest.mark.parametrize("day", [day])
# def test_part2(day, expected_value = 0): 
#     testdata = {"key": "sample", "file": f"test/data/day{day}.sample.dat"}
#     assert solve_part2(testdata) == expected_value