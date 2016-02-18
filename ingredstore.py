import requests
from lxml import html

class IngredStore:
    def __init__(self, url):
        self._geturl = url

    def get_ingredients(self):
        page = requests.get(self._geturl)
        self.__validate_web(self)
        tree = html.fromstring(page.content)
        ingredients = [li.xpath('normalize-space(.)') for li in tree.xpath('//ul[@class="ingred-list"]/li')]
        return ingredients

    def __validate_web(self):
        pass # todo

    

