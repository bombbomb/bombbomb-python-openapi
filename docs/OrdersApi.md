# bombbomb.OrdersApi

All URIs are relative to *https://api.bombbomb.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**template_asset_delete**](OrdersApi.md#template_asset_delete) | **DELETE** /orders/templates/images | Deletes image from user s3 store


# **template_asset_delete**
> template_asset_delete(file_name)

Deletes image from user s3 store

Deletes image from user s3 store

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
api_instance = bombbomb.OrdersApi(bombbomb.ApiClient(configuration))
file_name = 'file_name_example' # str | Filename for deletion

try:
    # Deletes image from user s3 store
    api_instance.template_asset_delete(file_name)
except ApiException as e:
    print("Exception when calling OrdersApi->template_asset_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_name** | **str**| Filename for deletion | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

