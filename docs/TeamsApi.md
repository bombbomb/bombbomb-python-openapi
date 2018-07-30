# bombbomb.TeamsApi

All URIs are relative to *https://api.bombbomb.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_team_member**](TeamsApi.md#add_team_member) | **POST** /team/{teamId}/member | Add Member to Team
[**add_users**](TeamsApi.md#add_users) | **POST** /team/{teamId}/members | Add users to group.
[**add_users_from_csv**](TeamsApi.md#add_users_from_csv) | **POST** /team/{teamId}/members/csv | Add members to group from CSV
[**cancel_jericho_send**](TeamsApi.md#cancel_jericho_send) | **DELETE** /team/{teamId}/jericho/{jerichoId} | Cancel a Jericho Send
[**create_subteam**](TeamsApi.md#create_subteam) | **POST** /team/{teamId}/subteam | Add a Subteam
[**delete_subteam**](TeamsApi.md#delete_subteam) | **DELETE** /team/{teamId}/subteam | Delete Subteam
[**get_all_client_group_associations**](TeamsApi.md#get_all_client_group_associations) | **GET** /team/associations/ | Lists team associations
[**get_client_group_assets**](TeamsApi.md#get_client_group_assets) | **GET** /team/assets/ | Lists team assets
[**get_client_group_statistics**](TeamsApi.md#get_client_group_statistics) | **GET** /team/{teamId}/stats | Get Team statistics
[**get_jericho_sends**](TeamsApi.md#get_jericho_sends) | **GET** /team/{teamId}/jericho | List Jericho Sends
[**get_jericho_stats**](TeamsApi.md#get_jericho_stats) | **GET** /team/{teamId}/jericho/{jerichoId}/performance | Gets Jericho performance statistics
[**get_paged_client_group_members**](TeamsApi.md#get_paged_client_group_members) | **GET** /team/{teamId}/members | List Team Members
[**get_prompt_monthly_stats**](TeamsApi.md#get_prompt_monthly_stats) | **GET** /team/{month}/{year}/monthStats | Jericho Monthly Stats
[**get_prompt_overview**](TeamsApi.md#get_prompt_overview) | **GET** /team/promptOverview | Get Prompt Overview
[**get_subteams**](TeamsApi.md#get_subteams) | **GET** /team/{teamId}/subteam | List Subteams
[**get_team_prompt_aggregate_stats**](TeamsApi.md#get_team_prompt_aggregate_stats) | **GET** /team/{clientGroupId}/campaign/stats | Get aggregate stats for campaigns
[**get_team_prompt_campaigns**](TeamsApi.md#get_team_prompt_campaigns) | **GET** /team/{clientGroupId}/campaign | Get campaigns for team
[**invite_to_social_prompt_team**](TeamsApi.md#invite_to_social_prompt_team) | **POST** /teams/prompt/invite | Invite a list to join the admin&#39;s social prompt team
[**queue_jericho_send**](TeamsApi.md#queue_jericho_send) | **POST** /team/{teamId}/jericho | Creates a Jericho send.
[**remove_member_from_team**](TeamsApi.md#remove_member_from_team) | **DELETE** /team/{teamId}/member/{userId} | Remove Member from Team
[**resend_team_member_invitation**](TeamsApi.md#resend_team_member_invitation) | **POST** /team/{teamId}/{memberUserId}/rewelcome | Resend invite
[**update_jericho_prompt_send**](TeamsApi.md#update_jericho_prompt_send) | **PUT** /team/{teamId}/jericho/{jerichoId} | Updates the Jericho Prompt Settings
[**update_team**](TeamsApi.md#update_team) | **POST** /team/{teamId} | Update a team
[**update_team_member**](TeamsApi.md#update_team_member) | **PUT** /team/{teamId}/member | Update Member of Team


# **add_team_member**
> str add_team_member(team_id, admin=admin, subgroup_ids=subgroup_ids, user_email=user_email, user_id=user_id)

Add Member to Team

Adds a member to a team.

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
api_instance = bombbomb.TeamsApi(bombbomb.ApiClient(configuration))
team_id = 'team_id_example' # str | The team id
admin = true # bool | Set if the user is an admin of this team. (optional)
subgroup_ids = 'subgroup_ids_example' # str | Subgroup IDs to add user to (optional)
user_email = 'user_email_example' # str | The email of the member being added to the team. (optional)
user_id = 'user_id_example' # str | The user id of the member being added to the team. (optional)

try:
    # Add Member to Team
    api_response = api_instance.add_team_member(team_id, admin=admin, subgroup_ids=subgroup_ids, user_email=user_email, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->add_team_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The team id | 
 **admin** | **bool**| Set if the user is an admin of this team. | [optional] 
 **subgroup_ids** | **str**| Subgroup IDs to add user to | [optional] 
 **user_email** | **str**| The email of the member being added to the team. | [optional] 
 **user_id** | **str**| The user id of the member being added to the team. | [optional] 

### Return type

**str**

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_users**
> add_users(team_id, user_details, send_welcome_email=send_welcome_email, subgroup_ids=subgroup_ids)

Add users to group.

Add a new or existing user to group.

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
api_instance = bombbomb.TeamsApi(bombbomb.ApiClient(configuration))
team_id = 'team_id_example' # str | The team id
user_details = 'user_details_example' # str | Array of emails or objects containing details needed to create user
send_welcome_email = 'send_welcome_email_example' # str | Whether to send welcome email to new users (optional)
subgroup_ids = 'subgroup_ids_example' # str | Subgroup IDs to add user to (optional)

try:
    # Add users to group.
    api_instance.add_users(team_id, user_details, send_welcome_email=send_welcome_email, subgroup_ids=subgroup_ids)
except ApiException as e:
    print("Exception when calling TeamsApi->add_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The team id | 
 **user_details** | **str**| Array of emails or objects containing details needed to create user | 
 **send_welcome_email** | **str**| Whether to send welcome email to new users | [optional] 
 **subgroup_ids** | **str**| Subgroup IDs to add user to | [optional] 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_users_from_csv**
> add_users_from_csv(team_id, csv_import_id, map, send_welcome_email=send_welcome_email, subgroup_ids=subgroup_ids)

Add members to group from CSV

Imports members to a group from a given CSV ID.

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
api_instance = bombbomb.TeamsApi(bombbomb.ApiClient(configuration))
team_id = 'team_id_example' # str | The team id
csv_import_id = 'csv_import_id_example' # str | ID of the CSV to import
map = 'map_example' # str | Object to use when mapping import to AccountCreateDetails. Key is property name on details, value is CSV column number.
send_welcome_email = 'send_welcome_email_example' # str | Whether to send welcome email to new users (optional)
subgroup_ids = 'subgroup_ids_example' # str | Subgroup IDs to add user to (optional)

try:
    # Add members to group from CSV
    api_instance.add_users_from_csv(team_id, csv_import_id, map, send_welcome_email=send_welcome_email, subgroup_ids=subgroup_ids)
except ApiException as e:
    print("Exception when calling TeamsApi->add_users_from_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The team id | 
 **csv_import_id** | **str**| ID of the CSV to import | 
 **map** | **str**| Object to use when mapping import to AccountCreateDetails. Key is property name on details, value is CSV column number. | 
 **send_welcome_email** | **str**| Whether to send welcome email to new users | [optional] 
 **subgroup_ids** | **str**| Subgroup IDs to add user to | [optional] 

### Return type

void (empty response body)

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
from __future__ import print_function
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
configuration = bombbomb.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.TeamsApi(bombbomb.ApiClient(configuration))
jericho_id = 'jericho_id_example' # str | ID of the Jericho Job to cancel

try:
    # Cancel a Jericho Send
    api_instance.cancel_jericho_send(jericho_id)
except ApiException as e:
    print("Exception when calling TeamsApi->cancel_jericho_send: %s\n" % e)
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
from __future__ import print_function
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
configuration = bombbomb.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.TeamsApi(bombbomb.ApiClient(configuration))
team_id = 'team_id_example' # str | The team id
name = 'name_example' # str | The subteam's name.

try:
    # Add a Subteam
    api_response = api_instance.create_subteam(team_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->create_subteam: %s\n" % e)
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
from __future__ import print_function
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
configuration = bombbomb.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.TeamsApi(bombbomb.ApiClient(configuration))
team_id = 'team_id_example' # str | The team id
subteam_id = 'subteam_id_example' # str | The subteam you wish to delete.

try:
    # Delete Subteam
    api_response = api_instance.delete_subteam(team_id, subteam_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->delete_subteam: %s\n" % e)
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

# **get_all_client_group_associations**
> get_all_client_group_associations(client_id)

Lists team associations

Returns a collection of team associations for a given user

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
api_instance = bombbomb.TeamsApi(bombbomb.ApiClient(configuration))
client_id = 'client_id_example' # str | The clientId requesting group associations.

try:
    # Lists team associations
    api_instance.get_all_client_group_associations(client_id)
except ApiException as e:
    print("Exception when calling TeamsApi->get_all_client_group_associations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The clientId requesting group associations. | 

### Return type

void (empty response body)

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
from __future__ import print_function
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
configuration = bombbomb.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.TeamsApi(bombbomb.ApiClient(configuration))
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
    print("Exception when calling TeamsApi->get_client_group_assets: %s\n" % e)
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

# **get_client_group_statistics**
> get_client_group_statistics(team_id, member_status=member_status)

Get Team statistics

Get top level statistic data for a Team

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
api_instance = bombbomb.TeamsApi(bombbomb.ApiClient(configuration))
team_id = 'team_id_example' # str | The team id
member_status = 'member_status_example' # str | The status of members to query for (optional)

try:
    # Get Team statistics
    api_instance.get_client_group_statistics(team_id, member_status=member_status)
except ApiException as e:
    print("Exception when calling TeamsApi->get_client_group_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The team id | 
 **member_status** | **str**| The status of members to query for | [optional] 

### Return type

void (empty response body)

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
from __future__ import print_function
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
configuration = bombbomb.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.TeamsApi(bombbomb.ApiClient(configuration))
team_id = 'team_id_example' # str | The team whose Jericho sends you wish to see.

try:
    # List Jericho Sends
    api_response = api_instance.get_jericho_sends(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_jericho_sends: %s\n" % e)
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
from __future__ import print_function
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
configuration = bombbomb.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.TeamsApi(bombbomb.ApiClient(configuration))
jericho_id = 'jericho_id_example' # str | ID of the Jericho job
team_id = 'team_id_example' # str | ID of team through which Jericho was sent

try:
    # Gets Jericho performance statistics
    api_response = api_instance.get_jericho_stats(jericho_id, team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_jericho_stats: %s\n" % e)
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

# **get_paged_client_group_members**
> get_paged_client_group_members(team_id, page_size, page, status=status, search=search, order_by=order_by, order_direction=order_direction)

List Team Members

Get a paginated listing of Team members

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
api_instance = bombbomb.TeamsApi(bombbomb.ApiClient(configuration))
team_id = 'team_id_example' # str | The team id
page_size = 'page_size_example' # str | Amount of records to return in a page.
page = 'page_example' # str | The page to return.
status = 'status_example' # str | The status type to filter by. (optional)
search = 'search_example' # str | Filter results with names that match the search term. (optional)
order_by = 'order_by_example' # str | Key to order results by (optional)
order_direction = 'order_direction_example' # str | ASC or DESC (optional)

try:
    # List Team Members
    api_instance.get_paged_client_group_members(team_id, page_size, page, status=status, search=search, order_by=order_by, order_direction=order_direction)
except ApiException as e:
    print("Exception when calling TeamsApi->get_paged_client_group_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The team id | 
 **page_size** | **str**| Amount of records to return in a page. | 
 **page** | **str**| The page to return. | 
 **status** | **str**| The status type to filter by. | [optional] 
 **search** | **str**| Filter results with names that match the search term. | [optional] 
 **order_by** | **str**| Key to order results by | [optional] 
 **order_direction** | **str**| ASC or DESC | [optional] 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prompt_monthly_stats**
> str get_prompt_monthly_stats(month, year)

Jericho Monthly Stats

Jericho Monthly Stats

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
api_instance = bombbomb.TeamsApi(bombbomb.ApiClient(configuration))
month = 'month_example' # str | The month whose Jericho sends you wish to see.
year = 'year_example' # str | The year whose Jericho sends you wish to see.

try:
    # Jericho Monthly Stats
    api_response = api_instance.get_prompt_monthly_stats(month, year)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_prompt_monthly_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **month** | **str**| The month whose Jericho sends you wish to see. | 
 **year** | **str**| The year whose Jericho sends you wish to see. | 

### Return type

**str**

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prompt_overview**
> str get_prompt_overview()

Get Prompt Overview

Get Prompt Overview

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
api_instance = bombbomb.TeamsApi(bombbomb.ApiClient(configuration))

try:
    # Get Prompt Overview
    api_response = api_instance.get_prompt_overview()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_prompt_overview: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

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
from __future__ import print_function
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bombbomb.TeamsApi()
team_id = 'team_id_example' # str | The team id

try:
    # List Subteams
    api_response = api_instance.get_subteams(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_subteams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The team id | 

### Return type

[**list[TeamPublicRepresentation]**](TeamPublicRepresentation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_prompt_aggregate_stats**
> get_team_prompt_aggregate_stats(client_group_id)

Get aggregate stats for campaigns

Get all the campaigns aggregate stats

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
api_instance = bombbomb.TeamsApi(bombbomb.ApiClient(configuration))
client_group_id = 'client_group_id_example' # str | ID of the client group association

try:
    # Get aggregate stats for campaigns
    api_instance.get_team_prompt_aggregate_stats(client_group_id)
except ApiException as e:
    print("Exception when calling TeamsApi->get_team_prompt_aggregate_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_group_id** | **str**| ID of the client group association | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_prompt_campaigns**
> get_team_prompt_campaigns(client_group_id, search_term=search_term, current_page=current_page)

Get campaigns for team

Get campaigns for the team and their stats

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
api_instance = bombbomb.TeamsApi(bombbomb.ApiClient(configuration))
client_group_id = 'client_group_id_example' # str | ID of the client group association
search_term = 'search_term_example' # str | The value to search for in prompt subject (optional)
current_page = 'current_page_example' # str | The current page (optional)

try:
    # Get campaigns for team
    api_instance.get_team_prompt_campaigns(client_group_id, search_term=search_term, current_page=current_page)
except ApiException as e:
    print("Exception when calling TeamsApi->get_team_prompt_campaigns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_group_id** | **str**| ID of the client group association | 
 **search_term** | **str**| The value to search for in prompt subject | [optional] 
 **current_page** | **str**| The current page | [optional] 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_to_social_prompt_team**
> invite_to_social_prompt_team(team_id, list_id)

Invite a list to join the admin's social prompt team

Invite to Social Prompt Team

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
api_instance = bombbomb.TeamsApi(bombbomb.ApiClient(configuration))
team_id = 'team_id_example' # str | The team id
list_id = 'list_id_example' # str | List to invite to the social prompt team.

try:
    # Invite a list to join the admin's social prompt team
    api_instance.invite_to_social_prompt_team(team_id, list_id)
except ApiException as e:
    print("Exception when calling TeamsApi->invite_to_social_prompt_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The team id | 
 **list_id** | **str**| List to invite to the social prompt team. | 

### Return type

void (empty response body)

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
from __future__ import print_function
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
configuration = bombbomb.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.TeamsApi(bombbomb.ApiClient(configuration))
config = bombbomb.JerichoConfiguration() # JerichoConfiguration | JSON representing a Jericho configuration
team_id = 'team_id_example' # str | The ID of the team.

try:
    # Creates a Jericho send.
    api_response = api_instance.queue_jericho_send(config, team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->queue_jericho_send: %s\n" % e)
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
from __future__ import print_function
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
configuration = bombbomb.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.TeamsApi(bombbomb.ApiClient(configuration))
team_id = 'team_id_example' # str | The team id
user_id = 'user_id_example' # str | The user id of the member being removed.

try:
    # Remove Member from Team
    api_response = api_instance.remove_member_from_team(team_id, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->remove_member_from_team: %s\n" % e)
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

# **resend_team_member_invitation**
> TeamPublicRepresentation resend_team_member_invitation(team_id, member_user_id)

Resend invite

Resend invitation to a member of a team

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
api_instance = bombbomb.TeamsApi(bombbomb.ApiClient(configuration))
team_id = 'team_id_example' # str | The team id
member_user_id = 'member_user_id_example' # str | The user id of the member being resent an invitation.

try:
    # Resend invite
    api_response = api_instance.resend_team_member_invitation(team_id, member_user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->resend_team_member_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The team id | 
 **member_user_id** | **str**| The user id of the member being resent an invitation. | 

### Return type

[**TeamPublicRepresentation**](TeamPublicRepresentation.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_jericho_prompt_send**
> update_jericho_prompt_send(team_id, jericho_id)

Updates the Jericho Prompt Settings

Updates the prompt settings based on the original email id

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
api_instance = bombbomb.TeamsApi(bombbomb.ApiClient(configuration))
team_id = 'team_id_example' # str | The team id
jericho_id = 'jericho_id_example' # str | ID of the Jericho job

try:
    # Updates the Jericho Prompt Settings
    api_instance.update_jericho_prompt_send(team_id, jericho_id)
except ApiException as e:
    print("Exception when calling TeamsApi->update_jericho_prompt_send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The team id | 
 **jericho_id** | **str**| ID of the Jericho job | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team**
> TeamPublicRepresentation update_team(team_id, name=name, state=state, subteams_can_add_members=subteams_can_add_members)

Update a team

Update fields on a team

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
api_instance = bombbomb.TeamsApi(bombbomb.ApiClient(configuration))
team_id = 'team_id_example' # str | The team id
name = 'name_example' # str | The name of the team (optional)
state = 'state_example' # str | The status of the login permissions (optional)
subteams_can_add_members = true # bool | Updates subteam member adding setting on group (optional)

try:
    # Update a team
    api_response = api_instance.update_team(team_id, name=name, state=state, subteams_can_add_members=subteams_can_add_members)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->update_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The team id | 
 **name** | **str**| The name of the team | [optional] 
 **state** | **str**| The status of the login permissions | [optional] 
 **subteams_can_add_members** | **bool**| Updates subteam member adding setting on group | [optional] 

### Return type

[**TeamPublicRepresentation**](TeamPublicRepresentation.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_team_member**
> update_team_member(team_id, user_id, admin, permission_suite_id=permission_suite_id)

Update Member of Team

Updates a member of a team

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
api_instance = bombbomb.TeamsApi(bombbomb.ApiClient(configuration))
team_id = 'team_id_example' # str | The team id
user_id = 'user_id_example' # str | The user id of the member being added to the team.
admin = true # bool | Set if the user is an admin of this team.
permission_suite_id = 'permission_suite_id_example' # str | Set if the user is an admin of this team. (optional)

try:
    # Update Member of Team
    api_instance.update_team_member(team_id, user_id, admin, permission_suite_id=permission_suite_id)
except ApiException as e:
    print("Exception when calling TeamsApi->update_team_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The team id | 
 **user_id** | **str**| The user id of the member being added to the team. | 
 **admin** | **bool**| Set if the user is an admin of this team. | 
 **permission_suite_id** | **str**| Set if the user is an admin of this team. | [optional] 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

