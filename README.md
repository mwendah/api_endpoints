# api_endpoints.


#Create a parcel delivery order
#Get all parcel delivery orders
#Get a specific parcel delivery order
#Cancel a parcel delivery order


       
EndPoint  Functionality
GET /parcels
Fetch all parcel delivery orders
GET /parcels/<parcelId>
Fetch a specific parcel delivery order
GET /users/<userId>/parcels
Fetch all parcel delivery orders by a specific user
PUT /parcels/<parcelId>/cancel
Cancel the specific parcel delivery order
POST /parcels
Create a parcel delivery order
