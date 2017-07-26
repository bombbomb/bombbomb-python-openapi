# bombbomb.ListsApi

All URIs are relative to *https://api.bombbomb.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_list**](ListsApi.md#clear_list) | **PUT** /lists/{listId}/clear | Clear Contacts from List
[**copy_list_contacts**](ListsApi.md#copy_list_contacts) | **POST** /lists/{listId}/copy | Copy All Contacts from a List
[**suppress_all_in_list**](ListsApi.md#suppress_all_in_list) | **PUT** /lists/{listId}/suppress | Suppress All Contacts from List


# **clear_list**
> clear_list(list_id)

Clear Contacts from List

Clears all contacts from a list.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.ListsApi()
list_id = 'list_id_example' # str | The list to be cleared.

try: 
    # Clear Contacts from List
    api_instance.clear_list(list_id)
except ApiException as e:
    print "Exception when calling ListsApi->clear_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**| The list to be cleared. | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_list_contacts**
> copy_list_contacts(from_list_id, list_id)

Copy All Contacts from a List

Copy all contacts from a list.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.ListsApi()
from_list_id = 'from_list_id_example' # str | The list to be cleared.
list_id = 'list_id_example' # str | The list to be cleared.

try: 
    # Copy All Contacts from a List
    api_instance.copy_list_contacts(from_list_id, list_id)
except ApiException as e:
    print "Exception when calling ListsApi->copy_list_contacts: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_list_id** | **str**| The list to be cleared. | 
 **list_id** | **str**| The list to be cleared. | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suppress_all_in_list**
> suppress_all_in_list(list_id)

Suppress All Contacts from List

Suppresses all contacts in a list.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.ListsApi()
list_id = 'list_id_example' # str | The list to be cleared.

try: 
    # Suppress All Contacts from List
    api_instance.suppress_all_in_list(list_id)
except ApiException as e:
    print "Exception when calling ListsApi->suppress_all_in_list: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**| The list to be cleared. | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

