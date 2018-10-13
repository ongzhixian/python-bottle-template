################################################################################
# Modules and functions import statements
################################################################################

import pdb
from helpers.app_helpers import *
from helpers.page_helpers import *
from helpers.jinja2_helpers import *

################################################################################
# Setup helper functions
################################################################################

# N/A

################################################################################
# Setup commonly used routes
################################################################################

@route('/favicon.ico')
def get_favicon():
    return bottle.static_file('favicon.ico', root='./')

@route('/<filename:path>')  
def static(filename):  
    '''  
    Serve static files
    '''  
    return bottle.static_file(filename, root='./static')

@route('/')
def display_home_page(errorMessages=None):
    context = get_default_context(request)
    return jinja2_env.get_template('html/site/home-page.html').render(context)

@route('/about')
def display_about_page(errorMessages=None):
    context = get_default_context(request)
    return jinja2_env.get_template('html/site/about-page.html').render(context)

@route('/contact')
def display_contact_page(errorMessages=None):
    context = get_default_context(request)
    return jinja2_env.get_template('html/site/contact-page.html').render(context)
