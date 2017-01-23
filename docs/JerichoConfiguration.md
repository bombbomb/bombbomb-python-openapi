# JerichoConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**client_group_id** | **str** |  | [optional] 
**send_date** | **datetime** | When the email should be sent. | [optional] 
**is_prompt** | **bool** | Video Prompt: Determines whether this is a static or prompted send. | 
**print_to_template** | **bool** | Controls whether or not the content is printed into a template. | [optional] 
**email_id** | **str** | Static send: The Email to send on behalf of the group members. | [optional] 
**example_video_id** | **str** | Video Prompt: The Video to include as an example for prompted users. | [optional] 
**follow_up_video_id** | **str** | The Video to include in the tracking follow up. | [optional] 
**prompt_intro** | **str** | Video Prompt: The intro text directed toward prompted users. | [optional] 
**prompt_subject** | **str** | Video Prompt: The subject line prompting the user to record a video. | [optional] 
**prompt_body** | **str** | Video Prompt: The HTML body of the email prompting the user to record a video. | [optional] 
**email_subject** | **str** | Video Prompt: The subject line of the final sent email | [optional] 
**email_body** | **str** | Video Prompt: The HTML body of the final sent email. | [optional] 
**send_without_video** | **bool** | Video Prompt: Whether to send the final email if no video was recorded. | [optional] 
**status** | **str** | The state of the send. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


