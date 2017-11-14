# swagger_client.LocationApi

All URIs are relative to *https://api.vasttrafik.se/bin/rest.exe/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_stops**](LocationApi.md#get_all_stops) | **GET** /location.allstops | Returns a list of all stops available in the journey planner.
[**get_location_by_name**](LocationApi.md#get_location_by_name) | **GET** /location.name | Returns a list of possible matches in the journey planner database
[**get_nearby_address**](LocationApi.md#get_nearby_address) | **GET** /location.nearbyaddress | Returns the address nearest a given coordinate.
[**get_nearby_stops**](LocationApi.md#get_nearby_stops) | **GET** /location.nearbystops | Returns a list of stops around a given center coordinate.


# **get_all_stops**
> LocationList get_all_stops(format=format, jsonp_callback=jsonp_callback)

Returns a list of all stops available in the journey planner.

Returns a list of all stops available in the journey planner. Be aware that a call of this service is very time consuming and should be only requested when it is really needed.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocationApi()
format = 'format_example' # str | the required response format (optional)
jsonp_callback = 'jsonp_callback_example' # str | If JSONP response format is needed, you can append an additional parameter to specify the name of a callback function, and the JSON object will be wrapped by a function call with this name. (optional)

try: 
    # Returns a list of all stops available in the journey planner.
    api_response = api_instance.get_all_stops(format=format, jsonp_callback=jsonp_callback)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationApi->get_all_stops: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| the required response format | [optional] 
 **jsonp_callback** | **str**| If JSONP response format is needed, you can append an additional parameter to specify the name of a callback function, and the JSON object will be wrapped by a function call with this name. | [optional] 

### Return type

[**LocationList**](LocationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location_by_name**
> LocationList get_location_by_name(input=input, format=format, jsonp_callback=jsonp_callback)

Returns a list of possible matches in the journey planner database

Performs a pattern matching of a user input to retrieve a list of possible matches in the journey planner database. Possible matches might be stops/stations, points of interest and addresses.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocationApi()
input = 'input_example' # str | a string with the user input (optional)
format = 'format_example' # str | the required response format (optional)
jsonp_callback = 'jsonp_callback_example' # str | If JSONP response format is needed, you can append an additional parameter to specify the name of a callback function, and the JSON object will be wrapped by a function call with this name. (optional)

try: 
    # Returns a list of possible matches in the journey planner database
    api_response = api_instance.get_location_by_name(input=input, format=format, jsonp_callback=jsonp_callback)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationApi->get_location_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | **str**| a string with the user input | [optional] 
 **format** | **str**| the required response format | [optional] 
 **jsonp_callback** | **str**| If JSONP response format is needed, you can append an additional parameter to specify the name of a callback function, and the JSON object will be wrapped by a function call with this name. | [optional] 

### Return type

[**LocationList**](LocationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nearby_address**
> LocationList get_nearby_address(origin_coord_lat, origin_coord_long, format=format, jsonp_callback=jsonp_callback)

Returns the address nearest a given coordinate.



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocationApi()
origin_coord_lat = 1.2 # float | latitude of coordinate in the WGS84 system
origin_coord_long = 1.2 # float | longitude of coordinate in the WGS84 system
format = 'format_example' # str | the required response format (optional)
jsonp_callback = 'jsonp_callback_example' # str | If JSONP response format is needed, you can append an additional parameter to specify the name of a callback function, and the JSON object will be wrapped by a function call with this name. (optional)

try: 
    # Returns the address nearest a given coordinate.
    api_response = api_instance.get_nearby_address(origin_coord_lat, origin_coord_long, format=format, jsonp_callback=jsonp_callback)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationApi->get_nearby_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin_coord_lat** | **float**| latitude of coordinate in the WGS84 system | 
 **origin_coord_long** | **float**| longitude of coordinate in the WGS84 system | 
 **format** | **str**| the required response format | [optional] 
 **jsonp_callback** | **str**| If JSONP response format is needed, you can append an additional parameter to specify the name of a callback function, and the JSON object will be wrapped by a function call with this name. | [optional] 

### Return type

[**LocationList**](LocationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nearby_stops**
> LocationList get_nearby_stops(origin_coord_lat, origin_coord_long, max_no=max_no, max_dist=max_dist, format=format, jsonp_callback=jsonp_callback)

Returns a list of stops around a given center coordinate.

Returns a list of stops around a given center coordinate. The returned results are ordered by their distance to the center coordinate.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LocationApi()
origin_coord_lat = 1.2 # float | latitude of center coordinate in the WGS84 system
origin_coord_long = 1.2 # float | longitude of center coordinate in the WGS84 system
max_no = 56 # int | maximum number of returned stops (optional)
max_dist = 56 # int | maximum distance from the center coordinate (optional)
format = 'format_example' # str | the required response format (optional)
jsonp_callback = 'jsonp_callback_example' # str | If JSONP response format is needed, you can append an additional parameter to specify the name of a callback function, and the JSON object will be wrapped by a function call with this name. (optional)

try: 
    # Returns a list of stops around a given center coordinate.
    api_response = api_instance.get_nearby_stops(origin_coord_lat, origin_coord_long, max_no=max_no, max_dist=max_dist, format=format, jsonp_callback=jsonp_callback)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationApi->get_nearby_stops: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **origin_coord_lat** | **float**| latitude of center coordinate in the WGS84 system | 
 **origin_coord_long** | **float**| longitude of center coordinate in the WGS84 system | 
 **max_no** | **int**| maximum number of returned stops | [optional] 
 **max_dist** | **int**| maximum distance from the center coordinate | [optional] 
 **format** | **str**| the required response format | [optional] 
 **jsonp_callback** | **str**| If JSONP response format is needed, you can append an additional parameter to specify the name of a callback function, and the JSON object will be wrapped by a function call with this name. | [optional] 

### Return type

[**LocationList**](LocationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

