# bombbomb.TeamsApi

All URIs are relative to *https://api.bombbomb.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_team_member**](TeamsApi.md#add_team_member) | **POST** /team/{teamId}/member | Add Member to Team
[**cancel_jericho_send**](TeamsApi.md#cancel_jericho_send) | **DELETE** /team/{teamId}/jericho/{jerichoId} | Cancel a Jericho Send
[**create_subteam**](TeamsApi.md#create_subteam) | **POST** /team/{teamId}/subteam | Add a Subteam
[**delete_subteam**](TeamsApi.md#delete_subteam) | **DELETE** /team/{teamId}/subteam | Delete Subteam
[**get_client_group_assets**](TeamsApi.md#get_client_group_assets) | **GET** /team/assets/ | Lists team assets
[**get_jericho_sends**](TeamsApi.md#get_jericho_sends) | **GET** /team/{teamId}/jericho | List Jericho Sends
[**get_jericho_stats**](TeamsApi.md#get_jericho_stats) | **GET** /team/{teamId}/jericho/{jerichoId}/performance | Gets Jericho performance statistics
[**get_subteams**](TeamsApi.md#get_subteams) | **GET** /team/{teamId}/subteam | List Subteams
[**queue_jericho_send**](TeamsApi.md#queue_jericho_send) | **POST** /team/{teamId}/jericho | Creates a Jericho send.
[**remove_member_from_team**](TeamsApi.md#remove_member_from_team) | **DELETE** /team/{teamId}/member/{userId} | Remove Member from Team
[**update_team**](TeamsApi.md#update_team) | **POST** /team/{teamId} | Update a team


# **add_team_member**
> str add_team_member(team_id, user_id=user_id, user_email=user_email, admin=admin)

Add Member to Team

Adds a member to a team.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.TeamsApi()
team_id = 'team_id_example' # str | The team id
user_id = 'user_id_example' # str | The user id of the member being added to the team. (optional)
user_email = 'user_email_example' # str | The email of the member being added to the team. (optional)
admin = true # bool | Set if the user is an admin of this team. (optional)

try: 
    # Add Member to Team
    api_response = api_instance.add_team_member(team_id, user_id=user_id, user_email=user_email, admin=admin)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TeamsApi->add_team_member: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The team id | 
 **user_id** | **str**| The user id of the member being added to the team. | [optional] 
 **user_email** | **str**| The email of the member being added to the team. | [optional] 
 **admin** | **bool**| Set if the user is an admin of this team. | [optional] 

### Return type

**str**

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_jericho_send**
> cancel_jericho_send(jericho_id)

Cancel a Jericho Send

Cancels a scheduled Jericho send from being sent.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.TeamsApi()
jericho_id = 'jericho_id_example' # str | ID of the Jericho Job to cancel

try: 
    # Cancel a Jericho Send
    api_instance.cancel_jericho_send(jericho_id)
except ApiException as e:
    print "Exception when calling TeamsApi->cancel_jericho_send: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jericho_id** | **str**| ID of the Jericho Job to cancel | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subteam**
> TeamPublicRepresentation create_subteam(team_id, name)

Add a Subteam

Adds a subteam to a parent team

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.TeamsApi()
team_id = 'team_id_example' # str | The team id
name = 'name_example' # str | The subteam's name.

try: 
    # Add a Subteam
    api_response = api_instance.create_subteam(team_id, name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TeamsApi->create_subteam: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The team id | 
 **name** | **str**| The subteam&#39;s name. | 

### Return type

[**TeamPublicRepresentation**](TeamPublicRepresentation.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subteam**
> str delete_subteam(team_id, subteam_id)

Delete Subteam

Deletes a subteam

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.TeamsApi()
team_id = 'team_id_example' # str | The team id
subteam_id = 'subteam_id_example' # str | The subteam you wish to delete.

try: 
    # Delete Subteam
    api_response = api_instance.delete_subteam(team_id, subteam_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TeamsApi->delete_subteam: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The team id | 
 **subteam_id** | **str**| The subteam you wish to delete. | 

### Return type

**str**

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_group_assets**
> InlineResponse200 get_client_group_assets(asset_type, team_id=team_id, auto_tag_name=auto_tag_name, page_size=page_size, page=page, search=search)

Lists team assets

Returns a collection of assets

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.TeamsApi()
asset_type = 'asset_type_example' # str | The type of assets.
team_id = 'team_id_example' # str | The team containing the assets. (optional)
auto_tag_name = 'auto_tag_name_example' # str | The auto tag name containing the assets. (optional)
page_size = 'page_size_example' # str | The number of items to retrieve in a single db query. (optional)
page = 'page_example' # str | Zero-based index of the page of data to retrieve from the db. (optional)
search = 'search_example' # str | Search words. (optional)

try: 
    # Lists team assets
    api_response = api_instance.get_client_group_assets(asset_type, team_id=team_id, auto_tag_name=auto_tag_name, page_size=page_size, page=page, search=search)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TeamsApi->get_client_group_assets: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type** | **str**| The type of assets. | 
 **team_id** | **str**| The team containing the assets. | [optional] 
 **auto_tag_name** | **str**| The auto tag name containing the assets. | [optional] 
 **page_size** | **str**| The number of items to retrieve in a single db query. | [optional] 
 **page** | **str**| Zero-based index of the page of data to retrieve from the db. | [optional] 
 **search** | **str**| Search words. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jericho_sends**
> list[JerichoConfiguration] get_jericho_sends(team_id)

List Jericho Sends

Lists Jericho sends, both pending and sent.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.TeamsApi()
team_id = 'team_id_example' # str | The team whose Jericho sends you wish to see.

try: 
    # List Jericho Sends
    api_response = api_instance.get_jericho_sends(team_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TeamsApi->get_jericho_sends: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The team whose Jericho sends you wish to see. | 

### Return type

[**list[JerichoConfiguration]**](JerichoConfiguration.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jericho_stats**
> JerichoPerformance get_jericho_stats(jericho_id, team_id)

Gets Jericho performance statistics

Returns an aggregate view of the performance of a Jericho send

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.TeamsApi()
jericho_id = 'jericho_id_example' # str | ID of the Jericho job
team_id = 'team_id_example' # str | ID of team through which Jericho was sent

try: 
    # Gets Jericho performance statistics
    api_response = api_instance.get_jericho_stats(jericho_id, team_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TeamsApi->get_jericho_stats: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jericho_id** | **str**| ID of the Jericho job | 
 **team_id** | **str**| ID of team through which Jericho was sent | 

### Return type

[**JerichoPerformance**](JerichoPerformance.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subteams**
> list[TeamPublicRepresentation] get_subteams(team_id)

List Subteams

Returns a collection of subteams for a parent team

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.TeamsApi()
team_id = 'team_id_example' # str | The team id

try: 
    # List Subteams
    api_response = api_instance.get_subteams(team_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TeamsApi->get_subteams: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The team id | 

### Return type

[**list[TeamPublicRepresentation]**](TeamPublicRepresentation.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **queue_jericho_send**
> JerichoConfiguration queue_jericho_send(config, team_id)

Creates a Jericho send.

Sends email content on behalf of members of a client group. There are two forms this send can take:         Static Email, and Video Prompt. Static emails require only an emailId.         Video Prompts build emails dynamically and require most of the other fields.         You must be an administrator of a Team Account to use this method.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.TeamsApi()
config = bombbomb.JerichoConfiguration() # JerichoConfiguration | JSON representing a Jericho configuration
team_id = 'team_id_example' # str | The ID of the team.

try: 
    # Creates a Jericho send.
    api_response = api_instance.queue_jericho_send(config, team_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TeamsApi->queue_jericho_send: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config** | [**JerichoConfiguration**](JerichoConfiguration.md)| JSON representing a Jericho configuration | 
 **team_id** | **str**| The ID of the team. | 

### Return type

[**JerichoConfiguration**](JerichoConfiguration.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_member_from_team**
> str remove_member_from_team(team_id, user_id)

Remove Member from Team

Removes a member from a team.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.TeamsApi()
team_id = 'team_id_example' # str | The team id
user_id = 'user_id_example' # str | The user id of the member being removed.

try: 
    # Remove Member from Team
    api_response = api_instance.remove_member_from_team(team_id, user_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TeamsApi->remove_member_from_team: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The team id | 
 **user_id** | **str**| The user id of the member being removed. | 

### Return type

**str**

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team**
> TeamPublicRepresentation update_team(team_id, name=name)

Update a team

Update fields on a team

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.TeamsApi()
team_id = 'team_id_example' # str | The team id
name = 'name_example' # str | The name of the team (optional)

try: 
    # Update a team
    api_response = api_instance.update_team(team_id, name=name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TeamsApi->update_team: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The team id | 
 **name** | **str**| The name of the team | [optional] 

### Return type

[**TeamPublicRepresentation**](TeamPublicRepresentation.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

