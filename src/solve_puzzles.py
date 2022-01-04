import day24
import day23
import day22
import day21
import day20
import day19
import day18
import day17
import day16
import day15
import day14
import day13
# import day12
import day11
import day10
import day09
import day08
import day07
import day06
import day05
import day04
import day03
import day02
import day01
import sys
sys.path.append('src/puzzle')
import puzzle

def getFileInfo(day, key="input"):
    return {"key": key, "file": f"src/data/day{day}.input.dat"}


# download all puzzles
for i in range(24):
    day = str(i+1)
    if len(day) == 1:
        day = "0" + day
    print(f"fetching data for day {day}")
    filename = puzzle.FetchForDay(day)
    print(f"Done: {filename}")

print(f"Day 01: Part 1: {day01.solve_part1(getFileInfo('01'))}")
print(f"Day 01: Part 2: {day01.solve_part2(getFileInfo('01'))}")
print(f"Day 02: Part 1: {day02.solve_part1(getFileInfo('02'))}")
print(f"Day 02: Part 2: {day02.solve_part2(getFileInfo('02'))}")
print(f"Day 03: Part 1: {day03.solve_part1(getFileInfo('03'))}")
print(f"Day 03: Part 2: {day03.solve_part2(getFileInfo('03'))}")
print(f"Day 04: Part 1: {day04.solve_part1(getFileInfo('04'))}")
print(f"Day 04: Part 2: {day04.solve_part2(getFileInfo('04'))}")
print(f"Day 05: Part 1: {day05.solve_part1(getFileInfo('05'))}")
print(f"Day 05: Part 2: {day05.solve_part2(getFileInfo('05'))}")
print(f"Day 06: Part 1: {day06.solve_part1(getFileInfo('06'))}")
print(f"Day 06: Part 2: {day06.solve_part2(getFileInfo('06'))}")
print(f"Day 07: Part 1: {day07.solve_part1(getFileInfo('07'))}")
print(f"Day 07: Part 2: {day07.solve_part2(getFileInfo('07'))}")
print(f"Day 08: Part 1: {day08.solve_part1(getFileInfo('08'))}")
print(f"Day 08: Part 2: {day08.solve_part2(getFileInfo('08'))}")
print(f"Day 09: Part 1: {day09.solve_part1(getFileInfo('09'))}")
print(f"Day 09: Part 2: {day09.solve_part2(getFileInfo('09'))}")
print(f"Day 10: Part 1: {day10.solve_part1(getFileInfo('10'))}")
print(f"Day 10: Part 2: {day10.solve_part2(getFileInfo('10'))}")
print(f"Day 11: Part 1: {day11.solve_part1(getFileInfo('11'), 100)}")
print(f"Day 11: Part 2: {day11.solve_part2(getFileInfo('11'), 300)}")
# print(f"Day 12: Part 1: {day12.solve_part1(getFileInfo('12'))}")
# print(f"Day 12: Part 2: {day12.solve_part2(getFileInfo('12'))}")
print(f"Day 13: Part 1: {day13.solve_part1(getFileInfo('13'))}")
print(f"Day 13: Part 2: {day13.solve_part2(getFileInfo('13'))}")
print(f"Day 14: Part 1: {day14.solve_part1(getFileInfo('14'))}")
print(f"Day 14: Part 2: {day14.solve_part2(getFileInfo('14'))}")
print(f"Day 15: Part 1: {day15.solve_part1(getFileInfo('15'))}")
print(f"Day 15: Part 2: {day15.solve_part2(getFileInfo('15'))}")
print(f"Day 16: Part 1: {day16.solve_part1(getFileInfo('16'))}")
print(f"Day 16: Part 2: {day16.solve_part2(getFileInfo('16'))}")
print(f"Day 17: Part 1: {day17.solve_part1(getFileInfo('17'))}")
print(f"Day 17: Part 2: {day17.solve_part2(getFileInfo('17'))}")
# print(f"Day 18: Part 1: {day18.solve_part1(getFileInfo('18'))}")
# print(f"Day 18: Part 2: {day18.solve_part2(getFileInfo('18'))}")
# print(f"Day 19: Part 1: {day19.solve_part1(getFileInfo('19'))}")
# print(f"Day 19: Part 2: {day19.solve_part2(getFileInfo('19'))}")
# print(f"Day 20: Part 1: {day20.solve_part1(getFileInfo('20'))}")
# print(f"Day 20: Part 2: {day20.solve_part2(getFileInfo('20'))}")
# print(f"Day 21: Part 1: {day21.solve_part1(getFileInfo('21'))}")
# print(f"Day 21: Part 2: {day21.solve_part2(getFileInfo('21'))}")
# print(f"Day 22: Part 1: {day22.solve_part1(getFileInfo('22'))}")
# print(f"Day 22: Part 2: {day22.solve_part2(getFileInfo('22'))}")
# print(f"Day 23: Part 1: {day23.solve_part1(getFileInfo('23'))}")
# print(f"Day 23: Part 2: {day23.solve_part2(getFileInfo('23'))}")
# print(f"Day 24: Part 1: {day24.solve_part1(getFileInfo('24'))}")
# print(f"Day 24: Part 2: {day24.solve_part2(getFileInfo('24'))}")
