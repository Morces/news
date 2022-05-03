# from unicodedata import category
from imp import source_from_cache

from flask import render_template, request, url_for, redirect
from . import main
from ..requests import find_sources,get_articles



#Views 
@main.route('/')
def index():
    '''
    View index page that displays/returns news sources
    '''

    general = find_sources('general')
    sports = find_sources('sports')
    business = find_sources('business')
    technology = find_sources('technology')
    entertainment = find_sources('entertainment')
    science = find_sources('science')

    return render_template('index.html', source = source_from_cache, general = general, sports = sports, business = business, technology = technology, entertainment = entertainment, science = science)


@main.route('/<source_id>')
def articles(source_id):
    '''
    View about page that displays/returns the details of articles
    '''

    articles = get_articles(source_id)
    title = f'{source_id}'
    return render_template('article.html', title=title, articles = articles, name = source_id)