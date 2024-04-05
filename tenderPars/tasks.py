import requests
import re
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
from celery import Celery


app = Celery('tasks', backend='your_conf', broker='your_conf')

session = requests.session()
headers: dict[str, str] = {
    "x-requested-with": "XMLHttpRequest",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.3.281 Yowser/2.5 Safari/537.36"
}


def search_in_xml(elem: ET, field: str) -> str:
    """
    Функция рекурсивно идущая по тэгам XML объекта пока не найден нужный тэг

    Args:
        elem (xml.etree.ElementTree): распарсенный XML объект
        field (str): искомый тэг

    Returns:
        (str): Значение искомого тэга
    """
    for child in elem:
        if field in child.tag: return child.text

    return search_in_xml([grandchild for child in elem for grandchild in child], field)


@app.task
def task_get_links(url: str, search: str) -> list[str]:
    """
    Функция которая при обходе страницы, собирает ссылки на печатную форму элемента (тендера)

    Args:
        url (str): страница для обхода
        search (str): значение содержащееся в ссылке

    Returns:
        links (list[str]): список ссылок на печатную форму элемента списка (тендера) 
    """
    request = session.get(url, headers=headers)
    soup = BeautifulSoup(request.content, "html.parser")
    ### Преобразуем ссылки в полный путь и на печатную XML-форму 
    links = [f"https://zakupki.gov.ru{link.get('href')}" for link in soup.find_all(href=re.compile(search))]
    links = [re.sub('view', 'viewXml', link) for link in links]
    
    return links


@app.task
def task_get_value(url: str, search: str):
    """
    Функция - таска, выполняtn запрос по url, распарсинг ответа
    и возвразает значения по искомому тэгу

    Args:
        url (str): ссылка на печатную форму в формате XML
        search (str): искомый тэг

    Returns:
        (str): склеенная строка в виде пары “ссылка на печатную форму”-”дата публикации”
    """
    request = session.get(url, headers=headers)
    root = ET.fromstring(request.content)
    value = res if (res := search_in_xml(root, search)) else None
    
    return f'"{url}"-"{value}"'
