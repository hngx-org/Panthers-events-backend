# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase, APIRequestFactory
# from .models import Event, Comment, Image
# from .views import CreateEventAPIView, EventListAPIView


# # Create your tests here.
# class EventTestCase(APITestCase):
#     """ Test all http verbs for the event model """

#     def setUp(self):
#         """ Setup test context """
#         self.factory = APIRequestFactory()
#         self.view = EventListAPIView.as_view()
#         self.url = reverse("event-list")
        
    
#     def test_create_event(self):
#         f""" Testing get request for {self.url} endpoint """
#         # GENERATE REQUEST AND RESPONSE TO THE CREATE EVENT API
#         request = self.factory.get(self.url)
#         response = self.view(request)

#         # TEST CASE FOR THE CREATE EVENT ENDPOINT
#         self.assertEqual(response.data, [])
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

        
        