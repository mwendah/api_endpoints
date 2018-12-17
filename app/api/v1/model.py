from app.api.v1 import  parcel
from flask_restful import Resource
from flask import response,jsonify,request


class ParcelModel(object):
	def _init_(self)
	self.db=ParcelModel()


	def create_order(self,destination,recipient,sender,weight,status)
	self.destination=destination
	self.recipient=recipient
	self.sender=sender
	self.weight=weight
	self.status=status

	paylaod={

	"id":len(self.db)+1m
	"destination"=self.destination
	"recipient"=self.recipient
	"sender"=self.sender
	"weight"=self.weight
	"status"=self.status

	}

	parcel.parcels.append(payload)


def get_All(self):
	return self.db

   
	def get_single_parcel(self,id):
	res=self.db
	result=[result for  result in res if result['id']==str
  (id)]
     return result

  	def cancel_order(self,id)
  	res=self.db
  	result=[result for  result in res if result['id']==str
  (id)]
  result=result[0]
  result['status']=='terminated'

  def user_parcels(self,username):
  	res=self.db
  	result=[result for  result in res if result['username']==str
  (username)]
     return result
 




	
	
			
