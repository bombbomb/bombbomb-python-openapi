# bombbomb.FilesApi

All URIs are relative to *https://api.bombbomb.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**doc_host_delete**](FilesApi.md#doc_host_delete) | **DELETE** /files | Deletes users file


# **doc_host_delete**
> doc_host_delete(doc_id)

Deletes users file

Deletes the file from the users s3 store

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.FilesApi()
doc_id = 'doc_id_example' # str | Id of document

try: 
    # Deletes users file
    api_instance.doc_host_delete(doc_id)
except ApiException as e:
    print "Exception when calling FilesApi->doc_host_delete: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_id** | **str**| Id of document | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

