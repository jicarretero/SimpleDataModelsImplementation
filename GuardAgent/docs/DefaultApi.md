# swagger_client.DefaultApi

All URIs are relative to *http://localhost/guard-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agents_get**](DefaultApi.md#agents_get) | **GET** /agents | Gets the information of an Agent
[**agents_id_delete**](DefaultApi.md#agents_id_delete) | **DELETE** /agents/{id} | Deletes (unregisters) the Agent from the CB
[**agents_id_get**](DefaultApi.md#agents_id_get) | **GET** /agents/{id} | Gets the properties of an agent.
[**agents_ping_id_put**](DefaultApi.md#agents_ping_id_put) | **PUT** /agents/ping/{id} | Puts a ping to GUARD Agent
[**agents_register_post**](DefaultApi.md#agents_register_post) | **POST** /agents/register | Post a new GUARD Agent


# **agents_get**
> GuardAgent agents_get(page_size=page_size)

Gets the information of an Agent

Gets a list of Agents and their security properites

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
page_size = 20 # int | Number of agents returned (optional) (default to 20)

try:
    # Gets the information of an Agent
    api_response = api_instance.agents_get(page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->agents_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| Number of agents returned | [optional] [default to 20]

### Return type

[**GuardAgent**](GuardAgent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agents_id_delete**
> agents_id_delete(id)

Deletes (unregisters) the Agent from the CB

Unsets the agent Security Properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | The ID of an already registered agent

try:
    # Deletes (unregisters) the Agent from the CB
    api_instance.agents_id_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->agents_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an already registered agent | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agents_id_get**
> GuardAgent agents_id_get(id)

Gets the properties of an agent.

Queries an agent

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | The ID of an already registered agent

try:
    # Gets the properties of an agent.
    api_response = api_instance.agents_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->agents_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an already registered agent | 

### Return type

[**GuardAgent**](GuardAgent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agents_ping_id_put**
> agents_ping_id_put(id)

Puts a ping to GUARD Agent

Sets a ping to the agent.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | The ID of an already registered agent

try:
    # Puts a ping to GUARD Agent
    api_instance.agents_ping_id_put(id)
except ApiException as e:
    print("Exception when calling DefaultApi->agents_ping_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an already registered agent | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agents_register_post**
> agents_register_post(agent=agent)

Post a new GUARD Agent

Sets the the agent Security Properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
agent = swagger_client.GuardAgent() # GuardAgent |  (optional)

try:
    # Post a new GUARD Agent
    api_instance.agents_register_post(agent=agent)
except ApiException as e:
    print("Exception when calling DefaultApi->agents_register_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent** | [**GuardAgent**](GuardAgent.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

