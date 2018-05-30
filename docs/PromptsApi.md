# bombbomb.PromptsApi

All URIs are relative to *https://api.bombbomb.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_prompt_bot**](PromptsApi.md#create_prompt_bot) | **POST** /prompts/bots | Create a running Prompt Bot for a list
[**create_video_email_prompt**](PromptsApi.md#create_video_email_prompt) | **POST** /prompt | Prompts user to send a video
[**get_alternate_campaign_content**](PromptsApi.md#get_alternate_campaign_content) | **GET** /campaign/{campaignId}/content/alternate | List alternate campaign content
[**get_pending_video_email_prompts**](PromptsApi.md#get_pending_video_email_prompts) | **GET** /prompt/pending | List pending prompts
[**get_prompt_bots**](PromptsApi.md#get_prompt_bots) | **GET** /prompts/bots | List Prompt Bots
[**get_prompt_campaigns**](PromptsApi.md#get_prompt_campaigns) | **GET** /prompts/{userId}/campaigns | List Prompt Campaigns
[**get_video_email_prompt**](PromptsApi.md#get_video_email_prompt) | **GET** /prompt/{id} | Gets a prompt
[**get_video_email_prompts**](PromptsApi.md#get_video_email_prompts) | **GET** /prompt/ | List prompts
[**respond_to_video_email_prompt**](PromptsApi.md#respond_to_video_email_prompt) | **POST** /prompt/{id}/response | Respond to a prompt
[**sync_prompt_subscriptions**](PromptsApi.md#sync_prompt_subscriptions) | **POST** /prompts/campaigns/sync | Syncs Campaigns and One to Ones Subscriptions for User
[**update_prompt**](PromptsApi.md#update_prompt) | **PUT** /prompts/{id} | Update Prompt
[**update_prompt_bot**](PromptsApi.md#update_prompt_bot) | **PUT** /prompts/bots/{id} | Update Prompt Bot
[**update_prompt_campaign**](PromptsApi.md#update_prompt_campaign) | **PUT** /prompts/campaigns/{id} | Update Prompt Campaign
[**update_prompt_template**](PromptsApi.md#update_prompt_template) | **PUT** /prompts/{id}/content | Update Prompt Content


# **create_prompt_bot**
> PromptBot create_prompt_bot(email_id, name, subject, content, contact_field_value_column, bot_type_id, template_id, list_id=list_id, video_id=video_id, end_date=end_date)

Create a running Prompt Bot for a list

Creates a Prompt Bot that sends emails to contacts on a list over the span of time defined.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.PromptsApi()
email_id = 'email_id_example' # str | The default email to use.
name = 'name_example' # str | The name of the bot.
subject = 'subject_example' # str | The subject of the default email.
content = 'content_example' # str | The content used in the email.
contact_field_value_column = 'contact_field_value_column_example' # str | The custom field value column with dates for this bot.
bot_type_id = 'bot_type_id_example' # str | The type of bot to create.
template_id = 'template_id_example' # str | The template used to create the email id.
list_id = 'list_id_example' # str | The list id to attach the bot to. (optional)
video_id = 'video_id_example' # str | The video used in the email. (optional)
end_date = 'end_date_example' # str | The time frame to complete sending to the list. (optional)

try: 
    # Create a running Prompt Bot for a list
    api_response = api_instance.create_prompt_bot(email_id, name, subject, content, contact_field_value_column, bot_type_id, template_id, list_id=list_id, video_id=video_id, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PromptsApi->create_prompt_bot: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_id** | **str**| The default email to use. | 
 **name** | **str**| The name of the bot. | 
 **subject** | **str**| The subject of the default email. | 
 **content** | **str**| The content used in the email. | 
 **contact_field_value_column** | **str**| The custom field value column with dates for this bot. | 
 **bot_type_id** | **str**| The type of bot to create. | 
 **template_id** | **str**| The template used to create the email id. | 
 **list_id** | **str**| The list id to attach the bot to. | [optional] 
 **video_id** | **str**| The video used in the email. | [optional] 
 **end_date** | **str**| The time frame to complete sending to the list. | [optional] 

### Return type

[**PromptBot**](PromptBot.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_video_email_prompt**
> VideoEmailPrompt create_video_email_prompt(prompt)

Prompts user to send a video

Sends the account holder an email prompting them to add a video to a scheduled outgoing message. Recipients, content and timing is all preset for the user.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.PromptsApi()
prompt = bombbomb.VideoEmailPrompt() # VideoEmailPrompt | The Video Email Prompt to be created

try: 
    # Prompts user to send a video
    api_response = api_instance.create_video_email_prompt(prompt)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PromptsApi->create_video_email_prompt: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt** | [**VideoEmailPrompt**](VideoEmailPrompt.md)| The Video Email Prompt to be created | 

### Return type

[**VideoEmailPrompt**](VideoEmailPrompt.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alternate_campaign_content**
> get_alternate_campaign_content(client_group_id)

List alternate campaign content

Returns a list of alternate campaign content by campaign id

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.PromptsApi()
client_group_id = 'client_group_id_example' # str | Id for the campaign

try: 
    # List alternate campaign content
    api_instance.get_alternate_campaign_content(client_group_id)
except ApiException as e:
    print "Exception when calling PromptsApi->get_alternate_campaign_content: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_group_id** | **str**| Id for the campaign | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pending_video_email_prompts**
> list[VideoEmailPrompt] get_pending_video_email_prompts()

List pending prompts

Returns a list of prompts that have not been sent yet, and can still be customized.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.PromptsApi()

try: 
    # List pending prompts
    api_response = api_instance.get_pending_video_email_prompts()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PromptsApi->get_pending_video_email_prompts: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VideoEmailPrompt]**](VideoEmailPrompt.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prompt_bots**
> list[PromptBot] get_prompt_bots()

List Prompt Bots

Returns a list of all Prompt Bots for the user.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.PromptsApi()

try: 
    # List Prompt Bots
    api_response = api_instance.get_prompt_bots()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PromptsApi->get_prompt_bots: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[PromptBot]**](PromptBot.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prompt_campaigns**
> get_prompt_campaigns()

List Prompt Campaigns

Returns a list of all Prompt Campaigns for the user.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.PromptsApi()

try: 
    # List Prompt Campaigns
    api_instance.get_prompt_campaigns()
except ApiException as e:
    print "Exception when calling PromptsApi->get_prompt_campaigns: %s\n" % e
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

# **get_video_email_prompt**
> VideoEmailPrompt get_video_email_prompt(id)

Gets a prompt

Gets a prompt

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.PromptsApi()
id = 'id_example' # str | The Id of the prompt

try: 
    # Gets a prompt
    api_response = api_instance.get_video_email_prompt(id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PromptsApi->get_video_email_prompt: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Id of the prompt | 

### Return type

[**VideoEmailPrompt**](VideoEmailPrompt.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_video_email_prompts**
> list[VideoEmailPrompt] get_video_email_prompts()

List prompts

Returns a list of all prompts.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.PromptsApi()

try: 
    # List prompts
    api_response = api_instance.get_video_email_prompts()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PromptsApi->get_video_email_prompts: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[VideoEmailPrompt]**](VideoEmailPrompt.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **respond_to_video_email_prompt**
> VideoEmailPrompt respond_to_video_email_prompt(id, choice, video_id=video_id, email_id=email_id, subject=subject)

Respond to a prompt

Respond to a prompt by either adding a video, sending without a video or cancelling the prompt.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bombbomb.PromptsApi()
id = 'id_example' # str | The id of the prompt.
choice = 'choice_example' # str | The users' selection. Can be: WithVideo, WithEmail, Cancel, Restore, Reset, Manual
video_id = 'video_id_example' # str | The id of the video. (optional)
email_id = 'email_id_example' # str | The id of the email. (optional)
subject = 'subject_example' # str | The subject of the email (optional)

try: 
    # Respond to a prompt
    api_response = api_instance.respond_to_video_email_prompt(id, choice, video_id=video_id, email_id=email_id, subject=subject)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PromptsApi->respond_to_video_email_prompt: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the prompt. | 
 **choice** | **str**| The users&#39; selection. Can be: WithVideo, WithEmail, Cancel, Restore, Reset, Manual | 
 **video_id** | **str**| The id of the video. | [optional] 
 **email_id** | **str**| The id of the email. | [optional] 
 **subject** | **str**| The subject of the email | [optional] 

### Return type

[**VideoEmailPrompt**](VideoEmailPrompt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_prompt_subscriptions**
> sync_prompt_subscriptions(migrate=migrate)

Syncs Campaigns and One to Ones Subscriptions for User

Syncs Campaigns and One to Ones Subscriptions for User based on their profile information. The user must be a Prompt Subscriber.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.PromptsApi()
migrate = true # bool | After syncing, migrate away from old campaigns. (optional)

try: 
    # Syncs Campaigns and One to Ones Subscriptions for User
    api_instance.sync_prompt_subscriptions(migrate=migrate)
except ApiException as e:
    print "Exception when calling PromptsApi->sync_prompt_subscriptions: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migrate** | **bool**| After syncing, migrate away from old campaigns. | [optional] 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_prompt**
> update_prompt(id, send_mechanism=send_mechanism, facebook_message=facebook_message, twitter_message=twitter_message, video_id=video_id, email_id=email_id, subject=subject, reset_cache=reset_cache, reset_email_content=reset_email_content, status=status)

Update Prompt

Updates a Prompt

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.PromptsApi()
id = 'id_example' # str | The prompt's id
send_mechanism = 'send_mechanism_example' # str | The mechanism for the prompt to be sent (optional)
facebook_message = 'facebook_message_example' # str | The facebook message assigned to the prompt (optional)
twitter_message = 'twitter_message_example' # str | The twitter message assigned to the prompt (optional)
video_id = 'video_id_example' # str | The id of the video. (optional)
email_id = 'email_id_example' # str | The id of the email. (optional)
subject = 'subject_example' # str | The subject of the email (optional)
reset_cache = 'reset_cache_example' # str | The subject of the email (optional)
reset_email_content = 'reset_email_content_example' # str | The subject of the email (optional)
status = 'status_example' # str | The status of the prompt (optional)

try: 
    # Update Prompt
    api_instance.update_prompt(id, send_mechanism=send_mechanism, facebook_message=facebook_message, twitter_message=twitter_message, video_id=video_id, email_id=email_id, subject=subject, reset_cache=reset_cache, reset_email_content=reset_email_content, status=status)
except ApiException as e:
    print "Exception when calling PromptsApi->update_prompt: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The prompt&#39;s id | 
 **send_mechanism** | **str**| The mechanism for the prompt to be sent | [optional] 
 **facebook_message** | **str**| The facebook message assigned to the prompt | [optional] 
 **twitter_message** | **str**| The twitter message assigned to the prompt | [optional] 
 **video_id** | **str**| The id of the video. | [optional] 
 **email_id** | **str**| The id of the email. | [optional] 
 **subject** | **str**| The subject of the email | [optional] 
 **reset_cache** | **str**| The subject of the email | [optional] 
 **reset_email_content** | **str**| The subject of the email | [optional] 
 **status** | **str**| The status of the prompt | [optional] 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_prompt_bot**
> PromptBot update_prompt_bot(id, email_id, name, subject, content, contact_field_value_column, template_id, list_id=list_id, video_id=video_id, end_date=end_date, status=status)

Update Prompt Bot

Updates a Prompt Bot's settings.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.PromptsApi()
id = 'id_example' # str | The bot id.
email_id = 'email_id_example' # str | The default email to use.
name = 'name_example' # str | The name of the bot.
subject = 'subject_example' # str | The subject of the default email.
content = 'content_example' # str | The content used in the default email.
contact_field_value_column = 'contact_field_value_column_example' # str | The custom field value column with dates for this bot.
template_id = 'template_id_example' # str | The template used to create the email id.
list_id = 'list_id_example' # str | The list id to attach the bot to. (optional)
video_id = 'video_id_example' # str | The video used in the default email. (optional)
end_date = 'end_date_example' # str | The time frame to complete sending to the list. (optional)
status = 'status_example' # str | The status of the bot. (optional)

try: 
    # Update Prompt Bot
    api_response = api_instance.update_prompt_bot(id, email_id, name, subject, content, contact_field_value_column, template_id, list_id=list_id, video_id=video_id, end_date=end_date, status=status)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling PromptsApi->update_prompt_bot: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The bot id. | 
 **email_id** | **str**| The default email to use. | 
 **name** | **str**| The name of the bot. | 
 **subject** | **str**| The subject of the default email. | 
 **content** | **str**| The content used in the default email. | 
 **contact_field_value_column** | **str**| The custom field value column with dates for this bot. | 
 **template_id** | **str**| The template used to create the email id. | 
 **list_id** | **str**| The list id to attach the bot to. | [optional] 
 **video_id** | **str**| The video used in the default email. | [optional] 
 **end_date** | **str**| The time frame to complete sending to the list. | [optional] 
 **status** | **str**| The status of the bot. | [optional] 

### Return type

[**PromptBot**](PromptBot.md)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_prompt_campaign**
> update_prompt_campaign(client_group_id, branded_template_id=branded_template_id, personal_template_id=personal_template_id, enabled=enabled, send_mechanism=send_mechanism)

Update Prompt Campaign

Updates a Prompt Campaign's Settings

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.PromptsApi()
client_group_id = 'client_group_id_example' # str | The client group of the campaign.
branded_template_id = 'branded_template_id_example' # str | The template to use for branded feel emails. (optional)
personal_template_id = 'personal_template_id_example' # str | The template to use for personal feel emails. (optional)
enabled = true # bool | Set whether the user is able to start receiving prompts. (optional)
send_mechanism = 'send_mechanism_example' # str | The way to send the prompt (optional)

try: 
    # Update Prompt Campaign
    api_instance.update_prompt_campaign(client_group_id, branded_template_id=branded_template_id, personal_template_id=personal_template_id, enabled=enabled, send_mechanism=send_mechanism)
except ApiException as e:
    print "Exception when calling PromptsApi->update_prompt_campaign: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_group_id** | **str**| The client group of the campaign. | 
 **branded_template_id** | **str**| The template to use for branded feel emails. | [optional] 
 **personal_template_id** | **str**| The template to use for personal feel emails. | [optional] 
 **enabled** | **bool**| Set whether the user is able to start receiving prompts. | [optional] 
 **send_mechanism** | **str**| The way to send the prompt | [optional] 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_prompt_template**
> update_prompt_template(id, alternate_content_id, new_email_id, og_email_id, new_example_video_id)

Update Prompt Content

Updates a Prompt Content

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.PromptsApi()
id = 'id_example' # str | The prompt's id
alternate_content_id = 'alternate_content_id_example' # str | The alternate content id
new_email_id = 'new_email_id_example' # str | The prompt's new email id
og_email_id = 'og_email_id_example' # str | The prompt's original email id
new_example_video_id = 'new_example_video_id_example' # str | The prompt's new tutorial video id

try: 
    # Update Prompt Content
    api_instance.update_prompt_template(id, alternate_content_id, new_email_id, og_email_id, new_example_video_id)
except ApiException as e:
    print "Exception when calling PromptsApi->update_prompt_template: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The prompt&#39;s id | 
 **alternate_content_id** | **str**| The alternate content id | 
 **new_email_id** | **str**| The prompt&#39;s new email id | 
 **og_email_id** | **str**| The prompt&#39;s original email id | 
 **new_example_video_id** | **str**| The prompt&#39;s new tutorial video id | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

