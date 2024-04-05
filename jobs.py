import json
from datetime import datetime, timedelta
import re
import requests

my_req = requests.get('https://yandex.ru/jobs/vacancies/')
data = json.loads(my_req.text)

print(data)


# def xpr_usdt(path):
#     my_req = requests.get(path)
#     str_with_price = re.findall(r'\"price\"\:\d\.\d{15}', my_req.text)
#     cut_price = re.sub(r'\"price\"\:', '', str_with_price[0])
#     price = float(cut_price)
#     return price
#
#
# site_page = 'https://www.binance.com/ru/price/xrp'
# max_price = xpr_usdt(site_page)
# timelimit = datetime.now() + timedelta(hours=1)
# count = 0
#
# if __name__ == '__main__':
#     while True:
#         count += 1
#         print(f'Цикл № {count}')
#         try:
#             new_price = xpr_usdt(site_page)
#             print(new_price)
#             if new_price > max_price or datetime.now() > timelimit:
#                 max_price = new_price
#                 timelimit = datetime.now() + timedelta(hours=1)
#                 print(f'Новый максимум: ${max_price}')
#             elif new_price < max_price * 0.99:
#                 max_price = new_price
#                 timelimit = datetime.now() + timedelta(hours=1)
#                 print(f'Wена упала на 1% от максимальной цены и состовляет: ${new_price}')
#         except Exception:
#             print('Ошибка, запрос не прошел!')

        # time.sleep(4)