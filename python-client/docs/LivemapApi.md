# swagger_client.LivemapApi

All URIs are relative to *https://api.vasttrafik.se/bin/rest.exe/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**livemap**](LivemapApi.md#livemap) | **GET** /livemap | Returns the positions of all vehicles in a given bounding box


# **livemap**
> LiveMap livemap(minx, maxx, miny, maxy, only_realtime)

Returns the positions of all vehicles in a given bounding box

This method will return the positions of all vehicles in a given bounding box.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LivemapApi()
minx = 'minx_example' # str | Left border (longitude) of the bounding box in WGS84 * 1000000
maxx = 'maxx_example' # str | Right border (longitude) of the bounding box in WGS84 * 1000000
miny = 'miny_example' # str | Lower border (latitude) of the bounding box in WGS84 * 1000000
maxy = 'maxy_example' # str | Upper border (latitude) of the bounding box in WGS84 * 1000000
only_realtime = 'only_realtime_example' # str | Can be used to define whether all vehicles should be returned or only those  vehicles which have realtime information. If it is set to yes, only vehicles  with realtime information are returned, if it is set to no, all vehicles in the  bounding box are returned.

try: 
    # Returns the positions of all vehicles in a given bounding box
    api_response = api_instance.livemap(minx, maxx, miny, maxy, only_realtime)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LivemapApi->livemap: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minx** | **str**| Left border (longitude) of the bounding box in WGS84 * 1000000 | 
 **maxx** | **str**| Right border (longitude) of the bounding box in WGS84 * 1000000 | 
 **miny** | **str**| Lower border (latitude) of the bounding box in WGS84 * 1000000 | 
 **maxy** | **str**| Upper border (latitude) of the bounding box in WGS84 * 1000000 | 
 **only_realtime** | **str**| Can be used to define whether all vehicles should be returned or only those  vehicles which have realtime information. If it is set to yes, only vehicles  with realtime information are returned, if it is set to no, all vehicles in the  bounding box are returned. | 

### Return type

[**LiveMap**](LiveMap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

