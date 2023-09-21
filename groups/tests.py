from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User  # Assuming you're using Django's built-in User model
from .models import Group
from .serializers import GroupSerializer
from users.models import User
from rest_framework.test import APIClient

class GroupViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        # Sample data for creating a group
        self.group_data = {
            'title': 'Test Group'
            # Add other fields as needed
        }

    def test_create_group(self):
        url = '/api/groups/'  # Replace with the actual URL for creating groups

        # Send a POST request to create a group
        response = self.client.post(url, self.group_data, format='json')

        # Assert that the response status code is 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the group was created in the database
        self.assertEqual(Group.objects.count(), 1)

        # Check if the group's title matches the provided data
        self.assertEqual(Group.objects.get().title, 'Test Group')

        # Check if the group owner is the test user
        self.assertEqual(Group.objects.get().usergroups_set.first().user, self.user)

    def test_create_group_invalid_data(self):
        url = '/api/groups/'  # Replace with the actual URL for creating groups

        # Send a POST request with invalid data (missing required fields)
        invalid_data = {}
        response = self.client.post(url, invalid_data, format='json')

        # Assert that the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Check that the group was not created in the database
        self.assertEqual(Group.objects.count(), 0)
