# bombbomb.ContactsApi

All URIs are relative to *https://api.bombbomb.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_contacts_csv**](ContactsApi.md#add_contacts_csv) | **POST** /contacts/import_csv | Add contacts from a CSV file.
[**add_new_contact**](ContactsApi.md#add_new_contact) | **POST** /contacts/ | Add a contact.
[**add_new_custom_field**](ContactsApi.md#add_new_custom_field) | **POST** /contacts/custom_fields/ | Add custom fields.
[**add_pasted_contacts**](ContactsApi.md#add_pasted_contacts) | **POST** /contacts/paste | Add pasted contacts.
[**c_sv_to_object**](ContactsApi.md#c_sv_to_object) | **POST** /csv-to-object | Format CSV.
[**delete_contacts**](ContactsApi.md#delete_contacts) | **PUT** /contacts/delete | Delete Contacts
[**get_contact_by_id**](ContactsApi.md#get_contact_by_id) | **GET** /contact/{id} | Get Contact Details
[**get_custom_fields**](ContactsApi.md#get_custom_fields) | **GET** /contacts/custom_fields/ | Get custom fields.


# **add_contacts_csv**
> add_contacts_csv(mapping_data, list_data)

Add contacts from a CSV file.

Add multiple contacts through the upload importer from a CSV file.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.ContactsApi()
mapping_data = 'mapping_data_example' # str | The info sent for the contacts
list_data = 'list_data_example' # str | The info sent with the import for the list

try: 
    # Add contacts from a CSV file.
    api_instance.add_contacts_csv(mapping_data, list_data)
except ApiException as e:
    print "Exception when calling ContactsApi->add_contacts_csv: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_data** | **str**| The info sent for the contacts | 
 **list_data** | **str**| The info sent with the import for the list | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_new_contact**
> add_new_contact(contact_email, contact_info=contact_info)

Add a contact.

Add a contact to the users list.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.ContactsApi()
contact_email = 'contact_email_example' # str | Email of the new contact we are adding
contact_info = 'contact_info_example' # str | The info sent for this contact (optional)

try: 
    # Add a contact.
    api_instance.add_new_contact(contact_email, contact_info=contact_info)
except ApiException as e:
    print "Exception when calling ContactsApi->add_new_contact: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_email** | **str**| Email of the new contact we are adding | 
 **contact_info** | **str**| The info sent for this contact | [optional] 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_new_custom_field**
> add_new_custom_field(field_name, field_type=field_type)

Add custom fields.

Add a new custom field.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.ContactsApi()
field_name = 'field_name_example' # str | Custom field name to be added
field_type = 'field_type_example' # str | Custom field type for the field to be added (optional)

try: 
    # Add custom fields.
    api_instance.add_new_custom_field(field_name, field_type=field_type)
except ApiException as e:
    print "Exception when calling ContactsApi->add_new_custom_field: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_name** | **str**| Custom field name to be added | 
 **field_type** | **str**| Custom field type for the field to be added | [optional] 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_pasted_contacts**
> add_pasted_contacts(contact_emails, list_info=list_info)

Add pasted contacts.

Add the pasted contacts to the users list.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.ContactsApi()
contact_emails = 'contact_emails_example' # str | Emails array of the new contacts we are adding
list_info = 'list_info_example' # str | Information about the lists id, recalculations on totals, consent etc (optional)

try: 
    # Add pasted contacts.
    api_instance.add_pasted_contacts(contact_emails, list_info=list_info)
except ApiException as e:
    print "Exception when calling ContactsApi->add_pasted_contacts: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_emails** | **str**| Emails array of the new contacts we are adding | 
 **list_info** | **str**| Information about the lists id, recalculations on totals, consent etc | [optional] 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **c_sv_to_object**
> c_sv_to_object(file)

Format CSV.

Format a CSV file to an object.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.ContactsApi()
file = 'file_example' # str | The CSV file being uploaded

try: 
    # Format CSV.
    api_instance.c_sv_to_object(file)
except ApiException as e:
    print "Exception when calling ContactsApi->c_sv_to_object: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**| The CSV file being uploaded | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contacts**
> delete_contacts(list_id)

Delete Contacts

Delete contacts

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.ContactsApi()
list_id = 'list_id_example' # str | The list of contacts to be deleted.

try: 
    # Delete Contacts
    api_instance.delete_contacts(list_id)
except ApiException as e:
    print "Exception when calling ContactsApi->delete_contacts: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_id** | **str**| The list of contacts to be deleted. | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_by_id**
> get_contact_by_id(id)

Get Contact Details

Get the contact details

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.ContactsApi()
id = 'id_example' # str | Guid for the contact.

try: 
    # Get Contact Details
    api_instance.get_contact_by_id(id)
except ApiException as e:
    print "Exception when calling ContactsApi->get_contact_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Guid for the contact. | 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_fields**
> get_custom_fields()

Get custom fields.

Get the current users custom fields.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.ContactsApi()

try: 
    # Get custom fields.
    api_instance.get_custom_fields()
except ApiException as e:
    print "Exception when calling ContactsApi->get_custom_fields: %s\n" % e
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

