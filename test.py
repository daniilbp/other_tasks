from datetime import datetime, timedelta
import re
import requests
# import time


def xpr_usdt(path):
    my_req = requests.get(path)
    str_with_price = re.findall(r'\"price\"\:\d\.\d{15}', my_req.text)
    cut_price = re.sub(r'\"price\"\:', '', str_with_price[0])
    price = float(cut_price)
    return price


site_page = 'https://www.binance.com/ru/price/xrp'
max_price = xpr_usdt(site_page)
timelimit = datetime.now() + timedelta(hours=1)
count = 0

if __name__ == '__main__':
    while True:
        count += 1
        print(f'Цикл № {count}')
        try:
            new_price = xpr_usdt(site_page)
            print(new_price)
            if new_price > max_price or datetime.now() > timelimit:
                max_price = new_price
                timelimit = datetime.now() + timedelta(hours=1)
                print(f'Новый максимум: ${max_price}')
            elif new_price < max_price * 0.99:
                max_price = new_price
                timelimit = datetime.now() + timedelta(hours=1)
                print(f'Wена упала на 1% от максимальной цены и состовляет: ${new_price}')
        except Exception:
            print('Ошибка, запрос не прошел!')

        # time.sleep(4)


# Но не секрет, что для сокращения i/o time есть практика использования асихнронных/многопоточных программ.
# Это как раз такой случай, потому что во время ожидания ответа от сервера наша программа ничего не делает,
# хотя могла бы отправлять уже другой запрос, а потом другой и т.д. Попробуем реализовать асинхронный подход к решению кейса.
#
# Хотите быть чемпионом по запросам - используйте asyncio.gather, но с тщательно подобранными лимитами.
# Если вы ходите не на один хост, а в разные источники, то вообще не стестяйтесь.


# site_page = 'https://www.binance.com/ru/price/xrp'
# max_price = 0
# count = 0
# timelimit = datetime.now() + timedelta(hours=1)
#
# while True:
#     try:
#         my_req = requests.get(site_page)
#         str_with_price = re.findall(r'\"price\"\:\d\.\d{15}', my_req.text)
#         cut_price = re.sub(r'\"price\"\:', '', str_with_price[0])
#         price = float(cut_price)
#
#         if price > max_price or datetime.now() > timelimit:
#             max_price = price
#             timelimit = datetime.now() + timedelta(hours=1)
#             print(f'Новый максимум: ${max_price}')
#         elif price < max_price * 0.99:
#             max_price = price
#             timelimit = datetime.now() + timedelta(hours=1)
#             print(f'Wена упала на 1% от максимальной цены и состовляет: ${price}')
#
#     except Exception:
#         print('Ошибка, запрос не прошел!')
#
#     time.sleep(4)
