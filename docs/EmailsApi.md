# bombbomb.EmailsApi

All URIs are relative to *https://api.bombbomb.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_printing_press_email**](EmailsApi.md#create_printing_press_email) | **POST** /emails/print | Create an Email with Printing Press
[**get_email_tracking**](EmailsApi.md#get_email_tracking) | **GET** /emails/{emailId}/tracking | Get Email Tracking
[**get_email_tracking_interactions**](EmailsApi.md#get_email_tracking_interactions) | **GET** /emails/{emailId}/tracking/interactions | Get Email Tracking Interactions
[**get_hourly_email_tracking**](EmailsApi.md#get_hourly_email_tracking) | **GET** /emails/{emailId}/tracking/hourly | Get Hourly Email Tracking


# **create_printing_press_email**
> create_printing_press_email(template_id, content, replace, video_id=video_id, subject_line=subject_line)

Create an Email with Printing Press

Prints an email using the template id and content to the users account.If a video id, is include it will replace any video placeholders with that video.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.EmailsApi()
template_id = 'template_id_example' # str | The template id to be printed.
content = 'content_example' # str | The content of the email.
replace = true # bool | Set whether to replace video placeholders with video id.
video_id = 'video_id_example' # str | A video to replace video place holders with. (optional)
subject_line = 'subject_line_example' # str | The subject line to be printed. (optional)

try: 
    # Create an Email with Printing Press
    api_instance.create_printing_press_email(template_id, content, replace, video_id=video_id, subject_line=subject_line)
except ApiException as e:
    print "Exception when calling EmailsApi->create_printing_press_email: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template id to be printed. | 
 **content** | **str**| The content of the email. | 
 **replace** | **bool**| Set whether to replace video placeholders with video id. | 
 **video_id** | **str**| A video to replace video place holders with. | [optional] 
 **subject_line** | **str**| The subject line to be printed. | [optional] 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_tracking**
> get_email_tracking(email_id, job_id=job_id)

Get Email Tracking

Get Tracking data for all sends of an Email

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.EmailsApi()
email_id = 'email_id_example' # str | ID of the email
job_id = 'job_id_example' # str | ID of the Job (or null for all jobs) (optional)

try: 
    # Get Email Tracking
    api_instance.get_email_tracking(email_id, job_id=job_id)
except ApiException as e:
    print "Exception when calling EmailsApi->get_email_tracking: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | **str**| ID of the email | 
 **job_id** | **str**| ID of the Job (or null for all jobs) | [optional] 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_tracking_interactions**
> get_email_tracking_interactions(email_id, job_id=job_id, interaction_type=interaction_type, search_term=search_term)

Get Email Tracking Interactions

Get Contact detail interactions for an Email

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.EmailsApi()
email_id = 'email_id_example' # str | ID of the email
job_id = 'job_id_example' # str | ID of the Job (or null for all jobs) (optional)
interaction_type = 'interaction_type_example' # str | Interaction type to order and filter by (optional)
search_term = 'search_term_example' # str | Search term to filer by (optional)

try: 
    # Get Email Tracking Interactions
    api_instance.get_email_tracking_interactions(email_id, job_id=job_id, interaction_type=interaction_type, search_term=search_term)
except ApiException as e:
    print "Exception when calling EmailsApi->get_email_tracking_interactions: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | **str**| ID of the email | 
 **job_id** | **str**| ID of the Job (or null for all jobs) | [optional] 
 **interaction_type** | **str**| Interaction type to order and filter by | [optional] 
 **search_term** | **str**| Search term to filer by | [optional] 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hourly_email_tracking**
> get_hourly_email_tracking(email_id, job_id=job_id, interaction_type=interaction_type)

Get Hourly Email Tracking

Get Tracking data for an Email,             broken down by the hour and filterable by an Interaction type

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.EmailsApi()
email_id = 'email_id_example' # str | ID of the email
job_id = 'job_id_example' # str | ID of the Job (or null for all jobs) (optional)
interaction_type = 'interaction_type_example' # str | Interaction type to filter by (optional)

try: 
    # Get Hourly Email Tracking
    api_instance.get_hourly_email_tracking(email_id, job_id=job_id, interaction_type=interaction_type)
except ApiException as e:
    print "Exception when calling EmailsApi->get_hourly_email_tracking: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | **str**| ID of the email | 
 **job_id** | **str**| ID of the Job (or null for all jobs) | [optional] 
 **interaction_type** | **str**| Interaction type to filter by | [optional] 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

