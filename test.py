import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


ua = UserAgent()


header = {
    "User-Agent": ua.random
}


