# JerichoConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**client_group_id** | **str** |  | [optional] 
**send_date** | **datetime** | When the email should be sent. | [optional] 
**is_prompt** | **bool** | Determines whether this is a static or prompted send. | 
**email_id** | **str** | Static send: The Email to send on behalf of the group members. | [optional] 
**prompt_subject** | **str** | Video Prompt: The subject line prompting the user to record a video. | [optional] 
**prompt_body** | **str** | Video Prompt: The HTML body of the email prompting the user to record a video. | [optional] 
**email_subject** | **str** | Video Prompt: The subject line of the final sent email | [optional] 
**email_body** | **str** | Video Prompt: The HTML body of the final sent email. | [optional] 
**send_without_video** | **bool** | Video Prompt: Whether to send the final email if no video was recorded. | [optional] 
**status** | **str** | The state of the send. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


