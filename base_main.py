"""
***********************************************************************
This script starts with the template in base_main.py.  Building upon 
the base template, in the task specific section, the module then 
performs API calls to Orchestrator, which will then perform API calls
to each appliance to retrieve alarm summaries specific to each
appliance.
***********************************************************************
"""

import api

# User input for needed variables
url = input("OrchIP: ")
user = input("UserId: ")
pwd = input("Password: ")

# Create OrchHelper object, which is used to login to Orchestrator session
api_session = api.OrchHelper(url, user, pwd)

# for MFA login:
#    api_session.send_mfa()
#    mfa = input("Enter MFA code: ")
#    api_session.mfa_login(mfa)

# Call login method on OrchHelper object.  This will login to the
# Orchestrator, create an API session, and return information on each
# site which can be used for future API calls.
site_list = api_session.login()  

""" start task specific code here:

** Add additional code here

end task specific code """

api_session.logout()

# end
