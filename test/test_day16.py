import pytest

from src.day16 import solve_part1, solve_part2, convertToBinary

day = "16"

testdata1 = [
    ("8A004A801A8002F478", 16),
    ("620080001611562C8802118E34", 12),
    ("C0015000016115A2E0802F182340", 23),
    ("A0016C880162017C3686B18A3D4780", 31)
]

testdata2 = [
    ("C200B40A82", 3),
    ("04005AC33890", 54),
    ("880086C3E88112", 7),
    ("CE00C43D881120", 9),
    ("D8005AC2A8F0", 1),
    ("F600BC2D8F", 0),
    ("9C005AC2F8F0", 0),
    ("9C0141080250320F1802104A08", 1)
]

@pytest.mark.parametrize("input, expected", testdata1)
def test_part1(input, expected): 
    assert solve_part1(convertToBinary(input)) == expected

@pytest.mark.parametrize("input, expected", testdata2)
def test_part2(input, expected): 
    assert solve_part2(convertToBinary(input)) == expected
