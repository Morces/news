from urllib.request import Request
# import requests as Request

from .models import Articles, Sources

# Getting api key
api_key = None

# Getting sources base url
base_url = None

# Getting article url
article_url = None

def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config['NEWS_ARTICLE_URL']

def find_sources():
    '''
    This function requests for data and processes it
    '''
    
    with Request.get(base_url.format(api_key)) as data:
        data = data.json()
        source_list = data.get('sources')
        source_results = []
        for source in source_list:
            id = source.get('id')
            name = source.get('name')
            source_object = Sources(id, name)
            source_results.append(source_object)
        return source_results

def get_article(source):
    '''
    This function processes osource results and transforms them into a list
    '''
    
    with Request.get(article_url.format(source, api_key)) as data:
        data = data.json()
        article_list = data.get('articles')
        article_results = []
        for art in article_list:
            publishedAt = art.get('publishedAt')
            urlToImage = art.get('urlToImage')
            title = art.get('title')
            content = art.get('content')
            author = art.get('author')
            url = art.get('url')
            description = art.get('description')
            article_object = Articles(publishedAt,urlToImage,title,content,author,url,description)
            article_results.append(article_object)

        return article_results
    

