import unittest
import tempfile
from app import create_app
from ..api.v1.veiws  import DataParcel
from ..api.v1.models  import ParcelModel
import json

class TestParcelData(unittest.TestCase):
	def setup(self):
		self.app=create_app()
		self.client=self.app.test_client()
		self.app_context=self.app.app_context()
		self.app_context.push()

self.order={
    "id" : 1,
	 "destination" : "likoni",
	"recipient" : "mr C",
	"sender" : "mr.activer",
	"weight" : "23",
"status" : "activer"
        }


class  Test_Random(TestParcelData):
	def test_cancel_order(self):
		response=self.client.post('/parcel/cancel',data=json.dumps(self.data),content_type='application/json')
	    result=json.loads.response.data.decode()
	    self.assertEqual(result['message'],'parcel canceled',message'Error in test')
	    assert response.status_code==200


	

def test_get(self):
	response=self.client.get('/user/parcel',data=json.dumps(self.data),content_type='application/json')      	result=json.loads(response.data.decode())
    self.assertEqual(result['message'],'parcel found',message'Error in test')
    assert response.status_code==200

def test_put(self):
	response=self.client.get('/parcel',data=json.dumps(self.data),content_type='application/json')
    result=json.loads(response.data.decode())
    self.assertEqual(result['message'],'Hello mate',message'Error in test')
	assert response.status_code==400



if __name__=='__main__':
   unittest.main()	
