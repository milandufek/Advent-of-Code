import os
import requests
import subprocess
from bs4 import BeautifulSoup


def scrape_title(url: str) -> None:
    response = requests.get(url)
    if response.status_code != 200:
        print(f'Failed to get the page. Status code: {response.status_code}')
        return

    bs = BeautifulSoup(response.content, 'html.parser')
    # title = bs.find('main').find('article', class_='day-desc').find('h2')
    title = bs.select_one('main article.day-desc h2')
    if not title:
        print(f'No article found...')
        return

    print(f"- [{title.get_text().strip('- ')}]({url})")


def check_solution(day: int) -> None:
    extensions = ['.py', '.ts']
    git_check = 'git ls-files --modified --others --exclude-standard'

    def check_git_status(file: str) -> bool:
        return subprocess.check_output(f'{git_check} {file}', shell=True) == b''

    p1_status = '❌'
    p2_status = '❌'

    p1_status = next(
        ('✅' if check_git_status(f'd{day}p1{ext}') else '🛠️')
        for ext in extensions
        if os.path.exists(f'd{day}p1{ext}')
    ) if any(os.path.exists(f'd{day}p1{ext}') for ext in extensions) else '❌'

    p2_status = next(
        ('✅' if check_git_status(f'd{day}p2{ext}') else '🛠️')
        for ext in extensions
        if os.path.exists(f'd{day}p2{ext}')
    ) if any(os.path.exists(f'd{day}p2{ext}') for ext in extensions) else '❌'

    print(f'  - Part 1 {p1_status} | Part 2 {p2_status}')


if __name__ == '__main__':
    for day in range(1, 26):
        url = f'https://adventofcode.com/2024/day/{day}'
        scrape_title(url)
        check_solution(day)
