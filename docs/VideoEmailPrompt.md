# VideoEmailPrompt

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the prompt. Read Only. | [optional] 
**user_id** | **str** | The prompt&#39;s owner. Read Only. | [optional] 
**template_id** | **str** | Optional. The email template to be used in the sent email, if none supplied, the users&#39; default will be applied. | [optional] 
**email_subject_line** | **str** | The subject line of the final email | 
**email_content** | **str** | The HTML content of the final email | 
**to_email_addresses** | **list[str]** | Email addresses to send the final email to, can be mixed with listIds. | [optional] 
**to_lists** | **list[str]** | List Ids to send the final email to | [optional] 
**jericho_id** | **str** | If sent in a jericho context, this will have the jericho id | [optional] 
**prompt_subject** | **str** | The prompt&#39;s subject line | 
**prompt_html** | **str** | The HTML body of the prompt | 
**send_without_video** | **bool** | Whether to send the email if no video is recorded. If set to require a video, and none is added before the videoDueDate, the prompt is cancelled. | [optional] 
**video_due_date** | **datetime** | When the video must be recorded by | [optional] 
**scheduled_send_date** | **datetime** | When the final email is scheduled to be sent | 
**video_id** | **str** | The video that was added to the prompt. Read Only. | [optional] 
**email_id** | **str** | The email that was created by the prompt Read Only. | [optional] 
**job_id** | **str** | The job sent by the prompt Read Only. | [optional] 
**status** | **int** | The status of the prompt: created &#x3D; 0, sent &#x3D; 10, recorded &#x3D; 20, job_created &#x3D; 30, timed_out &#x3D; 40, declined &#x3D; 50 Read Only | [optional] 
**do_not_apply_template** | **bool** | Controls whether a user template is applied to the message as it is sent | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


