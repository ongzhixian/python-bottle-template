################################################################################
# Modules and functions import statements
################################################################################

import logging
import socket
import jinja2

from datetime import datetime
from os import getenv
from jinja2 import Template, Environment, FileSystemLoader
from app_helpers import appconfig

################################################################################
# Function decorators
################################################################################

# N/A

################################################################################
# Basic functions
################################################################################

########################################
# Define filter functions
########################################

def get_year(value):
    """ZX: Lazy coding here. Assumes value is a valid datetime."""
    return value.year

########################################
# Define global functions
########################################

def get_datetime_now():
    """Returns local datetime"""
    return datetime.now()

def get_datetime_utcnow():
    """Returns local datetime in UTC"""
    return datetime.utcnow()

########################################
# Define core functions
########################################

def os_env(key):
    logging.debug("IN os_env()")
    return getenv(key)

def get_jinja2_env():
    logging.debug("Setting up jinja2 environment")
    env = Environment(loader = FileSystemLoader('./templates'))

    # Setup jinja2 globals variables/functions
    fqdn = socket.getfqdn().split(".")
    if len(fqdn) > 0:
        computer_name = fqdn[0].upper()
    else:
        computer_name = "unknown"

    # Define global variables that we can use in Jinja2 templates
    env.globals['COMPUTERNAME'] = computer_name
    env.globals['APPLICATION_NAME'] = appconfig["application"]["application_name"]
    env.globals['SITE_NAME'] = appconfig["application"]["site_name"]
    env.globals['VERSION'] = appconfig["application"]["version"]
    env.globals['VERSION_DATE'] = appconfig["application"]["version_date"]

    # Defines Jinja2 global functions
    env.globals['datetime'] = get_datetime_now
    env.globals['datetime_utc'] = get_datetime_utcnow

    # Setup jinja2 filters
    env.filters['os_env'] = os_env
    env.filters['year'] = get_year

    return env

################################################################################
# Variables dependent on Application basic functions
################################################################################

jinja2_env = get_jinja2_env()

################################################################################
# Main function
################################################################################

if __name__ == '__main__':
    pass