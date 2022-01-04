import requests
import os

def FetchForDay(day):
    with open('src/puzzle/cookie.txt') as cookieFile:
        for cookie in cookieFile:
            cookies = dict(session=cookie)
            result = requests.get(f'https://adventofcode.com/2021/day/{int(day)}/input', cookies=cookies)
            filename = f'src/data/day{day}.input.dat'
            if not os.path.exists(filename):
                with open(filename, 'x') as inputFile:
                    inputFile.write(result.text)
            return filename

def FetchTextForDay(day):
    with open('src/puzzle/cookie.txt') as cookieFile:
        for cookie in cookieFile:
            cookies = dict(session=cookie)
            result = requests.get(f'https://adventofcode.com/2021/day/{int(day)}/input', cookies=cookies)
            return result.text
