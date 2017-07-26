# bombbomb.SocialsApi

All URIs are relative to *https://api.bombbomb.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_social_article_properties**](SocialsApi.md#get_social_article_properties) | **GET** /socials/properties | Gets the social email properties
[**get_social_auto_shares**](SocialsApi.md#get_social_auto_shares) | **GET** /socials/shares | Gets the auto shares from the client group assoc id
[**get_social_permissions**](SocialsApi.md#get_social_permissions) | **GET** /socials/permissions | Get permissions for social integration
[**get_social_status**](SocialsApi.md#get_social_status) | **GET** /socials/states | Gets the social state
[**update_social_auto_shares**](SocialsApi.md#update_social_auto_shares) | **PUT** /socials/shares | Gets the auto shares from the client group assoc id
[**update_social_message**](SocialsApi.md#update_social_message) | **PUT** /socials/message | Sets the users social message to what they typed in
[**update_social_status**](SocialsApi.md#update_social_status) | **PUT** /socials/state | Updates the social state for the object


# **get_social_article_properties**
> get_social_article_properties(jericho_id, email_id, originator_id)

Gets the social email properties

Gets the social email properties

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.SocialsApi()
jericho_id = 'jericho_id_example' # str | associated jericho Id
email_id = 'email_id_example' # str | This is the email Id for the email url
originator_id = 'originator_id_example' # str | This is the originator Id

try: 
    # Gets the social email properties
    api_instance.get_social_article_properties(jericho_id, email_id, originator_id)
except ApiException as e:
    print "Exception when calling SocialsApi->get_social_article_properties: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jericho_id** | **str**| associated jericho Id | 
 **email_id** | **str**| This is the email Id for the email url | 
 **originator_id** | **str**| This is the originator Id | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_social_auto_shares**
> get_social_auto_shares(client_group_id)

Gets the auto shares from the client group assoc id

Gets the auto shares from the client group assoc id

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.SocialsApi()
client_group_id = 'client_group_id_example' # str | ID of the client group association

try: 
    # Gets the auto shares from the client group assoc id
    api_instance.get_social_auto_shares(client_group_id)
except ApiException as e:
    print "Exception when calling SocialsApi->get_social_auto_shares: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_group_id** | **str**| ID of the client group association | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_social_permissions**
> get_social_permissions(social_type)

Get permissions for social integration

Get permissions for social integration and has redirect for user to login

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.SocialsApi()
social_type = 'social_type_example' # str | Type of social integration

try: 
    # Get permissions for social integration
    api_instance.get_social_permissions(social_type)
except ApiException as e:
    print "Exception when calling SocialsApi->get_social_permissions: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_type** | **str**| Type of social integration | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_social_status**
> get_social_status(originator_id)

Gets the social state

Gets the social state

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.SocialsApi()
originator_id = 'originator_id_example' # str | associated originatorId

try: 
    # Gets the social state
    api_instance.get_social_status(originator_id)
except ApiException as e:
    print "Exception when calling SocialsApi->get_social_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **originator_id** | **str**| associated originatorId | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_social_auto_shares**
> update_social_auto_shares(auto_share, client_group_id)

Gets the auto shares from the client group assoc id

Gets the auto shares from the client group assoc id

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.SocialsApi()
auto_share = 'auto_share_example' # str | The social share that will auto share to
client_group_id = 'client_group_id_example' # str | ID of the client group association

try: 
    # Gets the auto shares from the client group assoc id
    api_instance.update_social_auto_shares(auto_share, client_group_id)
except ApiException as e:
    print "Exception when calling SocialsApi->update_social_auto_shares: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_share** | **str**| The social share that will auto share to | 
 **client_group_id** | **str**| ID of the client group association | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_social_message**
> update_social_message(message, originator_id)

Sets the users social message to what they typed in

Sets the users social message to what they typed in

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.SocialsApi()
message = 'message_example' # str | The social message the user typed in
originator_id = 'originator_id_example' # str | The parent id tied to the social share

try: 
    # Sets the users social message to what they typed in
    api_instance.update_social_message(message, originator_id)
except ApiException as e:
    print "Exception when calling SocialsApi->update_social_message: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**| The social message the user typed in | 
 **originator_id** | **str**| The parent id tied to the social share | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_social_status**
> update_social_status(state, originator_id)

Updates the social state for the object

Updates the social state for the object

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.SocialsApi()
state = 'state_example' # str | The state to set to
originator_id = 'originator_id_example' # str | The parent id tied to the social share

try: 
    # Updates the social state for the object
    api_instance.update_social_status(state, originator_id)
except ApiException as e:
    print "Exception when calling SocialsApi->update_social_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| The state to set to | 
 **originator_id** | **str**| The parent id tied to the social share | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

