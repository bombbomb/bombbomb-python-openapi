# bombbomb.CurriculumApi

All URIs are relative to *https://api.bombbomb.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_curricula**](CurriculumApi.md#get_curricula) | **GET** /curricula/ | Get Curricula
[**get_user_curriculum_with_progress**](CurriculumApi.md#get_user_curriculum_with_progress) | **GET** /curriculum/getForUserWithProgress | Get Detailed For User


# **get_curricula**
> list[Curriculum] get_curricula(include_progress=include_progress)

Get Curricula

Get Curricula, optionally with progress included.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.CurriculumApi()
include_progress = true # bool | Whether to return progress with the curriculum. (optional)

try: 
    # Get Curricula
    api_response = api_instance.get_curricula(include_progress=include_progress)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CurriculumApi->get_curricula: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_progress** | **bool**| Whether to return progress with the curriculum. | [optional] 

### Return type

[**list[Curriculum]**](Curriculum.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_curriculum_with_progress**
> list[CurriculumWithProgress] get_user_curriculum_with_progress()

Get Detailed For User

Get all curricula for user including progress for each curriculum.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.CurriculumApi()

try: 
    # Get Detailed For User
    api_response = api_instance.get_user_curriculum_with_progress()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CurriculumApi->get_user_curriculum_with_progress: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CurriculumWithProgress]**](CurriculumWithProgress.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

