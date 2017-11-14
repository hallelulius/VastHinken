# Leg

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fg_color** | **str** | Foregroundcolor of this line | [optional] 
**booking** | **bool** | Will be true if this journey needs to be booked | [optional] 
**direction** | **str** | Direction information | [optional] 
**journey_detail_ref** | [**JourneyDetailRef**](JourneyDetailRef.md) |  | [optional] 
**cancelled** | **bool** | Will be true if this journey is cancelled | [optional] 
**kcal** | **float** | Energy use | [optional] 
**origin** | [**Origin**](Origin.md) |  | [optional] 
**sname** | **str** | Short name of the leg | [optional] 
**type** | **str** | The attribute type specifies the type of the leg. Valid values are VAS, LDT (Long Distance Train), REG (Regional train), BUS , BOAT, TRAM, TAXI (Taxi/Telebus). Furthermore it can be of type WALK, BIKE and CAR if these legs are routes on the street network | 
**geometry_ref** | [**GeometryRef**](GeometryRef.md) |  | [optional] 
**bg_color** | **str** | Backgroundcolor of this line | [optional] 
**notes** | [**Notes**](Notes.md) |  | [optional] 
**id** | **str** | ID of the journey | [optional] 
**stroke** | **str** | Stroke style of this line | [optional] 
**reachable** | **bool** | Will be true if this journey is not reachable due to delay of the feeder | [optional] 
**name** | **str** | The attribute name specifies the name of the leg | 
**night** | **bool** | Will be true if this journey is a night journey | [optional] 
**destination** | [**Destination**](Destination.md) |  | [optional] 
**percent_bike_road** | **float** | Percentage of the route that is made up of bike roads | [optional] 
**accessibility** | **str** | will only be set if the vehicle has wheelchair + ramp/lift or lowfloor according to realtime data | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


