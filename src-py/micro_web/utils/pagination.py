from typing import List


class Pagination:
    def __init__(self, items: List = None, total: int = 0):
        if items is None:
            items = []

        self.items = items
        self.total = total


class Pager:
    def __init__(self, page_size: int = 20, page_num: int = 0):
        self.page_size = page_size
        self.page_num = page_num
