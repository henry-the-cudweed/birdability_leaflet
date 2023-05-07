# birdability_reskin
Creating a leaflet version of the [birdability map](https://gis.audubon.org/birdability/). 


Note: all text displayed in **bold** is a data field, not data! Some of the data fields are written as statements, which I realize is confusing. If you see a bold sentence with no unbolded text underneath, that means there is no data on that topic.

Data accessed 5/3/2023 at [Esri API](https://services1.arcgis.com/lDFzr3JyGEn5Eymu/ArcGIS/rest/services/survey123_7b5a83ebc9044268a03b84ff9fe12c71_stakeholder/FeatureServer/0/query?where=1%3D1&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&relationParam=&returnGeodetic=false&outFields=*&returnGeometry=true&featureEncoding=esriDefault&multipatchOption=xyFootprint&maxAllowableOffset=&geometryPrecision=&outSR=&defaultSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnQueryGeometry=false&returnDistinctValues=false&cacheHint=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&sqlFormat=none&f=pjson&token=)

Goals:
1. ~~Add all data to sidebar~~
2. Filterable markers
3. ~~Make sidebar data visibility toggleable~~
4. Add map directions? 
5. Add photos (there are photos in the Esri map, but not in the json available at arcgis.com)
6. Add attributions 
7. Clean up the data in the sidebar (make special characters visible, make sure all questions are formatted clearly)
