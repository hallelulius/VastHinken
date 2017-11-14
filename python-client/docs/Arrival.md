# Arrival

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fg_color** | **str** | Foregroundcolor of this line | 
**stop** | **str** | Contains the name of the stop/station | 
**booking** | **bool** | Will be true if this journey needs to be booked | [optional] 
**journey_detail_ref** | [**JourneyDetailRef**](JourneyDetailRef.md) |  | 
**origin** | **str** | Origin of the journey | 
**track** | **str** | Track information, if available | 
**rt_track** | **str** | Realtime track information, if available | [optional] 
**sname** | **str** | Short name of the leg | 
**type** | **str** | The attribute type specifies the type of the arriving journey. Valid values are VAS, LDT (Long Distance Train), REG (Regional train), BUS , BOAT, TRAM, TAXI (Taxi/Telebus) | 
**date** | **date** | Date in format YYYY-MM-DD | 
**bg_color** | **str** | Backgroundcolor of this line | 
**stroke** | **str** | Stroke style of this line | 
**rt_date** | **date** | Realtime date in format YYYY-MM-DD, if available | 
**time** | **str** | Time in format HH:MM | 
**name** | **str** | The attribute name specifies the name of the arriving journey | 
**rt_time** | **str** | Realtime time in format HH:MM if available | 
**night** | **bool** | Will be true if this journey is a night journey | [optional] 
**stopid** | **str** | Contains the id of the stop/station | 
**journeyid** | **str** | Contains the id of the journey | 
**accessibility** | **str** | will only be set if the vehicle has wheelchair + ramp/lift or lowfloor according to realtime data | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


