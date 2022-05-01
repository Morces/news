from flask import render_template

from . import main


@main.app_errorhandler(404)
def error(error):
    '''
    This function renders the error page
    '''

    return render_template('error.html'), 404