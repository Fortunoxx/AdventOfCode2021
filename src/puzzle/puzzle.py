import requests

def FetchForDay(day):
    with open('src/puzzle/cookie.txt') as cookieFile:
        for cookie in cookieFile:
            cookies = dict(session=cookie)
            input = requests.get(f'https://adventofcode.com/2021/day/{int(day)}/input', cookies=cookies)
            with open(f'src/day{day}/input.dat', 'w') as inputFile:
                inputFile.write(input.text)
