# swagger_client.ArrivalBoardApi

All URIs are relative to *https://api.vasttrafik.se/bin/rest.exe/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_arrival_board**](ArrivalBoardApi.md#get_arrival_board) | **GET** /arrivalBoard | Return the next 20 arrivals (or less if not existing) from a given point in time or the next arrivals in a given timespan.


# **get_arrival_board**
> ArrivalBoard get_arrival_board(id, date, time, direction, use_vas=use_vas, use_ld_train=use_ld_train, use_reg_train=use_reg_train, use_bus=use_bus, use_boat=use_boat, use_tram=use_tram, exclude_dr=exclude_dr, time_span=time_span, max_departures_per_line=max_departures_per_line, need_journey_detail=need_journey_detail, format=format, jsonp_callback=jsonp_callback)

Return the next 20 arrivals (or less if not existing) from a given point in time or the next arrivals in a given timespan.

This method will return the next 20 arrivals (or less if not existing) from a given point in time or the next arrivals in a given timespan. The service can only be called for stops/stations by using according ID retrieved by the location method. The parameter is called id. The time and date are defined with the parameters date and time.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ArrivalBoardApi()
id = 789 # int | stop id
date = '2013-10-20' # date | the date
time = 'time_example' # str | the time in format HH:MM
direction = 789 # int | stop id in order to get only departures of vehicles with a specified direction
use_vas = 'use_vas_example' # str | to exclude trips with Västtågen, set this parameter to 0. (optional)
use_ld_train = 'use_ld_train_example' # str | to exclude trips with long distance trains, set this parameter to 0. (optional)
use_reg_train = 'use_reg_train_example' # str | to exclude trips with regional trains, set this parameter to 0. (optional)
use_bus = 'use_bus_example' # str | to exclude trips with buses, set this parameter to 0. (optional)
use_boat = 'use_boat_example' # str | to exclude trips with boats, set this parameter to 0. (optional)
use_tram = 'use_tram_example' # str | to exclude trips with trams, set this parameter to 0. (optional)
exclude_dr = 'exclude_dr_example' # str | to exclude journeys which require tel. registration, set this parameter to 0. (optional)
time_span = 56 # int | to get the next departures in a specified timespan of up to 24 hours (unit: minutes). If this parameter is not set, the result will contain the next 20 departures. (optional)
max_departures_per_line = 56 # int | if timeSpan is set you can further reduce the number of returned journeys by adding this parameter, which will cause only the given number of journeys for every combination of line and direction. (optional)
need_journey_detail = 'need_journey_detail_example' # str | if the reference URL for the journey detail service is not needed in the result, set this parameter to 0 (optional)
format = 'format_example' # str | the required response format (optional)
jsonp_callback = 'jsonp_callback_example' # str | If JSONP response format is needed, you can append an additional parameter to specify the name of a callback function, and the JSON object will be wrapped by a function call with this name. (optional)

try: 
    # Return the next 20 arrivals (or less if not existing) from a given point in time or the next arrivals in a given timespan.
    api_response = api_instance.get_arrival_board(id, date, time, direction, use_vas=use_vas, use_ld_train=use_ld_train, use_reg_train=use_reg_train, use_bus=use_bus, use_boat=use_boat, use_tram=use_tram, exclude_dr=exclude_dr, time_span=time_span, max_departures_per_line=max_departures_per_line, need_journey_detail=need_journey_detail, format=format, jsonp_callback=jsonp_callback)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ArrivalBoardApi->get_arrival_board: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| stop id | 
 **date** | **date**| the date | 
 **time** | **str**| the time in format HH:MM | 
 **direction** | **int**| stop id in order to get only departures of vehicles with a specified direction | 
 **use_vas** | **str**| to exclude trips with Västtågen, set this parameter to 0. | [optional] 
 **use_ld_train** | **str**| to exclude trips with long distance trains, set this parameter to 0. | [optional] 
 **use_reg_train** | **str**| to exclude trips with regional trains, set this parameter to 0. | [optional] 
 **use_bus** | **str**| to exclude trips with buses, set this parameter to 0. | [optional] 
 **use_boat** | **str**| to exclude trips with boats, set this parameter to 0. | [optional] 
 **use_tram** | **str**| to exclude trips with trams, set this parameter to 0. | [optional] 
 **exclude_dr** | **str**| to exclude journeys which require tel. registration, set this parameter to 0. | [optional] 
 **time_span** | **int**| to get the next departures in a specified timespan of up to 24 hours (unit: minutes). If this parameter is not set, the result will contain the next 20 departures. | [optional] 
 **max_departures_per_line** | **int**| if timeSpan is set you can further reduce the number of returned journeys by adding this parameter, which will cause only the given number of journeys for every combination of line and direction. | [optional] 
 **need_journey_detail** | **str**| if the reference URL for the journey detail service is not needed in the result, set this parameter to 0 | [optional] 
 **format** | **str**| the required response format | [optional] 
 **jsonp_callback** | **str**| If JSONP response format is needed, you can append an additional parameter to specify the name of a callback function, and the JSON object will be wrapped by a function call with this name. | [optional] 

### Return type

[**ArrivalBoard**](ArrivalBoard.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

