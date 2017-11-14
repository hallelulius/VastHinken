# swagger_client.SysteminfoApi

All URIs are relative to *https://api.vasttrafik.se/bin/rest.exe/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_info**](SysteminfoApi.md#get_system_info) | **GET** /systeminfo | Provides information about the journey planner and the underlying data


# **get_system_info**
> SystemInfo get_system_info(format=format, jsonp_callback=jsonp_callback)

Provides information about the journey planner and the underlying data

Provides information about the journey planner and underlying data. It will return the begin of end of the timetable period and the creation date of the timetable data.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SysteminfoApi()
format = 'format_example' # str | the required response format (optional)
jsonp_callback = 'jsonp_callback_example' # str | If JSONP response format is needed, you can append an additional parameter to specify the name of a callback function, and the JSON object will be wrapped by a function call with this name. (optional)

try: 
    # Provides information about the journey planner and the underlying data
    api_response = api_instance.get_system_info(format=format, jsonp_callback=jsonp_callback)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SysteminfoApi->get_system_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| the required response format | [optional] 
 **jsonp_callback** | **str**| If JSONP response format is needed, you can append an additional parameter to specify the name of a callback function, and the JSON object will be wrapped by a function call with this name. | [optional] 

### Return type

[**SystemInfo**](SystemInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

