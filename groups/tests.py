from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Image, Group, UserGroups, GroupEvents, GroupImage
from users.models import User  # Import User model if it's defined in "users" app
from events.models import Event  # Import Event model if it's defined in "events" app
from .serializers import (
    ImageSerializer,
    GroupSerializer,
    UserGroupsSerializer,
    GroupEventsSerializer,
    GroupImageSerializer,
    
)

class ModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", password="testpassword")
        self.image = Image.objects.create(id="1", url="http://example.com/image.jpg")
        self.group = Group.objects.create(id="1", title="Test Group")
        self.event = Event.objects.create(id="1", title="Test Event")  # Import Event model if needed

    def test_image_model(self):
        image = Image.objects.get(id="1")
        self.assertEqual(image.url, "http://example.com/image.jpg")

    def test_group_model(self):
        group = Group.objects.get(id="1")
        self.assertEqual(group.title, "Test Group")

    def test_usergroups_model(self):
        usergroup = UserGroups.objects.create(user=self.user, group=self.group)
        self.assertEqual(usergroup.user, self.user)
        self.assertEqual(usergroup.group, self.group)

    def test_groupevents_model(self):
        groupevent = GroupEvents.objects.create(event=self.event, group=self.group)
        self.assertEqual(groupevent.event, self.event)
        self.assertEqual(groupevent.group, self.group)

    def test_groupimage_model(self):
        groupimage = GroupImage.objects.create(group=self.group, image=self.image)
        self.assertEqual(groupimage.group, self.group)
        self.assertEqual(groupimage.image, self.image)

class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username="testuser", password="testpassword")
        self.client.force_login(user=self.user)
        self.group_data = {"title": "Test Group"}

    def test_create_group(self):
        response = self.client.post("/api/groups/", self.group_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class SerializerTestCase(TestCase):
    def test_image_serializer(self):
        data = {"id": "1", "url": "http://example.com/image.jpg"}
        serializer = ImageSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_group_serializer(self):
        data = {"id": "1", "title": "Test Group"}
        serializer = GroupSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_usergroups_serializer(self):
        data = {"user": self.user.id, "group": self.group.id}
        serializer = UserGroupsSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_groupevents_serializer(self):
        data = {"event": self.event.id, "group": self.group.id}
        serializer = GroupEventsSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_groupimage_serializer(self):
        data = {"group": self.group.id, "image": self.image.id}
        serializer = GroupImageSerializer(data=data)
        self.assertTrue(serializer.is_valid())
