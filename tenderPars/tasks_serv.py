"""Серверная чсть запускающая таски ч/з celery"""
from celery import group

from tasks import task_get_links, task_get_value


links: list[str] = [
    "https://zakupki.gov.ru/epz/order/extendedsearch/results.html?fz44=on&pageNumber=1",
    "https://zakupki.gov.ru/epz/order/extendedsearch/results.html?fz44=on&pageNumber=2",
]
search_for_link = "printForm/view"
search_for_xml = "publishDTInEIS"

if __name__ == "__main__":
    ### 1v Получаем список списков ссылок на печатные формы тендеров,
    ### затем получаем склеенный р-т "ссылка"-"искомое значение"
    print_links = [
        task_get_value.delay(link, search_for_xml).get()
        for lst in [
            task_get_links.delay(link, search_for_link).get() for link in links
        ]
        for link in lst
    ]
    print(len(print_links), print_links, end='\n\n')
    
    ### 2v ч/з celery.group
    res = group(task_get_links.s(link, search_for_link) for link in links)()
    res = group(task_get_value.s(link, search_for_xml) for links in res.get() for link in links)()
    print(len(res := res.get()), res)
