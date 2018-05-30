# PromptSocialPrompt

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the prompt. Read Only. | [optional] 
**user_id** | **str** | The prompt&#39;s owner. Read Only. | [optional] 
**jericho_id** | **str** | If sent in a jericho context, this will have the jericho id | [optional] 
**prompt_subject** | **str** | The prompt&#39;s subject line | [optional] 
**prompt_html** | **str** | The suggested script of the prompt. | [optional] 
**scheduled_send_date** | **datetime** | When the final email is scheduled to be sent | [optional] 
**client_group_id** | **str** | The client group campaign that created the prompt. | [optional] 
**thumbnail_url** | **str** | The URL of a thumbnail image for this prompt | [optional] 
**status** | **int** | The status of the prompt: created &#x3D; 0, sent &#x3D; 10, recorded &#x3D; 20, job_created &#x3D; 30, timed_out &#x3D; 40, declined &#x3D; 50 Read Only | [optional] 
**created_date** | **datetime** | When the email was first sent out | [optional] 
**last_notified** | **datetime** | When the user was last notified about a prompt email waiting for a video | [optional] 
**send_mechanism** | **datetime** | The sendMechanism property | [optional] 
**send_types** | **list[str]** | The types of mechanisms this prompt can send. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


