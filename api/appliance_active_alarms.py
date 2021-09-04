"""
************************************************************
This module is the API call directly to appliances via the
Orchestrator.  It will retrieve a summary of the active
alarms for each appliance.
************************************************************
"""

import sys
import json
import requests
from api_methods import ApiMethods
from log_file import LogFile



class ApplianceActiveAlarms:

    @classmethod
    def active_alarms(cls, obj):
        """ This method  """

        obj.parameters = { "ids":[obj.id] }
        try:
            r = ApiMethods.post_orch("/alarm/appliance?view=active"
                                    "&orderBySeverity=true&&&", obj)
            if r.status_code == 200:
                alarm_summary = r.json()
                return alarm_summary
            else:
                print("Unable to reach Orchestrator.  See error.log for details")
                pass
        except Exception as err:
            LogFile.log_error(err)

# end
