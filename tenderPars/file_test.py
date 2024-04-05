import unittest
import tasks

from unittest import TestCase
from celery import group


links: list[str] = [
    "https://zakupki.gov.ru/epz/order/extendedsearch/results.html?fz44=on&pageNumber=1",
    "https://zakupki.gov.ru/epz/order/extendedsearch/results.html?fz44=on&pageNumber=2",
]
search_for_link = "printForm/view"
search_for_xml = "publishDTInEIS"


class Tests(TestCase):
    def test_task_get_links(self):
        task = tasks.task_get_links.delay(links[0], search_for_link)
        res = task.get()
        
        self.assertEqual(len(res), 10)
        self.assertEqual(task.status, 'SUCCESS')


    def test_task_get_value(self):
        task1 = tasks.task_get_links.delay(links[0], search_for_link)
        res1 = task1.get()
        
        task2 = group(tasks.task_get_value.s(link, search_for_xml) for link in res1)()
        res2 = task2.get()
        
        self.assertEqual(len(res2), 10)
        self.assertTrue(task2.ready())
        self.assertTrue(task2.successful())



if __name__ == '__main__':
    unittest.main()
