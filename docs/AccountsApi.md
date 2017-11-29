# bombbomb.AccountsApi

All URIs are relative to *https://api.bombbomb.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_details**](AccountsApi.md#account_details) | **GET** /accounts | Get account details.
[**create_account**](AccountsApi.md#create_account) | **POST** /accounts | Create Account
[**get_client_statistics**](AccountsApi.md#get_client_statistics) | **GET** /accounts/stats | Get Client Statistics
[**subscription_purchase_allowed**](AccountsApi.md#subscription_purchase_allowed) | **GET** /accounts/purchaseable | Check if subscription purchase allowed.


# **account_details**
> account_details()

Get account details.

Get the details of the user's account.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bombbomb.AccountsApi()

try: 
    # Get account details.
    api_instance.account_details()
except ApiException as e:
    print "Exception when calling AccountsApi->account_details: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_account**
> str create_account(team_id, first_name, last_name, email_address, company_name, phone, country=country, industry=industry, address=address, city=city, postal_code=postal_code, prevent_welcome_email=prevent_welcome_email)

Create Account

Creates a new BombBomb account. This method is currently only available to paid seat admins.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.AccountsApi()
team_id = 'team_id_example' # str | The team id
first_name = 'first_name_example' # str | First name of the user.
last_name = 'last_name_example' # str | Last name of the user.
email_address = 'email_address_example' # str | Email address of the user.
company_name = 'company_name_example' # str | Company of the user.
phone = 'phone_example' # str | Phone number of the user.
country = 'country_example' # str | Country of the user. (optional)
industry = 'industry_example' # str | Industry of the user. (optional)
address = 'address_example' # str | Street Address of the user. (optional)
city = 'city_example' # str | City of the user. (optional)
postal_code = 'postal_code_example' # str | Postal/Zip code of the user. (optional)
prevent_welcome_email = 'prevent_welcome_email_example' # str | prevent an email with login credentials from being sent to the new account. must be set to 'true' (optional)

try: 
    # Create Account
    api_response = api_instance.create_account(team_id, first_name, last_name, email_address, company_name, phone, country=country, industry=industry, address=address, city=city, postal_code=postal_code, prevent_welcome_email=prevent_welcome_email)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling AccountsApi->create_account: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The team id | 
 **first_name** | **str**| First name of the user. | 
 **last_name** | **str**| Last name of the user. | 
 **email_address** | **str**| Email address of the user. | 
 **company_name** | **str**| Company of the user. | 
 **phone** | **str**| Phone number of the user. | 
 **country** | **str**| Country of the user. | [optional] 
 **industry** | **str**| Industry of the user. | [optional] 
 **address** | **str**| Street Address of the user. | [optional] 
 **city** | **str**| City of the user. | [optional] 
 **postal_code** | **str**| Postal/Zip code of the user. | [optional] 
 **prevent_welcome_email** | **str**| prevent an email with login credentials from being sent to the new account. must be set to &#39;true&#39; | [optional] 

### Return type

**str**

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_statistics**
> get_client_statistics(client_id=client_id)

Get Client Statistics

Gets general statics for a Client

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: BBOAuth2
bombbomb.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = bombbomb.AccountsApi()
client_id = 'client_id_example' # str | Client ID of the account to retrieve. Defaults to yourself. (optional)

try: 
    # Get Client Statistics
    api_instance.get_client_statistics(client_id=client_id)
except ApiException as e:
    print "Exception when calling AccountsApi->get_client_statistics: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| Client ID of the account to retrieve. Defaults to yourself. | [optional] 

### Return type

void (empty response body)

### Authorization

[BBOAuth2](../README.md#BBOAuth2)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_purchase_allowed**
> subscription_purchase_allowed()

Check if subscription purchase allowed.

Check whether the user can purchase a subscription.

### Example 
```python
import time
import bombbomb
from bombbomb.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = bombbomb.AccountsApi()

try: 
    # Check if subscription purchase allowed.
    api_instance.subscription_purchase_allowed()
except ApiException as e:
    print "Exception when calling AccountsApi->subscription_purchase_allowed: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

