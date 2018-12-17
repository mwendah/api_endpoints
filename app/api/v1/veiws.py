from app.api.v1 import  ParcelModel
from flask_restful import Resource
from flask import response,jsonify,request

 class DataParcel(Resource)

def post(self)
Data=request.getjson()
if not Data
return jsonify{"message":"No data available"}
new_data=createparcel.parcel(data)
return jsonify{"message":"data created",
                "order":"[]"}


     def get(self)
     parcelorder=parcel_get_order()
                return jsonify{"message":" new data ",
                "order":"[]"

def put (self):
