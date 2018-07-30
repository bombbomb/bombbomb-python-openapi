# bombbomb.UsersApi

All URIs are relative to *https://api.bombbomb.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client_contact_information**](UsersApi.md#get_client_contact_information) | **GET** /clients/contact/information | Get client contact information.
[**get_user_profile_info**](UsersApi.md#get_user_profile_info) | **GET** /users/profile/information | Get user profile information.


# **get_client_contact_information**
> get_client_contact_information()

Get client contact information.

Get the client contact information of the user's account.

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
api_instance = bombbomb.UsersApi(bombbomb.ApiClient(configuration))

try:
    # Get client contact information.
    api_instance.get_client_contact_information()
except ApiException as e:
    print("Exception when calling UsersApi->get_client_contact_information: %s\n" % e)
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

# **get_user_profile_info**
> get_user_profile_info()

Get user profile information.

Get the users profile information.

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
api_instance = bombbomb.UsersApi(bombbomb.ApiClient(configuration))

try:
    # Get user profile information.
    api_instance.get_user_profile_info()
except ApiException as e:
    print("Exception when calling UsersApi->get_user_profile_info: %s\n" % e)
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

