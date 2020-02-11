import getpass
import os
from cloudmesh.common.console import Console
from cloudmesh.common.util import banner
from cloudmesh.common.util import HEADING
from cloudmesh.common.variables import Variables
from cloudmesh.common.debug import VERBOSE



variables = Variables()

variables['debug'] = True
variables['trace'] = True
# I need this explained I am not sure what verbose in cloudmesh being higher means.
variables['verbose'] = 10

userEnvVar = ['LOGNAME', 'USER', 'LNAME', 'USERNAME']

def getCurrentUser():
    values = []
    for nameVar in userEnvVar:
        userNameValue = os.getenv(nameVar, "NONE")
        values.append(userNameValue)
        if userNameValue != "NONE":
            banner(userNameValue)
    HEADING()
    return values

def useVerbose(arr1, arr2):
    nameDict = dict(zip(arr1,arr2))
    VERBOSE(nameDict)

useVerbose(userEnvVar, getCurrentUser())


