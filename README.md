# bombbomb
We make it easy to build relationships using simple videos.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0.0
- Package version: 2.0.0
- Build date: 2018-05-30T21:56:10.861Z
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
api_instance = bombbomb.AccountsApi

try:
    # Get account details.
    api_instance.account_details()
except ApiException as e:
    print "Exception when calling AccountsApi->account_details: %s\n" % e

```

## Documentation for API Endpoints

All URIs are relative to *https://api.bombbomb.com/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**account_details**](docs/AccountsApi.md#account_details) | **GET** /accounts | Get account details.
*AccountsApi* | [**create_account**](docs/AccountsApi.md#create_account) | **POST** /accounts | Create Account
*AccountsApi* | [**get_client_statistics**](docs/AccountsApi.md#get_client_statistics) | **GET** /accounts/stats | Get Client Statistics
*AccountsApi* | [**get_user_country**](docs/AccountsApi.md#get_user_country) | **GET** /accounts/{clientId}/country | Gets user country
*AccountsApi* | [**reset_api_key**](docs/AccountsApi.md#reset_api_key) | **PUT** /accounts/apikey | Reset API key
*AccountsApi* | [**subscription_purchase_allowed**](docs/AccountsApi.md#subscription_purchase_allowed) | **GET** /accounts/purchaseable | Check if subscription purchase allowed.
*AccountsApi* | [**update_profile_data**](docs/AccountsApi.md#update_profile_data) | **POST** /account/profile/ | Add profile information.
*AutomationsApi* | [**get_drip_drop_stats**](docs/AutomationsApi.md#get_drip_drop_stats) | **GET** /automation/{dripId}/dripdrop/{dripDropId}/stats | Get Automation Email Stats
*AutomationsApi* | [**get_drip_stats**](docs/AutomationsApi.md#get_drip_stats) | **GET** /automation/{id}/stats | Get Automation Stats
*ContactsApi* | [**add_contacts_csv**](docs/ContactsApi.md#add_contacts_csv) | **POST** /contacts/import_csv | Add contacts from a CSV file.
*ContactsApi* | [**add_new_contact**](docs/ContactsApi.md#add_new_contact) | **POST** /contacts/ | Add a contact.
*ContactsApi* | [**add_new_custom_field**](docs/ContactsApi.md#add_new_custom_field) | **POST** /contacts/custom_fields/ | Add custom fields.
*ContactsApi* | [**add_pasted_contacts**](docs/ContactsApi.md#add_pasted_contacts) | **POST** /contacts/paste | Add pasted contacts.
*ContactsApi* | [**c_sv_to_object**](docs/ContactsApi.md#c_sv_to_object) | **POST** /csv-to-object | Format CSV.
*ContactsApi* | [**delete_contacts**](docs/ContactsApi.md#delete_contacts) | **PUT** /contacts/delete | Delete Contacts
*ContactsApi* | [**get_contact_by_id**](docs/ContactsApi.md#get_contact_by_id) | **GET** /contact/{id} | Get Contact Details
*ContactsApi* | [**get_custom_fields**](docs/ContactsApi.md#get_custom_fields) | **GET** /contacts/custom_fields/ | Get custom fields.
*CurriculumApi* | [**get_curricula**](docs/CurriculumApi.md#get_curricula) | **GET** /curricula/ | Get Curricula
*CurriculumApi* | [**get_user_curriculum_with_progress**](docs/CurriculumApi.md#get_user_curriculum_with_progress) | **GET** /curriculum/getForUserWithProgress | Get Detailed For User
*EmailsApi* | [**create_printing_press_email**](docs/EmailsApi.md#create_printing_press_email) | **POST** /emails/print | Create an Email with Printing Press
*EmailsApi* | [**get_all_templates_for_current_user**](docs/EmailsApi.md#get_all_templates_for_current_user) | **GET** /emails/templates | Get all user templates
*EmailsApi* | [**get_email_tracking**](docs/EmailsApi.md#get_email_tracking) | **GET** /emails/{emailId}/tracking | Get Email Tracking
*EmailsApi* | [**get_email_tracking_interactions**](docs/EmailsApi.md#get_email_tracking_interactions) | **GET** /emails/{emailId}/tracking/interactions | Get Email Tracking Interactions
*EmailsApi* | [**get_hourly_email_tracking**](docs/EmailsApi.md#get_hourly_email_tracking) | **GET** /emails/{emailId}/tracking/hourly | Get Hourly Email Tracking
*EmailsApi* | [**get_live_fire_data**](docs/EmailsApi.md#get_live_fire_data) | **GET** /emails/livefire | Get livefire feed data
*EmailsApi* | [**get_quick_send_templates**](docs/EmailsApi.md#get_quick_send_templates) | **GET** /emails/quicksend/templates | Get all quicksend templates
*EmailsApi* | [**get_template_html_for_template_id**](docs/EmailsApi.md#get_template_html_for_template_id) | **GET** /emails/templates/{templateId}/html | Get the HTML for a given template
*EmailsApi* | [**get_video_quick_sender_data**](docs/EmailsApi.md#get_video_quick_sender_data) | **GET** /emails/quicksend | Get quicksend data
*EmailsApi* | [**save_quick_sender_settings**](docs/EmailsApi.md#save_quick_sender_settings) | **POST** /emails/quicksend/settings | Save quicksender settings
*EmailsApi* | [**video_quick_sender**](docs/EmailsApi.md#video_quick_sender) | **POST** /emails/quicksend | Send a quicksend email
*FilesApi* | [**doc_host_delete**](docs/FilesApi.md#doc_host_delete) | **DELETE** /files/{docId} | Delete file
*FilesApi* | [**doc_host_get**](docs/FilesApi.md#doc_host_get) | **GET** /files/{docId} | Get file
*FilesApi* | [**doc_host_list**](docs/FilesApi.md#doc_host_list) | **GET** /files | List all files
*FilesApi* | [**doc_host_upload_v2**](docs/FilesApi.md#doc_host_upload_v2) | **POST** /files | Upload a file
*FilesApi* | [**get_hosted_images_paged**](docs/FilesApi.md#get_hosted_images_paged) | **GET** /files/images/paged | Get paged hosted images
*FormsApi* | [**get_form_tracking_as_csv**](docs/FormsApi.md#get_form_tracking_as_csv) | **GET** /forms/{id}/tracking/export | Get csv
*IntegrationsApi* | [**connect_integration**](docs/IntegrationsApi.md#connect_integration) | **POST** /integrations | Activate an integration for a user.
*IntegrationsApi* | [**delete_integration**](docs/IntegrationsApi.md#delete_integration) | **DELETE** /integrations | Remove an integration for a user.
*IntegrationsApi* | [**get_integration_health**](docs/IntegrationsApi.md#get_integration_health) | **GET** /integrations/health/{code} | Get health for a given integration
*IntegrationsApi* | [**get_integration_page_components**](docs/IntegrationsApi.md#get_integration_page_components) | **GET** /integrations/pageComponents | Get page components for a given integration
*IntegrationsApi* | [**sync_users_integrated_lists**](docs/IntegrationsApi.md#sync_users_integrated_lists) | **GET** /integrations/sync | Synchronize your integration list or lists.
*ListsApi* | [**add_new_list**](docs/ListsApi.md#add_new_list) | **POST** /lists/ | Add list.
*ListsApi* | [**clear_list**](docs/ListsApi.md#clear_list) | **PUT** /lists/{listId}/clear | Clear Contacts from List
*ListsApi* | [**copy_list_contacts**](docs/ListsApi.md#copy_list_contacts) | **POST** /lists/{listId}/copy | Copy All Contacts from a List
*ListsApi* | [**get_all_lists**](docs/ListsApi.md#get_all_lists) | **GET** /lists/ | Get all Lists
*ListsApi* | [**suppress_all_in_list**](docs/ListsApi.md#suppress_all_in_list) | **PUT** /lists/{listId}/suppress | Suppress All Contacts from List
*OrdersApi* | [**template_asset_delete**](docs/OrdersApi.md#template_asset_delete) | **DELETE** /orders/templates/images | Deletes image from user s3 store
*PromptsApi* | [**create_prompt_bot**](docs/PromptsApi.md#create_prompt_bot) | **POST** /prompts/bots | Create a running Prompt Bot for a list
*PromptsApi* | [**create_video_email_prompt**](docs/PromptsApi.md#create_video_email_prompt) | **POST** /prompt | Prompts user to send a video
*PromptsApi* | [**get_alternate_campaign_content**](docs/PromptsApi.md#get_alternate_campaign_content) | **GET** /campaign/{campaignId}/content/alternate | List alternate campaign content
*PromptsApi* | [**get_pending_video_email_prompts**](docs/PromptsApi.md#get_pending_video_email_prompts) | **GET** /prompt/pending | List pending prompts
*PromptsApi* | [**get_prompt_bots**](docs/PromptsApi.md#get_prompt_bots) | **GET** /prompts/bots | List Prompt Bots
*PromptsApi* | [**get_prompt_campaigns**](docs/PromptsApi.md#get_prompt_campaigns) | **GET** /prompts/{userId}/campaigns | List Prompt Campaigns
*PromptsApi* | [**get_video_email_prompt**](docs/PromptsApi.md#get_video_email_prompt) | **GET** /prompt/{id} | Gets a prompt
*PromptsApi* | [**get_video_email_prompts**](docs/PromptsApi.md#get_video_email_prompts) | **GET** /prompt/ | List prompts
*PromptsApi* | [**respond_to_video_email_prompt**](docs/PromptsApi.md#respond_to_video_email_prompt) | **POST** /prompt/{id}/response | Respond to a prompt
*PromptsApi* | [**sync_prompt_subscriptions**](docs/PromptsApi.md#sync_prompt_subscriptions) | **POST** /prompts/campaigns/sync | Syncs Campaigns and One to Ones Subscriptions for User
*PromptsApi* | [**update_prompt**](docs/PromptsApi.md#update_prompt) | **PUT** /prompts/{id} | Update Prompt
*PromptsApi* | [**update_prompt_bot**](docs/PromptsApi.md#update_prompt_bot) | **PUT** /prompts/bots/{id} | Update Prompt Bot
*PromptsApi* | [**update_prompt_campaign**](docs/PromptsApi.md#update_prompt_campaign) | **PUT** /prompts/campaigns/{id} | Update Prompt Campaign
*PromptsApi* | [**update_prompt_template**](docs/PromptsApi.md#update_prompt_template) | **PUT** /prompts/{id}/content | Update Prompt Content
*SocialsApi* | [**get_facebook_pages**](docs/SocialsApi.md#get_facebook_pages) | **GET** /socials/facebook/pages | Gets facebook pages
*SocialsApi* | [**get_social_article_properties**](docs/SocialsApi.md#get_social_article_properties) | **GET** /socials/properties | Gets the social email properties
*SocialsApi* | [**get_social_authorizations**](docs/SocialsApi.md#get_social_authorizations) | **GET** /socials/authorizations | Get authorizations for all social integration
*SocialsApi* | [**get_social_profile_properties**](docs/SocialsApi.md#get_social_profile_properties) | **GET** /socials/profile | Gets the profile properties
*SocialsApi* | [**get_social_stats**](docs/SocialsApi.md#get_social_stats) | **GET** /socials/{promptId}/stats | Get social stats for a prompt
*SocialsApi* | [**post_social_content**](docs/SocialsApi.md#post_social_content) | **POST** /socials/content | Creates social content
*SocialsApi* | [**retry_social_send**](docs/SocialsApi.md#retry_social_send) | **POST** /socials/send/retry | Sends social content
*SocialsApi* | [**send_social**](docs/SocialsApi.md#send_social) | **POST** /socials/send | Sends social content
*SocialsApi* | [**update_client_group_send_mechanism**](docs/SocialsApi.md#update_client_group_send_mechanism) | **PUT** /socials/client/sendMechanism | Gets the auto shares from the client group assoc id
*SocialsApi* | [**update_client_groups_send_mechanism**](docs/SocialsApi.md#update_client_groups_send_mechanism) | **PUT** /socials/client/sendMechanisms | Toggles the prompt campaigns in a users account
*SocialsApi* | [**update_facebook_pages**](docs/SocialsApi.md#update_facebook_pages) | **PUT** /socials/facebook/pages | Updates facebook page Ids
*SocialsApi* | [**update_social_content**](docs/SocialsApi.md#update_social_content) | **PUT** /socials/content | Updates social content
*TeamsApi* | [**add_team_member**](docs/TeamsApi.md#add_team_member) | **POST** /team/{teamId}/member | Add Member to Team
*TeamsApi* | [**add_users**](docs/TeamsApi.md#add_users) | **POST** /team/{teamId}/members | Add users to group.
*TeamsApi* | [**add_users_from_csv**](docs/TeamsApi.md#add_users_from_csv) | **POST** /team/{teamId}/members/csv | Add members to group from CSV
*TeamsApi* | [**cancel_jericho_send**](docs/TeamsApi.md#cancel_jericho_send) | **DELETE** /team/{teamId}/jericho/{jerichoId} | Cancel a Jericho Send
*TeamsApi* | [**create_subteam**](docs/TeamsApi.md#create_subteam) | **POST** /team/{teamId}/subteam | Add a Subteam
*TeamsApi* | [**delete_subteam**](docs/TeamsApi.md#delete_subteam) | **DELETE** /team/{teamId}/subteam | Delete Subteam
*TeamsApi* | [**get_all_client_group_associations**](docs/TeamsApi.md#get_all_client_group_associations) | **GET** /team/associations/ | Lists team associations
*TeamsApi* | [**get_client_group_assets**](docs/TeamsApi.md#get_client_group_assets) | **GET** /team/assets/ | Lists team assets
*TeamsApi* | [**get_client_group_statistics**](docs/TeamsApi.md#get_client_group_statistics) | **GET** /team/{teamId}/stats | Get Team statistics
*TeamsApi* | [**get_jericho_sends**](docs/TeamsApi.md#get_jericho_sends) | **GET** /team/{teamId}/jericho | List Jericho Sends
*TeamsApi* | [**get_jericho_stats**](docs/TeamsApi.md#get_jericho_stats) | **GET** /team/{teamId}/jericho/{jerichoId}/performance | Gets Jericho performance statistics
*TeamsApi* | [**get_paged_client_group_members**](docs/TeamsApi.md#get_paged_client_group_members) | **GET** /team/{teamId}/members | List Team Members
*TeamsApi* | [**get_subteams**](docs/TeamsApi.md#get_subteams) | **GET** /team/{teamId}/subteam | List Subteams
*TeamsApi* | [**get_team_prompt_aggregate_stats**](docs/TeamsApi.md#get_team_prompt_aggregate_stats) | **GET** /team/{clientGroupId}/campaign/stats | Get aggregate stats for campaigns
*TeamsApi* | [**get_team_prompt_campaigns**](docs/TeamsApi.md#get_team_prompt_campaigns) | **GET** /team/{clientGroupId}/campaign | Get campaigns for team
*TeamsApi* | [**invite_to_social_prompt_team**](docs/TeamsApi.md#invite_to_social_prompt_team) | **POST** /teams/prompt/invite | Invite a list to join the admin&#39;s social prompt team
*TeamsApi* | [**queue_jericho_send**](docs/TeamsApi.md#queue_jericho_send) | **POST** /team/{teamId}/jericho | Creates a Jericho send.
*TeamsApi* | [**remove_member_from_team**](docs/TeamsApi.md#remove_member_from_team) | **DELETE** /team/{teamId}/member/{userId} | Remove Member from Team
*TeamsApi* | [**resend_team_member_invitation**](docs/TeamsApi.md#resend_team_member_invitation) | **POST** /team/{teamId}/{memberUserId}/rewelcome | Resend invite
*TeamsApi* | [**update_jericho_prompt_send**](docs/TeamsApi.md#update_jericho_prompt_send) | **PUT** /team/{teamId}/jericho/{jerichoId} | Updates the Jericho Prompt Settings
*TeamsApi* | [**update_team**](docs/TeamsApi.md#update_team) | **POST** /team/{teamId} | Update a team
*TeamsApi* | [**update_team_member**](docs/TeamsApi.md#update_team_member) | **PUT** /team/{teamId}/member | Update Member of Team
*UtilitiesApi* | [**create_o_auth_client**](docs/UtilitiesApi.md#create_o_auth_client) | **POST** /oauthclient | Create an OAuth Client
*UtilitiesApi* | [**delete_o_auth_client**](docs/UtilitiesApi.md#delete_o_auth_client) | **DELETE** /oauthclient/{id} | Delete an OAuth Client
*UtilitiesApi* | [**get_o_auth_clients**](docs/UtilitiesApi.md#get_o_auth_clients) | **GET** /oauthclient | Lists OAuth Clients
*UtilitiesApi* | [**get_spec**](docs/UtilitiesApi.md#get_spec) | **GET** /spec | Describes this api
*VideosApi* | [**get_video_encoding_status**](docs/VideosApi.md#get_video_encoding_status) | **GET** /videos/{videoId}/status | Video Encoding Status
*VideosApi* | [**get_video_recorder**](docs/VideosApi.md#get_video_recorder) | **GET** /videos/live/getRecorder | Get Live Video Recorder HTML
*VideosApi* | [**mark_live_recording_complete**](docs/VideosApi.md#mark_live_recording_complete) | **POST** /videos/live/markComplete | Completes a live recording
*VideosApi* | [**sign_upload**](docs/VideosApi.md#sign_upload) | **POST** /video/signedUpload | Generate Signed Url
*VideosApi* | [**update_video_thumbnail_v2**](docs/VideosApi.md#update_video_thumbnail_v2) | **PUT** /videos/thumbnail | Upload thumbnail
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
 - [HostedDoc](docs/HostedDoc.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse200Items](docs/InlineResponse200Items.md)
 - [JerichoConfiguration](docs/JerichoConfiguration.md)
 - [JerichoPerformance](docs/JerichoPerformance.md)
 - [OAuthClient](docs/OAuthClient.md)
 - [PromptBot](docs/PromptBot.md)
 - [PromptSocialPrompt](docs/PromptSocialPrompt.md)
 - [SignUploadRequest](docs/SignUploadRequest.md)
 - [SignUploadResponse](docs/SignUploadResponse.md)
 - [String](docs/String.md)
 - [TeamPublicRepresentation](docs/TeamPublicRepresentation.md)
 - [VideoEmailPrompt](docs/VideoEmailPrompt.md)
 - [VideoEncodingStatusResponse](docs/VideoEncodingStatusResponse.md)
 - [VideoPublicRepresentation](docs/VideoPublicRepresentation.md)
 - [VideoRecorderMethodResponse](docs/VideoRecorderMethodResponse.md)


## Documentation For Authorization


## BBOAuth2

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: https://app.bombbomb.com/auth/authorize
- **Scopes**: 
 - **all:manage**: View & Manage your BombBomb information
 - **all:read**: View your BombBomb information
 - **email:manage**: View & Manage your BombBomb emails
 - **email:read**: View your BombBomb emails
 - **video:manage**: View & Manage your BombBomb videos
 - **video:read**: View your BombBomb videos
 - **contact:manage**: View & Manage your BombBomb contacts
 - **contact:read**: View your BombBomb contacts
 - **curriculum:manage**: View & Manage your BombBomb challenges
 - **curriculum:read**: View your BombBomb challenges
 - **automation:manage**: View & Manage your BombBomb automations
 - **automation:read**: View your BombBomb automations
 - **form:manage**: View & Manage your BombBomb forms
 - **form:read**: View your BombBomb forms
 - **list:manage**: View & Manage your BombBomb lists
 - **team:manage**: View & Manage your BombBomb teams
 - **team:read**: View your BombBomb teams
 - **order:manage**: Manage your BombBomb orders
 - **settings:manage**: Manage your BombBomb settings
 - **file:manage**: View & Manage your BombBomb files
 - **file:read**: View your BombBomb files
 - **account:manage**: View & Manage your BombBomb account
 - **account:read**: View your BombBomb account


## Author



