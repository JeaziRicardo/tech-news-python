from ..database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    news_list = []
    query = {"title": {"$regex": title, "$options": "i"}}
    search_list = search_news(query)
    for new in search_list:
        news_list.append((new["title"], new["url"]))
    return news_list


# Requisito 7
def search_by_date(date):
    news_list = []
    try:
        format_date = datetime.datetime.strptime(date, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )
        query = {"timestamp": {"$regex": format_date}}
        search_list = search_news(query)
        for new in search_list:
            news_list.append((new["title"], new["url"]))
        return news_list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
