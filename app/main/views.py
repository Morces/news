import imp
from flask import render_template
from . import main


#Views 
@main.route('/')
def home():
    '''
    View home page that displays/returns the home page of the app
    '''

    return render_template('home.html')


@main.route('/')
def index():
    '''
    View index page that displays/returns news sources
    '''

    return render_template('index.html')


@main.route('/')
def about():
    '''
    View about page that displays/returns the details of articles
    '''

    return render_template('about.html')