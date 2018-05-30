# bombbomb.SocialsApi

All URIs are relative to *https://api.bombbomb.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_facebook_pages**](SocialsApi.md#get_facebook_pages) | **GET** /socials/facebook/pages | Gets facebook pages
[**get_social_article_properties**](SocialsApi.md#get_social_article_properties) | **GET** /socials/properties | Gets the social email properties
[**get_social_authorizations**](SocialsApi.md#get_social_authorizations) | **GET** /socials/authorizations | Get authorizations for all social integration
[**get_social_profile_properties**](SocialsApi.md#get_social_profile_properties) | **GET** /socials/profile | Gets the profile properties
[**get_social_stats**](SocialsApi.md#get_social_stats) | **GET** /socials/{promptId}/stats | Get social stats for a prompt
[**post_social_content**](SocialsApi.md#post_social_content) | **POST** /socials/content | Creates social content
[**retry_social_send**](SocialsApi.md#retry_social_send) | **POST** /socials/send/retry | Sends social content
[**send_social**](SocialsApi.md#send_social) | **POST** /socials/send | Sends social content
[**update_client_group_send_mechanism**](SocialsApi.md#update_client_group_send_mechanism) | **PUT** /socials/client/sendMechanism | Gets the auto shares from the client group assoc id
[**update_client_groups_send_mechanism**](SocialsApi.md#update_client_groups_send_mechanism) | **PUT** /socials/client/sendMechanisms | Toggles the prompt campaigns in a users account
[**update_facebook_pages**](SocialsApi.md#update_facebook_pages) | **PUT** /socials/facebook/pages | Updates facebook page Ids
[**update_social_content**](SocialsApi.md#update_social_content) | **PUT** /socials/content | Updates social content


# **get_facebook_pages**
> get_facebook_pages()

Gets facebook pages

Gets facebook pages by client id

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.SocialsApi()

try: 
    # Gets facebook pages
    api_instance.get_facebook_pages()
except ApiException as e:
    print "Exception when calling SocialsApi->get_facebook_pages: %s\n" % e
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

# **get_social_article_properties**
> get_social_article_properties(email_id, social_content_id)

Gets the social email properties

Gets the social email properties

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.SocialsApi()
email_id = 'email_id_example' # str | This is the email Id for the email url
social_content_id = 'social_content_id_example' # str | This is the social content Id

try: 
    # Gets the social email properties
    api_instance.get_social_article_properties(email_id, social_content_id)
except ApiException as e:
    print "Exception when calling SocialsApi->get_social_article_properties: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | **str**| This is the email Id for the email url | 
 **social_content_id** | **str**| This is the social content Id | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_social_authorizations**
> get_social_authorizations(client_group_id=client_group_id)

Get authorizations for all social integration

Get authorizations and autoshares for all social integration and has redirect for user to login

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.SocialsApi()
client_group_id = 'client_group_id_example' # str | ID of the client group association (optional)

try: 
    # Get authorizations for all social integration
    api_instance.get_social_authorizations(client_group_id=client_group_id)
except ApiException as e:
    print "Exception when calling SocialsApi->get_social_authorizations: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_group_id** | **str**| ID of the client group association | [optional] 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_social_profile_properties**
> get_social_profile_properties(social_type)

Gets the profile properties

Gets the social profile properties

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.SocialsApi()
social_type = 'social_type_example' # str | The social type

try: 
    # Gets the profile properties
    api_instance.get_social_profile_properties(social_type)
except ApiException as e:
    print "Exception when calling SocialsApi->get_social_profile_properties: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_type** | **str**| The social type | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_social_stats**
> get_social_stats(prompt_id)

Get social stats for a prompt

Get social stats for a prompt by id

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.SocialsApi()
prompt_id = 'prompt_id_example' # str | ID of the prompt

try: 
    # Get social stats for a prompt
    api_instance.get_social_stats(prompt_id)
except ApiException as e:
    print "Exception when calling SocialsApi->get_social_stats: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_id** | **str**| ID of the prompt | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_social_content**
> post_social_content(email_id)

Creates social content

Creates social content for an email

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.SocialsApi()
email_id = 'email_id_example' # str | The email's id

try: 
    # Creates social content
    api_instance.post_social_content(email_id)
except ApiException as e:
    print "Exception when calling SocialsApi->post_social_content: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | **str**| The email&#39;s id | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_social_send**
> retry_social_send(prompt_id)

Sends social content

Sends social content that failed for a user via their associated prompt

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.SocialsApi()
prompt_id = 'prompt_id_example' # str | The prompt id

try: 
    # Sends social content
    api_instance.retry_social_send(prompt_id)
except ApiException as e:
    print "Exception when calling SocialsApi->retry_social_send: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_id** | **str**| The prompt id | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_social**
> send_social(prompt_id, social_type)

Sends social content

Sends social content for a user via their associated prompt

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.SocialsApi()
prompt_id = 'prompt_id_example' # str | The prompt id
social_type = 'social_type_example' # str | The destination for social content

try: 
    # Sends social content
    api_instance.send_social(prompt_id, social_type)
except ApiException as e:
    print "Exception when calling SocialsApi->send_social: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt_id** | **str**| The prompt id | 
 **social_type** | **str**| The destination for social content | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_group_send_mechanism**
> update_client_group_send_mechanism(send_mechanism, client_group_id, enabled=enabled)

Gets the auto shares from the client group assoc id

Gets the auto shares from the client group assoc id

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.SocialsApi()
send_mechanism = 'send_mechanism_example' # str | The send mechanism for the prompt
client_group_id = 'client_group_id_example' # str | ID of the client group association
enabled = 'enabled_example' # str | Is the send mechanism enabled? (optional)

try: 
    # Gets the auto shares from the client group assoc id
    api_instance.update_client_group_send_mechanism(send_mechanism, client_group_id, enabled=enabled)
except ApiException as e:
    print "Exception when calling SocialsApi->update_client_group_send_mechanism: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_mechanism** | **str**| The send mechanism for the prompt | 
 **client_group_id** | **str**| ID of the client group association | 
 **enabled** | **str**| Is the send mechanism enabled? | [optional] 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_groups_send_mechanism**
> update_client_groups_send_mechanism(send_mechanism, enabled)

Toggles the prompt campaigns in a users account

Toggles the prompt campaigns in a users account for a social integrations on or off

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.SocialsApi()
send_mechanism = 'send_mechanism_example' # str | The send mechanism for the prompt
enabled = 'enabled_example' # str | Is the send mechanism enabled?

try: 
    # Toggles the prompt campaigns in a users account
    api_instance.update_client_groups_send_mechanism(send_mechanism, enabled)
except ApiException as e:
    print "Exception when calling SocialsApi->update_client_groups_send_mechanism: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_mechanism** | **str**| The send mechanism for the prompt | 
 **enabled** | **str**| Is the send mechanism enabled? | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_facebook_pages**
> update_facebook_pages(page_ids)

Updates facebook page Ids

Updates facebook page Ids to be sent to for prompts

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.SocialsApi()
page_ids = 'page_ids_example' # str | Page Ids for the prompt

try: 
    # Updates facebook page Ids
    api_instance.update_facebook_pages(page_ids)
except ApiException as e:
    print "Exception when calling SocialsApi->update_facebook_pages: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_ids** | **str**| Page Ids for the prompt | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_social_content**
> update_social_content(social_id, title=title, description=description, picture_url=picture_url, suggested_message=suggested_message)

Updates social content

Updates social content for an email

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.SocialsApi()
social_id = 'social_id_example' # str | The social id
title = 'title_example' # str | The title for the article (optional)
description = 'description_example' # str | The article description (optional)
picture_url = 'picture_url_example' # str | The article picture url (optional)
suggested_message = 'suggested_message_example' # str | The suggested message to use (optional)

try: 
    # Updates social content
    api_instance.update_social_content(social_id, title=title, description=description, picture_url=picture_url, suggested_message=suggested_message)
except ApiException as e:
    print "Exception when calling SocialsApi->update_social_content: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **social_id** | **str**| The social id | 
 **title** | **str**| The title for the article | [optional] 
 **description** | **str**| The article description | [optional] 
 **picture_url** | **str**| The article picture url | [optional] 
 **suggested_message** | **str**| The suggested message to use | [optional] 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

