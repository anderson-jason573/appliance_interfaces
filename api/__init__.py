"""
***************************************************************
This script initializes the 'api' package, when it is imported.
It imports all of the classes to be used from the modules in
the api package.
***************************************************************
"""

import logging
from .login import OrchHelper
from .appliance_info import ApplianceInfo
from .appliance_active_alarms import ApplianceActiveAlarms
from .progress_bar import ProgressBar
from .log_file import LogFile

logging.basicConfig(filename = 'syslog.log', level = logging.DEBUG,
                    format = '%(asctime)s -%(levelname)s -%(message)s')

#end
