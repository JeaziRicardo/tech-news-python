import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        header = {"user-agent": "Fake user-agent"}
        response = requests.get(url, headers=header, timeout=3)
        if response.status_code == 200:
            return response.text
    except (requests.HTTPError, requests.ReadTimeout):
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    links_list = selector.css(".entry-thumbnail div a::attr(href)").getall()
    return links_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    link_page = selector.css("a.next::attr(href)").get()
    return link_page


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
