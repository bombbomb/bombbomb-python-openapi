# bombbomb.FormsApi

All URIs are relative to *https://api.bombbomb.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_form_tracking_as_csv**](FormsApi.md#get_form_tracking_as_csv) | **GET** /forms/{id}/tracking/export | Get csv


# **get_form_tracking_as_csv**
> get_form_tracking_as_csv(id)

Get csv

Get form tracking as csv

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
api_instance = bombbomb.FormsApi(bombbomb.ApiClient(configuration))
id = 'id_example' # str | Id of the form

try:
    # Get csv
    api_instance.get_form_tracking_as_csv(id)
except ApiException as e:
    print("Exception when calling FormsApi->get_form_tracking_as_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id of the form | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

