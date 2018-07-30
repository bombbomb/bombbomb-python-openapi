# bombbomb.AutomationsApi

All URIs are relative to *https://api.bombbomb.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_drip_drop_stats**](AutomationsApi.md#get_drip_drop_stats) | **GET** /automation/{dripId}/dripdrop/{dripDropId}/stats | Get Automation Email Stats
[**get_drip_stats**](AutomationsApi.md#get_drip_stats) | **GET** /automation/{id}/stats | Get Automation Stats
[**get_scheduling_status**](AutomationsApi.md#get_scheduling_status) | **GET** /automation/{id}/scheduling/status | Get the number of pending scheduling calculations


# **get_drip_drop_stats**
> get_drip_drop_stats(drip_id, drip_drop_id)

Get Automation Email Stats

Get Automation Email Stats

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
api_instance = bombbomb.AutomationsApi(bombbomb.ApiClient(configuration))
drip_id = 'drip_id_example' # str | The id of the drip
drip_drop_id = 'drip_drop_id_example' # str | The id of the drip drop

try:
    # Get Automation Email Stats
    api_instance.get_drip_drop_stats(drip_id, drip_drop_id)
except ApiException as e:
    print("Exception when calling AutomationsApi->get_drip_drop_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **drip_id** | **str**| The id of the drip | 
 **drip_drop_id** | **str**| The id of the drip drop | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_drip_stats**
> get_drip_stats(id)

Get Automation Stats

Get Automation Stats

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
api_instance = bombbomb.AutomationsApi(bombbomb.ApiClient(configuration))
id = 'id_example' # str | The id of the automation

try:
    # Get Automation Stats
    api_instance.get_drip_stats(id)
except ApiException as e:
    print("Exception when calling AutomationsApi->get_drip_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the automation | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduling_status**
> get_scheduling_status(id)

Get the number of pending scheduling calculations

Get the number of pending scheduling calculations

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
api_instance = bombbomb.AutomationsApi(bombbomb.ApiClient(configuration))
id = 'id_example' # str | The id of the automation

try:
    # Get the number of pending scheduling calculations
    api_instance.get_scheduling_status(id)
except ApiException as e:
    print("Exception when calling AutomationsApi->get_scheduling_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the automation | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

