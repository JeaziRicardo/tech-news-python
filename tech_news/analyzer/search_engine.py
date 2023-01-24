from ..database import search_news


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
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
