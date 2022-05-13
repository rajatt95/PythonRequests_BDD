from Z_Utilities.Configurations import getConfig


def getBaseURL_ReqRes():
    return getConfig()['API']['application_ReqRes_Base_URL']
