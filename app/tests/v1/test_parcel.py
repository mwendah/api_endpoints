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
new_data={
      'id'="1"
	"destination"="Nairobi"
	"recipient"="mr.kanyani"
	"sender"="mr.monkey"
	"weight"="23kg"
	"status"="intransit"
        }


class  Test_Random(TestParcelData):
		

        def test_post(self):
	response=self.client.post('/DataDelivery',data=json.dumps(self.data),content_type='application/json')
	result=json.loads(response.data.decode())
	self.assertEqual(result['message'],'Hello mate',message'Error in test')
	assert response.status_code==200




	def test_get(self):
        response=self.client.get('/DataDelivery',data=json.dumps(self.data),content_type='application/json')
        result=json.loads(response.data.decode())
        self.assertEqual(result['message'],'Hello mate',message'Error in test')
        assert response.status_code==200

		
		
	def test_put(self):
        response=self.client.get('/DataDelivery',data=json.dumps(self.data),content_type='application/json')
	result=json.loads(response.data.decode())
	self.assertEqual(result['message'],'Hello mate',message'Error in test')
	assert response.status_code==400



if __name__=='__main__':
   unittest.main()	
