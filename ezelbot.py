
import requests
import random
import threading
from bs4 import BeautifulSoup

Z = '\033[1;31m'
B = '\033[1;36m'
F = '\033[2;32m'
W = '\033[1;39m'

token = input(Z + '[÷] Token: ')
id = input(B + '[÷] ID: ')
print(B + r'*' * 72)

def az():
    while True:
        number = ''.join(random.choices('0123456789', k=random.randint(2, 4)))
        user = f'ezel{number}'

        url = requests.get(f'https://t.me/{user}').text
        if 'tgme_username_link' in url:
            url = f'https://fragment.com/?query={user}&sort=price_asc'
            re = requests.get(url).content
            soup = BeautifulSoup(re, 'html.parser')
            cards = soup.find_all("div", {"class": "table-cell-status-thin thin-only tm-status-unavail"})
            try:
                teamB = cards[0].text.strip()
                if teamB == 'Unavailable':
                    print(F + f'good   : {user}')
                    message_text = f"""
ezel siker

<code>{user}</code>

@Ezellllj

Bot ID atanı sikerler.
"""
                    response = requests.post(
                        f'https://api.telegram.org/bot{token}/sendMessage',
                        data={
                            'chat_id': id,
                            'text': message_text,
                            'parse_mode': 'HTML'
                        }
                    )
            except:
                print(Z + f'bad   : {user}')
        else:
            print(Z + f'bad   : {user}')

Threads = []
for t in range(50):
    x = threading.Thread(target=az)
    x.start()
    Threads.append(x)
for Th in Threads:
    Th.join()
