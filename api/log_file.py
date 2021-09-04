"""
***********************************************************************
This module.......
***********************************************************************
"""

import sys
import logging

class LogFile:

    def __init__(self, hostname, id, err):
        self.hostname = hostname
        self.id = id
        self.err = err

    def log_informational(self):
        error = self.hostname + ' ' + self.id + ' ' + str(self.err)
        logging.warning(error) # send log entry to syslog.log
        with open('errors.log', 'a') as err_file: # send log entry to errors.log
            err_file.write('Unable to retrieve information from ' + str(error) + '\n')
            err_file.close()

    @classmethod
    def log_error(cls, err):
        logging.critical(err) # send log entry to syslog.log
        sys.exit("Exception - unable to connect to Orchestrator.  See syslog.log for details.")

 # end
