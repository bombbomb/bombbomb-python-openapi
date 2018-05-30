# bombbomb.IntegrationsApi

All URIs are relative to *https://api.bombbomb.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connect_integration**](IntegrationsApi.md#connect_integration) | **POST** /integrations | Activate an integration for a user.
[**delete_integration**](IntegrationsApi.md#delete_integration) | **DELETE** /integrations | Remove an integration for a user.
[**get_integration_health**](IntegrationsApi.md#get_integration_health) | **GET** /integrations/health/{code} | Get health for a given integration
[**get_integration_page_components**](IntegrationsApi.md#get_integration_page_components) | **GET** /integrations/pageComponents | Get page components for a given integration
[**sync_users_integrated_lists**](IntegrationsApi.md#sync_users_integrated_lists) | **GET** /integrations/sync | Synchronize your integration list or lists.


# **connect_integration**
> connect_integration(code, key=key, secret=secret, token=token, data=data, overwrite=overwrite)

Activate an integration for a user.

Provide the correct parameters to enable an integration. Required Parameters vary based on the desired          integration. Integrations requiring OAuth will provide the OAuth link that the user must be presented.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.IntegrationsApi()
code = 'code_example' # str | The identifier of the integration.
key = 'key_example' # str | The key value. (optional)
secret = 'secret_example' # str | The secret value. (optional)
token = 'token_example' # str | The token value. (optional)
data = 'data_example' # str | The data value as JSON. (optional)
overwrite = 'overwrite_example' # str | Boolean value to know whether or not to delete the integration if it already exists (optional)

try: 
    # Activate an integration for a user.
    api_instance.connect_integration(code, key=key, secret=secret, token=token, data=data, overwrite=overwrite)
except ApiException as e:
    print "Exception when calling IntegrationsApi->connect_integration: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The identifier of the integration. | 
 **key** | **str**| The key value. | [optional] 
 **secret** | **str**| The secret value. | [optional] 
 **token** | **str**| The token value. | [optional] 
 **data** | **str**| The data value as JSON. | [optional] 
 **overwrite** | **str**| Boolean value to know whether or not to delete the integration if it already exists | [optional] 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_integration**
> delete_integration(id=id, code=code)

Remove an integration for a user.

Remove an integration by providing the integration id or integration code. Only provide one of the             parameters.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.IntegrationsApi()
id = 'id_example' # str | Integration ID (optional)
code = 'code_example' # str | Integration Code (optional)

try: 
    # Remove an integration for a user.
    api_instance.delete_integration(id=id, code=code)
except ApiException as e:
    print "Exception when calling IntegrationsApi->delete_integration: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Integration ID | [optional] 
 **code** | **str**| Integration Code | [optional] 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration_health**
> get_integration_health(code)

Get health for a given integration

Get health for an integration.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.IntegrationsApi()
code = 'code_example' # str | The integration code for which to retrieve the information from

try: 
    # Get health for a given integration
    api_instance.get_integration_health(code)
except ApiException as e:
    print "Exception when calling IntegrationsApi->get_integration_health: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The integration code for which to retrieve the information from | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration_page_components**
> get_integration_page_components(integration_name)

Get page components for a given integration

Get all page components for an integration.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.IntegrationsApi()
integration_name = 'integration_name_example' # str | The integration for which to retrieve HTML page components.

try: 
    # Get page components for a given integration
    api_instance.get_integration_page_components(integration_name)
except ApiException as e:
    print "Exception when calling IntegrationsApi->get_integration_page_components: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_name** | **str**| The integration for which to retrieve HTML page components. | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_users_integrated_lists**
> str sync_users_integrated_lists(integration_id=integration_id)

Synchronize your integration list or lists.

Synchronize your integration contact list with the service you are integrated with. If no integration code is provided, all integrations will be synchronized.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.IntegrationsApi()
integration_id = 'integration_id_example' # str | The integration to sync lists for. All integrations will sync if nothing is provided. (optional)

try: 
    # Synchronize your integration list or lists.
    api_response = api_instance.sync_users_integrated_lists(integration_id=integration_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling IntegrationsApi->sync_users_integrated_lists: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integration_id** | **str**| The integration to sync lists for. All integrations will sync if nothing is provided. | [optional] 

### Return type

**str**

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

