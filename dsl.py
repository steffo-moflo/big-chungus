from enum import Enum
from typing import  List, Dict, Type

from selenium import webdriver

class Env(Enum):
    DEV = "dev"
    QA = "qa"
    PROD = "prod"

class ExternalConnection():
    pass

class WebDriver(ExternalConnection):
    def __init__(
        self,
        driver: webdriver.Firefox() #@TODO what is preferred browser
    ):
        self.driver = driver


class Websource():
    source_type = "websource"
    connection: Dict[Env, WebDriver]

class Newegg(Websource):
    name = "newegg",
    url = ""
    product_inventory_css_selector = "product-inventory"
    search = ""

class Amazon(Websource):
    name = "amazon"
    url = ""
    product_inventory_css_selector = "placeholdery"
    search = "nav-search-field"


all_sources = [
    Newegg,
    Amazon
]

def create_websource_connect(source: Type[Websource]):
    return Websource.connection["DEV"]