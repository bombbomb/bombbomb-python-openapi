# bombbomb.ContactsApi

All URIs are relative to *https://api.bombbomb.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_contacts**](ContactsApi.md#delete_contacts) | **PUT** /contacts/delete | Delete Contacts


# **delete_contacts**
> delete_contacts(list_id)

Delete Contacts

Delete contacts

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.ContactsApi()
list_id = 'list_id_example' # str | The list of contacts to be deleted.

try: 
    # Delete Contacts
    api_instance.delete_contacts(list_id)
except ApiException as e:
    print "Exception when calling ContactsApi->delete_contacts: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**| The list of contacts to be deleted. | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

