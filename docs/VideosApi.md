# bombbomb.VideosApi

All URIs are relative to *https://api.bombbomb.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_video_encoding_status**](VideosApi.md#get_video_encoding_status) | **GET** /videos/{videoId}/status | Video Encoding Status
[**get_video_recorder**](VideosApi.md#get_video_recorder) | **GET** /videos/live/getRecorder | Get Live Video Recorder HTML
[**mark_live_recording_complete**](VideosApi.md#mark_live_recording_complete) | **POST** /videos/live/markComplete | Completes a live recording
[**sign_upload**](VideosApi.md#sign_upload) | **POST** /video/signedUpload | Generate Signed Url
[**update_video_thumbnail_v2**](VideosApi.md#update_video_thumbnail_v2) | **PUT** /videos/thumbnail | Upload thumbnail


# **get_video_encoding_status**
> VideoEncodingStatusResponse get_video_encoding_status(video_id)

Video Encoding Status

Get information about the current state of encoding for a given video id.

### Example
```python
from __future__ import print_function
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
configuration = bombbomb.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.VideosApi(bombbomb.ApiClient(configuration))
video_id = 'video_id_example' # str | The video's id.

try:
    # Video Encoding Status
    api_response = api_instance.get_video_encoding_status(video_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_video_encoding_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The video&#39;s id. | 

### Return type

[**VideoEncodingStatusResponse**](VideoEncodingStatusResponse.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_recorder**
> VideoRecorderMethodResponse get_video_recorder(width=width, video_id=video_id)

Get Live Video Recorder HTML

Returns an object with a number of properties to help you put a video recorder on your site.         This is to be used in conjunction with the VideoRecordedLive call one the user has confirmed in your UI that         the video is how they want it.

### Example
```python
from __future__ import print_function
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
configuration = bombbomb.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.VideosApi(bombbomb.ApiClient(configuration))
width = 56 # int | The width of the recorder to present. (optional)
video_id = 'video_id_example' # str | The id of the video to record (optional)

try:
    # Get Live Video Recorder HTML
    api_response = api_instance.get_video_recorder(width=width, video_id=video_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_video_recorder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **width** | **int**| The width of the recorder to present. | [optional] 
 **video_id** | **str**| The id of the video to record | [optional] 

### Return type

[**VideoRecorderMethodResponse**](VideoRecorderMethodResponse.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_live_recording_complete**
> VideoPublicRepresentation mark_live_recording_complete(video_id, filename, title)

Completes a live recording

Used in conjunction with the live recorder method to mark a video recording as complete.

### Example
```python
from __future__ import print_function
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
configuration = bombbomb.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.VideosApi(bombbomb.ApiClient(configuration))
video_id = 'video_id_example' # str | The id of the video to mark as done.
filename = 'filename_example' # str | The filename that was chosen as the final video.
title = 'title_example' # str | The title to give the video

try:
    # Completes a live recording
    api_response = api_instance.mark_live_recording_complete(video_id, filename, title)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->mark_live_recording_complete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The id of the video to mark as done. | 
 **filename** | **str**| The filename that was chosen as the final video. | 
 **title** | **str**| The title to give the video | 

### Return type

[**VideoPublicRepresentation**](VideoPublicRepresentation.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sign_upload**
> str sign_upload(policy, v4=v4)

Generate Signed Url

Generates a signed url to be used for video uploads.

### Example
```python
from __future__ import print_function
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bombbomb.VideosApi()
policy = bombbomb.SignUploadRequest() # SignUploadRequest | The policy to sign
v4 = true # bool | Whether to do v4 signing (optional)

try:
    # Generate Signed Url
    api_response = api_instance.sign_upload(policy, v4=v4)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->sign_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | [**SignUploadRequest**](SignUploadRequest.md)| The policy to sign | 
 **v4** | **bool**| Whether to do v4 signing | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_video_thumbnail_v2**
> update_video_thumbnail_v2(video_id, thumbnail, custom=custom)

Upload thumbnail

Upload a new video thumbnail

### Example
```python
from __future__ import print_function
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
configuration = bombbomb.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.VideosApi(bombbomb.ApiClient(configuration))
video_id = 'video_id_example' # str | The id of the video
thumbnail = 'thumbnail_example' # str | The thumbnail being uploaded
custom = true # bool | The default email to use. (optional)

try:
    # Upload thumbnail
    api_instance.update_video_thumbnail_v2(video_id, thumbnail, custom=custom)
except ApiException as e:
    print("Exception when calling VideosApi->update_video_thumbnail_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| The id of the video | 
 **thumbnail** | **str**| The thumbnail being uploaded | 
 **custom** | **bool**| The default email to use. | [optional] 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

