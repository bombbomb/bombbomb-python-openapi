# bombbomb.UtilitiesApi

All URIs are relative to *https://api.bombbomb.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_o_auth_client**](UtilitiesApi.md#create_o_auth_client) | **POST** /oauthclient | Create an OAuth Client
[**delete_o_auth_client**](UtilitiesApi.md#delete_o_auth_client) | **DELETE** /oauthclient/{id} | Delete an OAuth Client
[**get_o_auth_clients**](UtilitiesApi.md#get_o_auth_clients) | **GET** /oauthclient | Lists OAuth Clients
[**get_spec**](UtilitiesApi.md#get_spec) | **GET** /spec | Describes this api


# **create_o_auth_client**
> OAuthClient create_o_auth_client(name, redirect_uri)

Create an OAuth Client

Creates an OAuth Client managed by the user

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
api_instance = bombbomb.UtilitiesApi(bombbomb.ApiClient(configuration))
name = 'name_example' # str | The name of the OAuth client. e.g. MyCrm DEV, or MyCrm PROD
redirect_uri = 'redirect_uri_example' # str | The URI to direct the client to after logging in.

try:
    # Create an OAuth Client
    api_response = api_instance.create_o_auth_client(name, redirect_uri)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilitiesApi->create_o_auth_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the OAuth client. e.g. MyCrm DEV, or MyCrm PROD | 
 **redirect_uri** | **str**| The URI to direct the client to after logging in. | 

### Return type

[**OAuthClient**](OAuthClient.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_o_auth_client**
> delete_o_auth_client(id)

Delete an OAuth Client

Deletes an OAuth Client managed by the user

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
api_instance = bombbomb.UtilitiesApi(bombbomb.ApiClient(configuration))
id = 'id_example' # str | The id of the OAuth Client

try:
    # Delete an OAuth Client
    api_instance.delete_o_auth_client(id)
except ApiException as e:
    print("Exception when calling UtilitiesApi->delete_o_auth_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the OAuth Client | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_o_auth_clients**
> list[OAuthClient] get_o_auth_clients()

Lists OAuth Clients

Enumerates OAuth Clients managed by the user

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
api_instance = bombbomb.UtilitiesApi(bombbomb.ApiClient(configuration))

try:
    # Lists OAuth Clients
    api_response = api_instance.get_o_auth_clients()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilitiesApi->get_o_auth_clients: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[OAuthClient]**](OAuthClient.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spec**
> get_spec()

Describes this api

Describes methods available through the API.

### Example
```python
from __future__ import print_function
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bombbomb.UtilitiesApi()

try:
    # Describes this api
    api_instance.get_spec()
except ApiException as e:
    print("Exception when calling UtilitiesApi->get_spec: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

