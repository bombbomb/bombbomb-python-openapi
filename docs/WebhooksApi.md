# bombbomb.WebhooksApi

All URIs are relative to *https://api.bombbomb.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_web_hook**](WebhooksApi.md#add_web_hook) | **POST** /webhook | Add Webhook
[**delete_web_hook**](WebhooksApi.md#delete_web_hook) | **DELETE** /webhook/{hookId} | Deletes Webhook
[**get_web_hooks**](WebhooksApi.md#get_web_hooks) | **GET** /webhook/ | Lists Webhooks
[**list_web_hook_events**](WebhooksApi.md#list_web_hook_events) | **GET** /webhook/events | Describe WebHook Events
[**send_webhook_example**](WebhooksApi.md#send_webhook_example) | **POST** /webhook/test | Sends test Webhook


# **add_web_hook**
> BBWebHook add_web_hook(hook_url)

Add Webhook

Idempotently adds a Webhook url

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
api_instance = bombbomb.WebhooksApi(bombbomb.ApiClient(configuration))
hook_url = 'hook_url_example' # str | The Url of your listener

try:
    # Add Webhook
    api_response = api_instance.add_web_hook(hook_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->add_web_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hook_url** | **str**| The Url of your listener | 

### Return type

[**BBWebHook**](BBWebHook.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_web_hook**
> str delete_web_hook(hook_id)

Deletes Webhook

Deletes a Webhook

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
api_instance = bombbomb.WebhooksApi(bombbomb.ApiClient(configuration))
hook_id = 'hook_id_example' # str | The id of the webhook to delete

try:
    # Deletes Webhook
    api_response = api_instance.delete_web_hook(hook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->delete_web_hook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hook_id** | **str**| The id of the webhook to delete | 

### Return type

**str**

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_hooks**
> list[BBWebHook] get_web_hooks()

Lists Webhooks

Lists all registered Webhooks

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
api_instance = bombbomb.WebhooksApi(bombbomb.ApiClient(configuration))

try:
    # Lists Webhooks
    api_response = api_instance.get_web_hooks()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebhooksApi->get_web_hooks: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BBWebHook]**](BBWebHook.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_web_hook_events**
> list_web_hook_events()

Describe WebHook Events

Returns example Webhook events for each kind of possible event.

### Example
```python
from __future__ import print_function
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bombbomb.WebhooksApi()

try:
    # Describe WebHook Events
    api_instance.list_web_hook_events()
except ApiException as e:
    print("Exception when calling WebhooksApi->list_web_hook_events: %s\n" % e)
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

# **send_webhook_example**
> send_webhook_example()

Sends test Webhook

Triggers a test webhook to be sent to your endpoints.

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
api_instance = bombbomb.WebhooksApi(bombbomb.ApiClient(configuration))

try:
    # Sends test Webhook
    api_instance.send_webhook_example()
except ApiException as e:
    print("Exception when calling WebhooksApi->send_webhook_example: %s\n" % e)
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

