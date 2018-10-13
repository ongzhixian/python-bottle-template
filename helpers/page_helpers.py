################################################################################
# Import statements
################################################################################

import logging
import bottle
from bottle import default_app, run, route, request, response, redirect, abort
from app_helpers import appconfig
from datetime import datetime

################################################################################
# Function decorators
################################################################################

def require_authentication(fn):
    logging.debug("IN require_authentication(%s)" % str(fn))
    def wrapper(*args, **kwargs):
        # print 'function %s called with positional args %s and keyword args %s' % (fn.__name__, args, kwargs)
        auth_cookie_id = request.cookies.get('appconfig["application"][auth_cookie_name]')
        if not auth_cookie_id:
            logging.debug("IN auth cookie not exists")
            # redirect("/login")
            return fn(*args, **kwargs)
        else:
            logging.debug("IN auth cookie exists")
            return fn(*args, **kwargs)
    return wrapper

################################################################################
# Basic functions
################################################################################

########################################
# Define core functions
########################################

def get_default_context(request):
    context = {
        'auth_cookie'       : request.cookies.get(appconfig["application"]["auth_cookie_name"]),
        'current_datetime'  : datetime.now()
    }
    return context


################################################################################
# Variables dependent on Application basic functions
################################################################################

# N/A

################################################################################
# Main function
################################################################################

if __name__ == '__main__':
    pass