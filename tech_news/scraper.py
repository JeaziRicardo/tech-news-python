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
    selector = Selector(text=html_content)

    url = selector.css("head link[rel='canonical']::attr(href)").get()
    title = selector.css("h1::text").get().strip()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    comments_count = len(selector.css(".comment-list li").getall())
    summary = "".join(
        selector.css("div.entry-content > p:first-of-type *::text").getall())
    tags = selector.css(".post-tags ul li a::text").getall()
    category = selector.css(".meta-category a .label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary.strip().replace("\xa0", " "),
        "tags": tags,
        "category": category
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
