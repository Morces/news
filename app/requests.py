import urllib.request, json
from .models import Articles, Sources

# Getting api key
apiKey = None
# Getting sources base url
base_url = None
# Getting article url
article_url = None

def configure_request(app):
    global apiKey,base_url,article_url
    apiKey = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config['NEWS_ARTICLE_URL']

def find_sources(category):
    '''
    This function requests for data and processes it
    '''
    find_sources_url = base_url.format(category, apiKey)

    with urllib.request.urlopen(find_sources_url) as url:
        find_sources_data = url.read()
        find_sources_response = json.loads(find_sources_data)

        source_results = None

        if find_sources_response['articles']:
            source_results_list = find_sources_response['articles']
            source_results = process_results(source_results_list)


        return source_results


def process_results(source_list):
    '''
    Function that processes the source results and return the source list
    '''
    source_results = []

    for source in source_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        language = source.get('language')
        country = source.get('country')

        if url:
            source_object = Sources(id,name,description,url,category,language,country)
            source_results.append(source_object)

    return source_results


def process_articles(articles_list):

    article_results = []

    for article_item in articles_list:
        publishedAt = article_item.get('publishedAt')
        urlToImage = article_item.get('urlToImage')
        title = article_item.get('title')
        content = article_item.get('content')
        author = article_item.get('author')
        url = article_item.get('url')
        description = article_item.get('description')

        if urlToImage:
            article_object = Articles(publishedAt,urlToImage,title,content,author,url,description)
            article_results.append(article_object)
    
    return article_results

def get_articles(source_id):
    '''
    This function processes osource results and transforms them into a list
    '''
    get_articles_url = article_url.format(source_id, apiKey)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        
        article_results = None 

        if get_articles_response['articles']:
            article_results_list = get_articles_response['articles']
            article_results = process_articles(article_results_list)  

    return article_results
    







