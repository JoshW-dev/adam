import time
import define
import download

def createMediaObject(params):
    """ Create media object
    Args:
        params: dictionary of params
    
    API Endpoint:
        https://graph.facebook.com/v15.0/{ig-user-id}/media?image_url={image-url}&caption={caption}&access_token={access-token}
        https://graph.facebook.com/v15.0/{ig-user-id}/media?video_url={video-url}&caption={caption}&access_token={access-token}
    Returns:
        object: data from the endpoint
    """
    url = params['endpoint_base'] + params['instagram_account_id'] + '/media' # endpoint url
    endpointParams = dict() # parameter to send to the endpoint
    endpointParams['caption'] = params['caption']  # caption for the post
    endpointParams['access_token'] = params['access_token'] # access token

    if 'IMAGE' == params['media_type'] : # posting image
        endpointParams['image_url'] = params['media_url']  # url to the asset
    else : # posting video
        endpointParams['media_type'] = params['media_type']  # specify media type
        endpointParams['video_url'] = params['media_url']  # url to the asset
    
    return define.makeApiCall( url, endpointParams, 'POST' ) # make the api call

def getMediaObjectStatus( mediaObjectId, params ) :
	""" Check the status of a media object
	Args:
		mediaObjectId: id of the media object
		params: dictionary of params
	
	API Endpoint:
		https://graph.facebook.com/v5.0/{ig-container-id}?fields=status_code
	Returns:
		object: data from the endpoint
	"""

	url = params['endpoint_base'] + '/' + mediaObjectId # endpoint url

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['fields'] = 'status_code' # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	return define.makeApiCall( url, endpointParams, 'GET' ) # make the api callgetMediaObjectStatus

def publishMedia( mediaObjectId, params ) :
	""" Publish content
	Args:
		mediaObjectId: id of the media object
		params: dictionary of params
	
	API Endpoint:
		https://graph.facebook.com/v5.0/{ig-user-id}/media_publish?creation_id={creation-id}&access_token={access-token}
	Returns:
		object: data from the endpoint
	"""

	url = params['endpoint_base'] + params['instagram_account_id'] + '/media_publish' # endpoint url

	endpointParams = dict() # parameter to send to the endpoint
	endpointParams['creation_id'] = mediaObjectId # fields to get back
	endpointParams['access_token'] = params['access_token'] # access token

	return define.makeApiCall( url, endpointParams, 'POST' ) # make the api call


#Main posting method
def postImage (url, caption):
    params = define.getCreds() # get creds from defines
    params['media_type'] = 'IMAGE' # type of asset
    #must be png
    params['media_url'] = url # url on public server for the post
    params['caption'] = caption
 
    imageMediaObjectResponse = createMediaObject( params ) # create a media object through the api
    imageMediaObjectId = imageMediaObjectResponse['json_data']['id'] # id of the media object that was created
    imageMediaStatusCode = 'IN_PROGRESS';

    print( "\n---- IMAGE MEDIA OBJECT -----\n" ) # title
    print( "\tID:" ) # label
    print( "\t" + imageMediaObjectId ) # id of the object

    while imageMediaStatusCode != 'FINISHED' : # keep checking until the object status is finished
        imageMediaObjectStatusResponse = getMediaObjectStatus( imageMediaObjectId, params ) # check the status on the object
        imageMediaStatusCode = imageMediaObjectStatusResponse['json_data']['status_code'] # update status code

        print( "\n---- IMAGE MEDIA OBJECT STATUS -----\n" ) # display status response
        print( "\tStatus Code:" ) # label
        print( "\t" + imageMediaStatusCode ) # status code of the object
        time.sleep( 5 ) # wait 5 seconds if the media object is still being processed

    publishImageResponse = publishMedia( imageMediaObjectId, params ) # publish the post to instagram

    print( "\n---- PUBLISHED IMAGE RESPONSE -----\n" ) # title
    print( "\tResponse:" ) # label
    print( publishImageResponse['json_data_pretty'] ) # json response from ig api

def postOutputImages():
    print("Posting Output to Instagram")
    hastags="#News #AI #Art #BBC"
    #test auto post image
    urlPrefix = "https://mj-gallery.com/"
    urlSuffix = "/grid_0.png"

    images = download.parseOutput()
    for image in images:
        try:
            prompt = image.split("##")[0]
            jobID = image.split("##")[1].replace("/", "" )
            caption = image.split("##")[2]            
            url = urlPrefix + jobID + urlSuffix
            instaCaption = prompt + "-BBC News"+"\n\n"+hastags            
            postImage(url,instaCaption)
        except:
            print("Insta Posting: An exception occurred")