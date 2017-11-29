# bombbomb.FilesApi

All URIs are relative to *https://api.bombbomb.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**doc_host_delete**](FilesApi.md#doc_host_delete) | **DELETE** /files/{docId} | Delete file
[**doc_host_get**](FilesApi.md#doc_host_get) | **GET** /files/{docId} | Get file
[**doc_host_list**](FilesApi.md#doc_host_list) | **GET** /files | List all files
[**doc_host_upload_v2**](FilesApi.md#doc_host_upload_v2) | **POST** /files | Upload a file
[**get_hosted_images_paged**](FilesApi.md#get_hosted_images_paged) | **GET** /files/images/paged | Get paged hosted images


# **doc_host_delete**
> doc_host_delete(doc_id)

Delete file

Deletes a users file

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
    # Delete file
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

# **doc_host_get**
> HostedDoc doc_host_get(doc_id)

Get file

Get a single file by id

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
    # Get file
    api_response = api_instance.doc_host_get(doc_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FilesApi->doc_host_get: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_id** | **str**| Id of document | 

### Return type

[**HostedDoc**](HostedDoc.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **doc_host_list**
> list[HostedDoc] doc_host_list()

List all files

List all uploaded user files

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

try: 
    # List all files
    api_response = api_instance.doc_host_list()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FilesApi->doc_host_list: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[HostedDoc]**](HostedDoc.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **doc_host_upload_v2**
> list[HostedDoc] doc_host_upload_v2(file)

Upload a file

Upload a new file

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
file = 'file_example' # str | The file being uploaded

try: 
    # Upload a file
    api_response = api_instance.doc_host_upload_v2(file)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling FilesApi->doc_host_upload_v2: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**| The file being uploaded | 

### Return type

[**list[HostedDoc]**](HostedDoc.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hosted_images_paged**
> get_hosted_images_paged(page_size, page, search=search)

Get paged hosted images

Get a specific page of uploaded images available to the user.

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
page_size = 'page_size_example' # str | The number of items to retrieve in a single db query.
page = 'page_example' # str | Zero-based index of the page of data to retrieve from the db.
search = 'search_example' # str | Filter results with names that match the search term. (optional)

try: 
    # Get paged hosted images
    api_instance.get_hosted_images_paged(page_size, page, search=search)
except ApiException as e:
    print "Exception when calling FilesApi->get_hosted_images_paged: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **str**| The number of items to retrieve in a single db query. | 
 **page** | **str**| Zero-based index of the page of data to retrieve from the db. | 
 **search** | **str**| Filter results with names that match the search term. | [optional] 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

