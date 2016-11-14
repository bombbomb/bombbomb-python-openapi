# bombbomb
We make it easy to build relationships using simple videos.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0.21432
- Package version: 2.0.21432
- Build date: 2016-11-14T17:58:04.401Z
- Build package: class io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import bombbomb 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import bombbomb
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# create an instance of the API class
api_instance = bombbomb.CurriculumApi
include_progress = true # bool | Whether to return progress with the curriculum. (optional)

try:
    # Get Curricula
    api_response = api_instance.get_curricula(include_progress=include_progress)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CurriculumApi->get_curricula: %s\n" % e

```

## Documentation for API Endpoints

All URIs are relative to *https://api.bombbomb.com/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CurriculumApi* | [**get_curricula**](docs/CurriculumApi.md#get_curricula) | **GET** /curricula/ | Get Curricula
*CurriculumApi* | [**get_user_curriculum_with_progress**](docs/CurriculumApi.md#get_user_curriculum_with_progress) | **GET** /curriculum/getForUserWithProgress | Get Detailed For User
*PromptsApi* | [**create_video_email_prompt**](docs/PromptsApi.md#create_video_email_prompt) | **POST** /prompt | Prompts user to send a video
*PromptsApi* | [**get_video_email_prompt**](docs/PromptsApi.md#get_video_email_prompt) | **GET** /prompt/{id} | Gets a prompt
*PromptsApi* | [**respond_to_video_email_prompt**](docs/PromptsApi.md#respond_to_video_email_prompt) | **POST** /prompt/{id}/response | Respond to a prompt
*TeamsApi* | [**add_team_member**](docs/TeamsApi.md#add_team_member) | **POST** /team/{teamId}/member | Add Member to Team
*TeamsApi* | [**cancel_jericho_send**](docs/TeamsApi.md#cancel_jericho_send) | **DELETE** /team/{teamId}/jericho/{jerichoId} | Cancel a Jericho Send
*TeamsApi* | [**create_subteam**](docs/TeamsApi.md#create_subteam) | **POST** /team/{teamId}/subteam | Add a Subteam
*TeamsApi* | [**delete_subteam**](docs/TeamsApi.md#delete_subteam) | **DELETE** /team/{teamId}/subteam | Delete Subteam
*TeamsApi* | [**get_client_group_assets**](docs/TeamsApi.md#get_client_group_assets) | **GET** /team/assets/ | Lists team assets
*TeamsApi* | [**get_jericho_sends**](docs/TeamsApi.md#get_jericho_sends) | **GET** /team/{teamId}/jericho | List Jericho Sends
*TeamsApi* | [**get_jericho_stats**](docs/TeamsApi.md#get_jericho_stats) | **GET** /team/{teamId}/jericho/{jerichoId}/performance | Gets Jericho performance statistics
*TeamsApi* | [**get_subteams**](docs/TeamsApi.md#get_subteams) | **GET** /team/{teamId}/subteam | List Subteams
*TeamsApi* | [**queue_jericho_send**](docs/TeamsApi.md#queue_jericho_send) | **POST** /team/{teamId}/jericho | Creates a Jericho send.
*TeamsApi* | [**remove_member_from_team**](docs/TeamsApi.md#remove_member_from_team) | **DELETE** /team/{teamId}/member/{userId} | Remove Member from Team
*TeamsApi* | [**update_team**](docs/TeamsApi.md#update_team) | **POST** /team/{teamId} | Update a team
*UtilitiesApi* | [**create_o_auth_client**](docs/UtilitiesApi.md#create_o_auth_client) | **POST** /oauthclient | Create an OAuth Client
*UtilitiesApi* | [**delete_o_auth_client**](docs/UtilitiesApi.md#delete_o_auth_client) | **DELETE** /oauthclient/{id} | Delete an OAuth Client
*UtilitiesApi* | [**get_o_auth_clients**](docs/UtilitiesApi.md#get_o_auth_clients) | **GET** /oauthclient | Lists OAuth Clients
*UtilitiesApi* | [**get_spec**](docs/UtilitiesApi.md#get_spec) | **GET** /spec | Describes this api
*WebhooksApi* | [**add_web_hook**](docs/WebhooksApi.md#add_web_hook) | **POST** /webhook | Add Webhook
*WebhooksApi* | [**delete_web_hook**](docs/WebhooksApi.md#delete_web_hook) | **DELETE** /webhook/{hookId} | Deletes Webhook
*WebhooksApi* | [**get_web_hooks**](docs/WebhooksApi.md#get_web_hooks) | **GET** /webhook/ | Lists Webhooks
*WebhooksApi* | [**list_web_hook_events**](docs/WebhooksApi.md#list_web_hook_events) | **GET** /webhook/events | Describe WebHook Events
*WebhooksApi* | [**send_webhook_example**](docs/WebhooksApi.md#send_webhook_example) | **POST** /webhook/test | Sends test Webhook


## Documentation For Models

 - [BBWebHook](docs/BBWebHook.md)
 - [Curriculum](docs/Curriculum.md)
 - [CurriculumUserProgress](docs/CurriculumUserProgress.md)
 - [CurriculumWithProgress](docs/CurriculumWithProgress.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse200Items](docs/InlineResponse200Items.md)
 - [JerichoConfiguration](docs/JerichoConfiguration.md)
 - [JerichoPerformance](docs/JerichoPerformance.md)
 - [OAuthClient](docs/OAuthClient.md)
 - [String](docs/String.md)
 - [TeamPublicRepresentation](docs/TeamPublicRepresentation.md)
 - [VideoEmailPrompt](docs/VideoEmailPrompt.md)


## Documentation For Authorization


## BBOAuth2

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: https://app.bombbomb.com/auth/authorize
- **Scopes**: 
 - **all:manage**: Manage All
 - **all:read**: Read All
 - **email:manage**: Manage Email
 - **email:read**: Read Email
 - **video:manage**: Manage Video
 - **video:read**: Read Video
 - **contact:manage**: Manage Contact
 - **contact:read**: Read Contact
 - **curriculum:manage**: Manage Curriculum
 - **curriculum:read**: Read Curriculum
 - **automation:manage**: Manage Automation
 - **automation:read**: Read Automation
 - **form:manage**: Manage Form
 - **form:read**: Read Form
 - **team:manage**: Manage Team
 - **team:read**: Read Team
 - **settings:manage**: Manage Settings


## Author



