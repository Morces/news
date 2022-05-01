from flask import render_template
from . import main
from app.requests import find_sources, get_article



#Views 
@main.route('/')
def home():
    '''
    View home page that displays/returns the home page of the app
    '''

    return render_template('home.html')


@main.route('/sources')
def index():
    '''
    View index page that displays/returns news sources
    '''
    general = find_sources()
    return render_template('index.html', message = general)


@main.route('/about/<source_id>')
def about(source_id):
    '''
    View about page that displays/returns the details of articles
    '''
    articles = get_article(source_id)
    return render_template('about.html', articles = articles)