# The web application start file
################################################################################
# Import statements
################################################################################

import json
import logging
from datetime import datetime

################################################################################
# Setup logging configuration
################################################################################

logging_format = '%(asctime)-15s %(levelname)-8s %(message)s'
#logging_format = '%(asctime)-15s %(levelname)-8s %(module)-16s %(funcName)-24s %(message)s'
logging.basicConfig(filename='python-bottle-template.log', level=logging.DEBUG, format=logging_format) # Log to file
console_logger = logging.StreamHandler() # Log to console as well
console_logger.setFormatter(logging.Formatter(logging_format))
logging.getLogger().addHandler(console_logger)

################################################################################
# Import helper modules
################################################################################

from helpers import *

################################################################################
# Setup bottle and fetch configuration
################################################################################

app = page_helpers.default_app()  

################################################################################
# Setup appconfig
################################################################################

appconfig = app_helpers.appconfig

################################################################################
# Setup jinja2 environment
################################################################################

jinja2_env = jinja2_helpers.jinja2_env



################################################################################
# Import pages modules
################################################################################

from pages import *

################################################################################
# Main function
################################################################################

if __name__ == '__main__':
    logging.info("[PROGRAM START]")
    logging.critical("%8s test message %s" % ("CRITICAL", str(datetime.utcnow())))
    logging.error("%8s test message %s" % ("ERROR", str(datetime.utcnow())))
    logging.warning("%8s test message %s" % ("WARNING", str(datetime.utcnow())))
    logging.info("%8s test message %s" % ("INFO", str(datetime.utcnow())))
    logging.debug("%8s test message %s" % ("DEBUG", str(datetime.utcnow())))
    page_helpers.run(host="0.0.0.0", port=49152, debug=True, reloader=False)
    logging.info("[PROGRAM END]")
