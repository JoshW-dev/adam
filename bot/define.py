#Thank you jstolpe
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()


def getCreds() :
    creds = dict() # dictionary to hold everything
    creds['access_token'] = (os.getenv("Instagram-User-Access-Token-Long")) # access token for use with all api calls
    creds['graph_domain'] = 'https://graph.facebook.com/' # base domain for api calls
    creds['graph_version'] = 'v15.0' # version of the api we are hitting
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/' # base endpoint with domain and version
    creds['instagram_account_id'] = (os.getenv("Instagram-Business-Account-ID")) # users instagram account id
    return creds

#not tested
def getCredsFB() :
    creds = dict() # dictionary to hold everything
    creds['access_token'] = (os.getenv("Facebook-Page-Access-Token")) # access token for use with all api calls
    creds['graph_domain'] = 'https://graph.facebook.com/' # base domain for api calls
    creds['graph_version'] = 'v15.0' # version of the api we are hitting
    creds['endpoint_base'] = creds['graph_domain'] + creds['graph_version'] + '/' # base endpoint with domain and version
    creds['page_id'] = (os.getenv("Facebook-ID")) # facebook account id
    return creds

def makeApiCall( url, endpointParams, type) :
    """ Request data from endpoint with params

    Args:
        url: string of the url endpoint to make request from
        endpointParams: dictionary keyed by the names of the url parameters
    Returns:
        object: data from the endpoint
    """
    if type == 'POST' :
        data = requests.post( url, endpointParams ) # make get request
    else:
        data = requests.get( url, endpointParams ) # make get request
    
    response = dict() # hold response info
    response['url'] = url # url we are hitting
    response['endpoint_params'] = endpointParams #parameters for the endpoint
    response['endpoint_params_pretty'] = json.dumps( endpointParams, indent = 4 ) # pretty print for cli
    
    response['json_data'] = json.loads( data.content ) # response data from the api
    response['json_data_pretty'] = json.dumps( response['json_data'], indent = 4 ) # pretty print for cli

    return response # get and return content
