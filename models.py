from django.db import models


class CommentImages(models.Model):
    comment = models.OneToOneField('Comments', models.DO_NOTHING, primary_key=True)  # The composite primary key (comment_id, image_id) found, that is not supported. The first column is selected.
    image = models.ForeignKey('Images', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'comment_images'
        unique_together = (('comment', 'image'),)


class Comments(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    body = models.TextField(blank=True, null=True)
    event = models.ForeignKey('Events', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comments'


class EventThumbnail(models.Model):
    image = models.OneToOneField('Images', models.DO_NOTHING, primary_key=True)  # The composite primary key (image_id, event_id) found, that is not supported. The first column is selected.
    event = models.ForeignKey('Events', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'event_thumbnail'
        unique_together = (('image', 'event'),)


class Events(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    creator = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'


class GroupEvents(models.Model):
    group = models.OneToOneField('Groups', models.DO_NOTHING, primary_key=True)  # The composite primary key (group_id, event_id) found, that is not supported. The first column is selected.
    event = models.ForeignKey(Events, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'group_events'
        unique_together = (('group', 'event'),)


class GroupImage(models.Model):
    group = models.OneToOneField('Groups', models.DO_NOTHING, primary_key=True)  # The composite primary key (group_id, image_id) found, that is not supported. The first column is selected.
    image = models.ForeignKey('Images', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'group_image'
        unique_together = (('group', 'image'),)


class Groups(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    title = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groups'


class Images(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    url = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'images'


class InterestedEvents(models.Model):
    event = models.OneToOneField(Events, models.DO_NOTHING, primary_key=True)  # The composite primary key (event_id, user_id) found, that is not supported. The first column is selected.
    user = models.ForeignKey('Users', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'interested_events'
        unique_together = (('event', 'user'),)


class Likes(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, comment_id) found, that is not supported. The first column is selected.
    comment = models.ForeignKey(Comments, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'likes'
        unique_together = (('user', 'comment'),)


class UserGroups(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, group_id) found, that is not supported. The first column is selected.
    group = models.ForeignKey(Groups, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_groups'
        unique_together = (('user', 'group'),)


class Users(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    avatar = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
