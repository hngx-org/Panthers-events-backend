# from django.test import TestCase
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APIClient
# from .models import Image, Group, UserGroups, GroupEvents, GroupImage
# from .serializers import (
#     ImageSerializer,
#     GroupSerializer,
#     UserGroupsSerializer,
#     GroupEventsSerializer,
#     GroupImageSerializer,
    
# )
# from users.models import User  # Import your User model here
# from events.models import Event  # Import your Event model here

# class ImageTests(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create(username='testuser', password='testpassword')
#         self.client.force_authenticate(user=self.user)
#         self.image_data = {'url': 'https://example.com/image.jpg'}
#         self.image = Image.objects.create(url=self.image_data['url'])

#     def test_create_image(self):
#         response = self.client.post(reverse('image-list'), self.image_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_get_image_list(self):
#         response = self.client.get(reverse('image-list'))
#         images = Image.objects.all()
#         serializer = ImageSerializer(images, many=True)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_get_image_detail(self):
#         response = self.client.get(reverse('image-detail', args=[str(self.image.id)]))
#         image = Image.objects.get(pk=self.image.id)
#         serializer = ImageSerializer(image)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_update_image(self):
#         updated_data = {'url': 'https://example.com/updated-image.jpg'}
#         response = self.client.put(reverse('image-detail', args=[str(self.image.id)]), updated_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.image.refresh_from_db()
#         self.assertEqual(self.image.url, updated_data['url'])

#     def test_delete_image(self):
#         response = self.client.delete(reverse('image-detail', args=[str(self.image.id)]))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(Image.objects.filter(pk=self.image.id).exists())

# class GroupTests(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create(username='testuser', password='testpassword')
#         self.client.force_authenticate(user=self.user)
#         self.group_data = {'title': 'Test Group', 'creator_id': self.user.id}
#         self.group = Group.objects.create(title=self.group_data['title'], creator_id=self.user.id)

#     def test_create_group(self):
#         response = self.client.post(reverse('group-list'), self.group_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_get_group_list(self):
#         response = self.client.get(reverse('group-list'))
#         groups = Group.objects.all()
#         serializer = GroupSerializer(groups, many=True)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_get_group_detail(self):
#         response = self.client.get(reverse('group-detail', args=[str(self.group.id)]))
#         group = Group.objects.get(pk=self.group.id)
#         serializer = GroupSerializer(group)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_update_group(self):
#         updated_data = {'title': 'Updated Test Group'}
#         response = self.client.put(reverse('group-detail', args=[str(self.group.id)]), updated_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.group.refresh_from_db()
#         self.assertEqual(self.group.title, updated_data['title'])

#     def test_delete_group(self):
#         response = self.client.delete(reverse('group-detail', args=[str(self.group.id)]))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(Group.objects.filter(pk=self.group.id).exists())

# class ViewTestCase(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create(username='testuser', password='testpassword')
#         self.client.force_authenticate(user=self.user)
#         self.group_data = {'title': 'Test Group', 'creator_id': self.user.id}
#         self.group = Group.objects.create(title=self.group_data['title'], creator_id=self.user.id)

#     def test_create_group(self):
#         response = self.client.post(reverse('group-list'), self.group_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_get_group_list(self):
#         response = self.client.get(reverse('group-list'))
#         groups = Group.objects.all()
#         serializer = GroupSerializer(groups, many=True)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_get_group_detail(self):
#         response = self.client.get(reverse('group-detail', args=[str(self.group.id)]))
#         group = Group.objects.get(pk=self.group.id)
#         serializer = GroupSerializer(group)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_update_group(self):
#         updated_data = {'title': 'Updated Test Group'}
#         response = self.client.put(reverse('group-detail', args=[str(self.group.id)]), updated_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.group.refresh_from_db()
#         self.assertEqual(self.group.title, updated_data['title'])

#     def test_delete_group(self):
#         response = self.client.delete(reverse('group-detail', args=[str(self.group.id)]))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(Group.objects.filter(pk=self.group.id).exists())


# class UserGroupsTests(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create(username='testuser', password='testpassword')
#         self.client.force_authenticate(user=self.user)
        
#         # Create a test group
#         self.group_data = {'title': 'Test Group', 'creator_id': self.user.id}
#         self.group = Group.objects.create(title=self.group_data['title'], creator_id=self.user.id)
        
#         # Create a UserGroups instance
#         self.user_groups_data = {'user': self.user.id, 'group': self.group.id}
#         self.user_groups = UserGroups.objects.create(user=self.user, group=self.group)

#     def test_create_user_group(self):
#         response = self.client.post(reverse('usergroups-list'), self.user_groups_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_get_user_group_list(self):
#         response = self.client.get(reverse('usergroups-list'))
#         user_groups = UserGroups.objects.all()
#         serializer = UserGroupsSerializer(user_groups, many=True)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_get_user_group_detail(self):
#         response = self.client.get(reverse('usergroups-detail', args=[str(self.user_groups.id)]))
#         user_group = UserGroups.objects.get(pk=self.user_groups.id)
#         serializer = UserGroupsSerializer(user_group)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_update_user_group(self):
#         updated_data = {'user': self.user.id, 'group': self.group.id}
#         response = self.client.put(reverse('usergroups-detail', args=[str(self.user_groups.id)]), updated_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.user_groups.refresh_from_db()
#         self.assertEqual(self.user_groups.user.id, updated_data['user'])
#         self.assertEqual(self.user_groups.group.id, updated_data['group'])

#     def test_delete_user_group(self):
#         response = self.client.delete(reverse('usergroups-detail', args=[str(self.user_groups.id)]))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(UserGroups.objects.filter(pk=self.user_groups.id).exists())

# class GroupEventsTests(TestCase):
#     def setUp(self):
#         self.client = APIClient()

#         # Create a test user
#         self.user_data = {'username': 'testuser', 'password': 'testpassword'}
#         self.user = User.objects.create_user(**self.user_data)
#         self.client.force_authenticate(user=self.user)

#         # Create a test group
#         self.group_data = {'title': 'Test Group', 'creator_id': self.user.id}
#         self.group = Group.objects.create(title=self.group_data['title'], creator_id=self.user.id)

#         # Create a test event
#         self.event_data = {'name': 'Test Event', 'description': 'Event Description'}
#         self.event = Event.objects.create(**self.event_data)

#         # Create a GroupEvents instance
#         self.group_events_data = {'group': self.group.id, 'event': self.event.id}
#         self.group_events = GroupEvents.objects.create(group=self.group, event=self.event)

#     def test_create_group_event(self):
#         response = self.client.post(reverse('groupevents-list'), self.group_events_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_get_group_event_list(self):
#         response = self.client.get(reverse('groupevents-list'))
#         group_events = GroupEvents.objects.all()
#         serializer = GroupEventsSerializer(group_events, many=True)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_get_group_event_detail(self):
#         response = self.client.get(reverse('groupevents-detail', args=[str(self.group_events.id)]))
#         group_event = GroupEvents.objects.get(pk=self.group_events.id)
#         serializer = GroupEventsSerializer(group_event)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_update_group_event(self):
#         updated_data = {'group': self.group.id, 'event': self.event.id}
#         response = self.client.put(reverse('groupevents-detail', args=[str(self.group_events.id)]), updated_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.group_events.refresh_from_db()
#         self.assertEqual(self.group_events.group.id, updated_data['group'])
#         self.assertEqual(self.group_events.event.id, updated_data['event'])

#     def test_delete_group_event(self):
#         response = self.client.delete(reverse('groupevents-detail', args=[str(self.group_events.id)]))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(GroupEvents.objects.filter(pk=self.group_events.id).exists())

# class GroupImageTests(TestCase):
#     def setUp(self):
#         self.client = APIClient()

#         # Create a test user
#         self.user_data = {'username': 'testuser', 'password': 'testpassword'}
#         self.user = User.objects.create_user(**self.user_data)
#         self.client.force_authenticate(user=self.user)

#         # Create a test group
#         self.group_data = {'title': 'Test Group', 'creator_id': self.user.id}
#         self.group = Group.objects.create(title=self.group_data['title'], creator_id=self.user.id)

#         # Create a test image
#         self.image_data = {'url': 'https://example.com/image.jpg'}
#         self.image = Image.objects.create(**self.image_data)

#         # Create a GroupImage instance
#         self.group_image_data = {'group': self.group.id, 'image': self.image.id}
#         self.group_image = GroupImage.objects.create(group=self.group, image=self.image)

#     def test_create_group_image(self):
#         response = self.client.post(reverse('groupimages-list'), self.group_image_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_get_group_image_list(self):
#         response = self.client.get(reverse('groupimages-list'))
#         group_images = GroupImage.objects.all()
#         serializer = GroupImageSerializer(group_images, many=True)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_get_group_image_detail(self):
#         response = self.client.get(reverse('groupimages-detail', args=[str(self.group_image.id)]))
#         group_image = GroupImage.objects.get(pk=self.group_image.id)
#         serializer = GroupImageSerializer(group_image)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_update_group_image(self):
#         updated_data = {'group': self.group.id, 'image': self.image.id}
#         response = self.client.put(reverse('groupimages-detail', args=[str(self.group_image.id)]), updated_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.group_image.refresh_from_db()
#         self.assertEqual(self.group_image.group.id, updated_data['group'])
#         self.assertEqual(self.group_image.image.id, updated_data['image'])

#     def test_delete_group_image(self):
#         response = self.client.delete(reverse('groupimages-detail', args=[str(self.group_image.id)]))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertFalse(GroupImage.objects.filter(pk=self.group_image.id).exists())
