class Sources:
    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url 
        self.category = category
        self.language = language
        self.country = country

class Articles:
    def __init__(self,publishedAt,urlToImage,title,content,author,url,description):
        self.publishedAt = publishedAt
        self.urlToImage = urlToImage
        self.title = title
        self.content = content
        self.author = author
        self.url = url
        self.description = description