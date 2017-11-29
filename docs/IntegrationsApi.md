# bombbomb.IntegrationsApi

All URIs are relative to *https://api.bombbomb.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sync_users_integrated_lists**](IntegrationsApi.md#sync_users_integrated_lists) | **GET** /integrations/sync | Synchronize your integration list or lists.


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

