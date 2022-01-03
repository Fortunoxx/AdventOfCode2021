import pytest

from src.day11 import solve_part1, solve_part2

day = "11"

@pytest.mark.parametrize("day", [day])
def test_part1(day, expected_value = 204): 
    testdata = {"key": "sample", "file": f"test/data/day{day}.sample.dat"}
    assert solve_part1(testdata, 10) == expected_value

@pytest.mark.parametrize("day", [day])
def test_part1(day, expected_value = 1656): 
    testdata = {"key": "sample", "file": f"test/data/day{day}.sample.dat"}
    assert solve_part1(testdata, 100) == expected_value

@pytest.mark.parametrize("day", [day])
def test_part2(day, expected_value = 195): 
    testdata = {"key": "sample", "file": f"test/data/day{day}.sample.dat"}
    assert solve_part2(testdata, 200) == expected_value