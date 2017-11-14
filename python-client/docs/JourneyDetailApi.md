# swagger_client.JourneyDetailApi

All URIs are relative to *https://api.vasttrafik.se/bin/rest.exe/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_journey_detail**](JourneyDetailApi.md#get_journey_detail) | **GET** /journeyDetail | Returns information about the complete route of a trip.


# **get_journey_detail**
> JourneyDetail get_journey_detail(ref)

Returns information about the complete route of a trip.

Delivers information about the complete route of a trip. This service can not be called directly but only by reference URLs in a result of a trip or departureBoard request. It contains a list of all stops/stations of this journey including all departure and arrival times (with real-time data if available) and additional information like specific attributes about facilities and other texts.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.JourneyDetailApi()
ref = 'ref_example' # str | the ref query parameter, URL decoded, from a URL retrieved as a result of a trip or or departureBoard request

try: 
    # Returns information about the complete route of a trip.
    api_response = api_instance.get_journey_detail(ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JourneyDetailApi->get_journey_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref** | **str**| the ref query parameter, URL decoded, from a URL retrieved as a result of a trip or or departureBoard request | 

### Return type

[**JourneyDetail**](JourneyDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

