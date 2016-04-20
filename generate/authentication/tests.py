#from django.core.urlresolvers import reverse
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory

from django.conf import settings

from models import User
from views import UserList

class CreateUserTest(APITestCase):
    def setup(self):
        self.superuser = User.objects.create_superuser('vishnu@vishnu.com', '1989-09-26', 'vishnupassword')
        self.client.login(username='vishnu', password='vishnupassword')
        self.data = {'email': 'test@gmail.com',
                     'date_of_birth': '1989-09-26',
                     'position': 1,
                     'meters': 1,
                     'minutes': 1,
                     'strokes': 1,
                     'metersAverage': 1,
                     'minutesAverage': 1,
                     'city_id': 1,
                     'name': 'Alexander',
                     'surname': 'The Great',
                     'trend': 'down',
                     'bio': None,
                     'password': '12346'
                     }

    def test_can_create_user(self):
        self.setup()
        self.token = Token.objects.get(user_id=self.superuser.id)
        self.api_key = settings.API_KEY
        self.factory = APIRequestFactory()
        self.response = self.client.post('/api/v1/users/?api_key=%s' % self.api_key, 
                                    self.data, 
                                    HTTP_AUTHORIZATION='Token {}'.format(self.token))
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
