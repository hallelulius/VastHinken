# Destination

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**route_idx** | **str** | Route index of a stop/station. Can be used as a reference of the stop/station in a journeyDetail response | [optional] 
**value** | **str** |  | 
**cancelled** | **bool** | Will be set to true if departure/arrival at this stop is cancelled | [optional] 
**track** | **str** | Track information, if available | [optional] 
**rt_track** | **str** | Realtime track information, if available | [optional] 
**type** | **str** | The attribute type specifies the type of location. Valid values are ST (stop/station), ADR (address) or POI (point of interest) | 
**date** | **date** | Date in format YYYY-MM-DD | 
**notes** | [**Notes**](Notes.md) |  | [optional] 
**id** | **str** | ID of this stop | 
**rt_date** | **date** | Realtime date in format YYYY-MM-DD, if available | [optional] 
**time** | **str** | Time in format HH:MM | 
**directdate** | **date** | Date in format YYYY-MM-DD.  Based on the direct travel time | [optional] 
**name** | **str** | Contains the name of the location | 
**rt_time** | **str** | Realtime time in format HH:MM if available | [optional] 
**directtime** | **str** | Direct Time format HH:MM. Based on the direct travel time | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


