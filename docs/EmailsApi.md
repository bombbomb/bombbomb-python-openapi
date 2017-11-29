# bombbomb.EmailsApi

All URIs are relative to *https://api.bombbomb.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_printing_press_email**](EmailsApi.md#create_printing_press_email) | **POST** /emails/print | Create an Email with Printing Press
[**get_all_templates_for_current_user**](EmailsApi.md#get_all_templates_for_current_user) | **GET** /emails/templates | Get all user templates
[**get_email_tracking**](EmailsApi.md#get_email_tracking) | **GET** /emails/{emailId}/tracking | Get Email Tracking
[**get_email_tracking_interactions**](EmailsApi.md#get_email_tracking_interactions) | **GET** /emails/{emailId}/tracking/interactions | Get Email Tracking Interactions
[**get_hourly_email_tracking**](EmailsApi.md#get_hourly_email_tracking) | **GET** /emails/{emailId}/tracking/hourly | Get Hourly Email Tracking
[**get_quick_send_templates**](EmailsApi.md#get_quick_send_templates) | **GET** /emails/quicksend/templates | Get all quicksend templates
[**video_quick_sender**](EmailsApi.md#video_quick_sender) | **POST** /emails/quicksend | Send a quicksend email


# **create_printing_press_email**
> create_printing_press_email(template_id, content, email_id=email_id, video_id=video_id, subject_line=subject_line)

Create an Email with Printing Press

Prints an email using the template id and content to the users account.If a video id is included, it will replace any video placeholders with that video.

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
email_id = 'email_id_example' # str | The email id to be printed to. (optional)
video_id = 'video_id_example' # str | A video to replace video place holders with. (optional)
subject_line = 'subject_line_example' # str | The subject line to be printed. (optional)

try: 
    # Create an Email with Printing Press
    api_instance.create_printing_press_email(template_id, content, email_id=email_id, video_id=video_id, subject_line=subject_line)
except ApiException as e:
    print "Exception when calling EmailsApi->create_printing_press_email: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| The template id to be printed. | 
 **content** | **str**| The content of the email. | 
 **email_id** | **str**| The email id to be printed to. | [optional] 
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

# **get_all_templates_for_current_user**
> get_all_templates_for_current_user(quick_send_only=quick_send_only)

Get all user templates

Get all templates accessible to the current user

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
quick_send_only = true # bool | Whether to return only quick send templates. (optional)

try: 
    # Get all user templates
    api_instance.get_all_templates_for_current_user(quick_send_only=quick_send_only)
except ApiException as e:
    print "Exception when calling EmailsApi->get_all_templates_for_current_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quick_send_only** | **bool**| Whether to return only quick send templates. | [optional] 

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

# **get_quick_send_templates**
> get_quick_send_templates()

Get all quicksend templates

Get all quicksend templates accessible to the user.

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

try: 
    # Get all quicksend templates
    api_instance.get_quick_send_templates()
except ApiException as e:
    print "Exception when calling EmailsApi->get_quick_send_templates: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **video_quick_sender**
> video_quick_sender(video_id=video_id, email_addresses=email_addresses, subject=subject, message=message, list_ids=list_ids, scheduled_send_timestamp=scheduled_send_timestamp, extended_properties=extended_properties, template_id=template_id, strip_html=strip_html)

Send a quicksend email

Send a quicksend video email to the list or users provided.

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
video_id = 'video_id_example' # str | A guid id for the video. (optional)
email_addresses = 'email_addresses_example' # str | A semi-colon separated list of email addresses to send to. (optional)
subject = 'subject_example' # str | Subject line for the email. (optional)
message = 'message_example' # str | Message for the body of the email. (optional)
list_ids = 'list_ids_example' # str | An array of list ids (optional)
scheduled_send_timestamp = 56 # int | When to schedule the send (seconds since epoch). null value means send immediately. (optional)
extended_properties = 'extended_properties_example' # str | Bool value that when checked will send back both emailId as well as extra properties (optional)
template_id = 'template_id_example' # str | Id of a template to use for this send. A null value means use the default for this user. (optional)
strip_html = 'strip_html_example' # str | remove HTML elements (optional)

try: 
    # Send a quicksend email
    api_instance.video_quick_sender(video_id=video_id, email_addresses=email_addresses, subject=subject, message=message, list_ids=list_ids, scheduled_send_timestamp=scheduled_send_timestamp, extended_properties=extended_properties, template_id=template_id, strip_html=strip_html)
except ApiException as e:
    print "Exception when calling EmailsApi->video_quick_sender: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **str**| A guid id for the video. | [optional] 
 **email_addresses** | **str**| A semi-colon separated list of email addresses to send to. | [optional] 
 **subject** | **str**| Subject line for the email. | [optional] 
 **message** | **str**| Message for the body of the email. | [optional] 
 **list_ids** | **str**| An array of list ids | [optional] 
 **scheduled_send_timestamp** | **int**| When to schedule the send (seconds since epoch). null value means send immediately. | [optional] 
 **extended_properties** | **str**| Bool value that when checked will send back both emailId as well as extra properties | [optional] 
 **template_id** | **str**| Id of a template to use for this send. A null value means use the default for this user. | [optional] 
 **strip_html** | **str**| remove HTML elements | [optional] 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

