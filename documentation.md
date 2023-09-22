# WetinDeySup API Documentation

- *Required Parameter

## Table of Content

- [User](#user)
  - [`/user/`](###`/user/`)
  - [`/user/{id}/`](###`/user/{id}/`)


- [Events](#events)
  - [`/api/events/`](###`/api/events/`)
  - [`/api/events/`](#get-all-events)
  - [`/api/events/{id}/`](###`/api/events/{id}/`)
  - [`/api/events/{id}/`](#update-an-event)

- [Groups](#groups)
  - [`/groups/`](###`/groups/`)
  - [`/groups/`](`##/groups/`)
  - [`/groups/{id}/`](#get-a-group-by-id)
  - [`/groups/{id}/`](###`/groups/{id}/`)
  - [`/groups/{id}/`](#delete-a-group-by-id)

- [Group Images](#group-images)
  - [`/group-images/`](###`/group-images/`)
  - [`/group-images/{id}/`](#get-a-group-image)
  - [`/group-images/{id}/`](#update-a-group-image)
  - [`/group-images/{id}/`](#delete-a-group-image)

- [Group Events](#group-events)
  - [`/groupevents/`](#create-a-group-event)
  - [`/groupevents/`](#get-all-group-events)
  - [`/groupevents/{id}/`](###`/group-images/{id}/`)
  - [`/groupevents/{id}/`](###`/group-images/{id}/`)
  - [`/groupevents/{id}/`](#delete-a-group-event-by-id)

- [Likes](#likes)
  - [`/likes/`](###`/likes/`)
  - [`/likes/`](#get-all-likes-on-a-comment)

- [Usage Examples](##Usage Examples)
  - [Events](##events)
  - [Groups](##groups)
  - [Group Images](##group-images)
  - [Group Events](##GROUP EVENTS)
  - [Images](##images)
  - [User Groups](##user-groups)

## USER

### `/user/`

Create a user.

**HTTP Method:** POST

### Parameters


  **body**


- `name*` (string): The name of the user
- `email*`(string): Email of the user
- `avatar` (string): url to avatar file

### Response

The API will respond with a JSON object containing the following fields:

- `id` : id of the user
- `name*` (string): The name of the user
- `email*`(string): Email of the user
- `created_at`: (time): The time the group was created(e.g., "HH:MM AM/PM").
- `avatar` (string): url to avatar file

### `/user/`

Get all users.

**HTTP Method:** GET

### Parameters


 None


### Response

The API will respond with a JSON object containing a list of the following fields:

- `id` : id of the user
- `name*` (string): The name of the user
- `email*`(string): Email of the user
- `created_at`: (time): The time the group was created(e.g., "HH:MM AM/PM").
- `avatar` (string): url to avatar file

### `/user/{id}/`

Get a user by id.

**HTTP Method:** GET

### Parameters


 **path**


- `id*` : A unique value identifying this user.

### Response

The API will respond with a JSON object containing the following fields:

- `id` : id of the user
- `name*` (string): The name of the user
- `email*`(string): Email of the user
- `created_at`: (time): The time the group was created(e.g., "HH:MM AM/PM").
- `avatar` (string): url to avatar file

### `/user/{id}/`

Update a user by id.

**HTTP Method:** PUT

### Parameters


 **path**


- `id*` : A unique value identifying this user.

### Response

The API will respond with a JSON object containing the following fields:

- `id` : id of the user
- `name*` (string): The name of the user
- `email*`(string): Email of the user
- `created_at`: (time): The time the group was created(e.g., "HH:MM AM/PM").
- `avatar` (string): url to avatar file

## EVENTS

### `/api/events/`

Create an event.

**HTTP Method:** POST

### Parameters


   **body**


- **`title` ***(string): The title of the event.
- **`description`** (string): A brief description of the event.
- **`location` ***(string): The location where the event will take place.
- **`start_date` ***(date): The date on which the event starts (e.g., "YYYY-MM-DD").
- **`end_date` ***(date): The date on which the event ends (e.g., "YYYY-MM-DD").
- **`start_time` ***(time): The time at which the event starts (e.g., "HH:MM AM/PM").
- **`end_time` ***(time): The time at which the event ends (e.g., "HH:MM AM/PM").
- **`thumbnail` ***(file): An image or thumbnail for the event.
- **`creator` ***(string): The name or identifier of the event creator.

### Response

The API will respond with a JSON object containing the following fields:

- `id` : id of the event
- **`title`**(string): The title of the event.
- **`description`** (string): A brief description of the event.
- **`location`**(string): The location where the event will take place.
- **`start_date`**(date): The date on which the event starts (e.g., "YYYY-MM-DD").
- **`end_date`**(date): The date on which the event ends (e.g., "YYYY-MM-DD").
- **`start_time`**(time): The time at which the event starts (e.g., "HH:MM AM/PM").
- **`end_time`**(time): The time at which the event ends (e.g., "HH:MM AM/PM").
- **`thumbnail`**(file): An image or thumbnail for the event.
- **`creator`**(string): The name or identifier of the event creator.

### `/api/events/`

Get all events.

**HTTP Method:** Get

### Parameters

- None

### Response

The API will respond with a JSON object containing a list the following fields:

- `id` : id of the event
- **`title`**(string): The title of the event.
- **`description`** (string): A brief description of the event.
- **`location`**(string): The location where the event will take place.
- **`start_date`**(date): The date on which the event starts (e.g., "YYYY-MM-DD").
- **`end_date`**(date): The date on which the event ends (e.g., "YYYY-MM-DD").
- **`start_time`**(time): The time at which the event starts (e.g., "HH:MM AM/PM").
- **`end_time`**(time): The time at which the event ends (e.g., "HH:MM AM/PM").
- **`thumbnail`**(file): An image or thumbnail for the event.
- **`creator`**(string): The name or identifier of the event creator.

### `/api/events/{id}/`

Get a particular event by id.

**HTTP Method:** Get

### Parameters

**Path**

- `id` : A unique integer value identifying this event.

### Response

The API will respond with a JSON object containing a list the following fields:

- `id` : id of the event
- **`title`**(string): The title of the event.
- **`description`** (string): A brief description of the event.
- **`location`**(string): The location where the event will take place.
- **`start_date`**(date): The date on which the event starts (e.g., "YYYY-MM-DD").
- **`end_date`**(date): The date on which the event ends (e.g., "YYYY-MM-DD").
- **`start_time`**(time): The time at which the event starts (e.g., "HH:MM AM/PM").
- **`end_time`**(time): The time at which the event ends (e.g., "HH:MM AM/PM").
- **`thumbnail`**(file): An image or thumbnail for the event.
- **`creator`**(string): The name or identifier of the event creator.

## GROUPS

### `/groups/`

Create a group.

**HTTP Method:** POST

### Parameters

   **body**
- `title*` : A unique identifying the group
- `ceator_id*` : A unique identifier for the creator

### Response

The API will respond with a JSON object containing the following fields:

- `id` : id of group
- `title` : (string) The group name
- `created_at`: (time): The time the group was created(e.g., "HH:MM AM/PM").
- `creator_id` : (string): The name or identifier of the event creator.

### `/groups/`

Get all group.

**HTTP Method:** GET

### Parameters

  None

### Response

The API will respond with a JSON object containing a list of the following fields:

- `id` : id of group
- `title` : (string) The group name
- `created_at`: (time): The time the group was created(e.g., "HH:MM AM/PM").
- `creator_id` : (string): The name or identifier of the event creator.

### `/groups/{id}/`

Get a group by id.

**HTTP Method:** GET

### Parameters

   **path**
- `id*` (string): A unique value identifying this group.

### Response

The API will respond with a JSON object containing the following fields:

- `id` : id of group
- `title` : (string) The group name
- `created_at`: (time): The time the group was created(e.g., "HH:MM AM/PM").
- `creator_id` : (string): The name or identifier of the event creator.

### `/groups/{id}/`

Update a group by id.

**HTTP Method:** PUT

### Parameters

   **path**
- `id*` (string): A unique value identifying this group.
    
    **body**
    
- `title*` : A unique identifying the group
    
- `ceator_id*` : A unique identifier for the creator
    

### `/groups/{id}/`

Delete a group by id.

**HTTP Method:** DELETE

### Parameters

  **Path**
- `id*` (string): A unique value identifying this group.

### Response

The API will respond with a JSON object containing the following fields:

- `id` : id of group
- `title` : The group name
- `message` : Success on deletion

### Response

The API will respond with a JSON object containing the following fields:

- `id` : id of group
- `title` : (string) The group name
- `created_at`: (time): The time the group was created(e.g., "HH:MM AM/PM").
- `creator_id` : (string): The name or identifier of the event creator.

## GROUP-IMAGES

### `/group-images/`

Add a group image.

**HTTP Method:** POST

### Parameters

   **body**

- `group*` : A unique identifying the group
- `image*` (file): Group image file

### Response

The API will respond with a JSON object containing the following fields:

- `id` : id of group image
- `group` : The group name
- `image` (url): The group image

### `/group-images/{id}/`

Get a group image.

**HTTP Method:** Get

### Parameters

   **Path**

- `id` *: A unique integer value identifying this group image.

### Response

The API will respond with a JSON object containing the following fields:

- `id` : id of group image
- `group` : The group name
- `image` (url): The group image

### `/group-images/{id}/`

Update a group image.

**HTTP Method:** PUT

### Parameters

  **Path**
- `id` *: A unique integer value identifying this group image.
    
    **body**
    
- `group*` : A unique identifying the group
    
- `image*` (file): Group image file
    

### Response

The API will respond with a JSON object containing the following fields:

- `id` : id of group image
- `group` : The group name
- `image` (url): The group image

### `/group-images/{id}/`

Delete a group image.

**HTTP Method:** DELETE

### Parameters

  **Path**
- `id*` : A unique integer value identifying this group image.

### Response

The API will respond with a JSON object containing the following fields:

- `id` : id of group image

### `/groupevents/`

Create a group event.

**HTTP Method:** POST

### Parameters

   **body**
- `event*` (integer): A unique value identifying the event
- `group*` (string): A unique value identifying the group

### Response

The API will respond with a JSON object containing the following fields:

- `id` : id of group event
- `event` (integer): id of event
- `group`: (string): id of th group.

## GROUP EVENTS

### `/groupevents/`

Get all group events.

**HTTP Method:** GET

### Parameters

- None

### Response

The API will respond with a JSON object containing a list of the following fields:

- `id` : id of group event
- `event` (integer): id of event
- `group`: (string): id of th group.

### `/groupevents/{id}/`

Get a group event by id.

**HTTP Method:** GET

### Parameters

   path

- `id*` (integer): A unique value identifying this group events

### Response

The API will respond with a JSON object containing the following fields:

- `id` : id of group event
- `event` (integer): id of event
- `group`: (string): id of the group.

### `/groupevents/{id}/`

Update a group event by id.

**HTTP Method:** Update

### Parameters

   **path**

- `id*` (integer): A unique value identifying this group events
    
    **body**
    
- `event*` (integer): A unique value identifying the event
    
- `group*` (string): A unique value identifying the group
    

### Response

The API will respond with a JSON object containing the following fields:

- `id` : id of group event
- `event` (integer): id of event
- `group`: (string): id of the group.

### `/groupevents/{id}/`

Delete a group event by id.

**HTTP Method:** GET

### Parameters

   **path**

- `id*` (integer): A unique value identifying this group events

### Response

The API will respond with a JSON object containing the following fields:

- `id` : id of group event
- `event` (integer): id of event
- `group`: (string): id of the group.

## LIKES

### `/likes/`

Like a comment.

**HTTP Method:** POST

### Parameters

 **body**
- `comment*`(string): The id of the comment

### Response

The API will respond with a JSON object containing the following fields:

- `id` (integer): Like id
    
    **User**
    
- `id` : id of the user
    
- `name*` (string): The name of the user
    
- `email*`(string): Email of the user
    
- `created_at`: (time): The time the group was created(e.g., "HH:MM AM/PM").
    
- `avatar` (string): url to avatar file
    
    **Comment**
    
- `id` : id of the comment
    
- `body` (string): comment body
    
- `creator` (string): id of the creator
    
- `event` (integer): Event id
    

### `/likes/`

Get all the likes on a comment.

**HTTP Method:** GET

### Parameters

- None

### Response

The API will respond with a JSON object containing the following fields:

- `id` (integer): Like id
    
    **User**
    
- `id` : id of the user
    
- `name*` (string): The name of the user
    
- `email*`(string): Email of the user
    
- `created_at`: (time): The time the group was created(e.g., "HH:MM AM/PM").
    
- `avatar` (string): url to avatar file
    
    **Comment**
    
- `id` : id of the comment
    
- `body` (string): comment body
    
- `creator` (string): id of the creator
    
- `event` (integer): Event id
    

## Usage Examples

The following examples demonstrate the usage of the WetinDeySup API.

## User

### Get All Users

Retrieve all users from the API.

```
GET /api/user/

```

Example Response:

```json
[
	{
		"id": 1,
		"name": "John Doe",
		"email": "john@mail.com",
		"avatar": "https://example.com/avatar.jpg",
		"created_at": "2023-09-22T08:54:32.156734Z",
		"updated_at": "2023-09-22T08:54:32.156776Z"
	},
	{
		"id": 2,
		"name": "James Smith",
		"email": "james@mail.com",
		"avatar": "https://example.com/avatar-2.jpg",
		"created_at": "2023-09-22T10:48:21.929635Z",
		"updated_at": "2023-09-22T10:48:21.929667Z"
	},
  ...
]

```

### Get User Details

Retrieve details of a specific user by its ID.

```
GET /api/user/{user_id}/

```

Example Response:

```json
{
	"id": 2,
	"name": "James Smith",
	"email": "james@mail.com",
	"avatar": "https://example.com/avatar-2.jpg",
	"created_at": "2023-09-22T10:48:21.929635Z",
	"updated_at": "2023-09-22T10:48:21.929667Z"
}

```

### Create a User

Create a new user by providing the required parameters.

```
POST /api/events/

Request Body:
	{
		"name": "New User",
		"email": "newuser@mail.com",
		"avatar": "https://example.com/avatar-3.jpg",
	}

```

Example Response:

```json
{
	"id": 3,
	"name": "New User",
	"email": "newuser@mail.com",
	"avatar": "https://example.com/avatar-3.jpg",
	"created_at": "2023-09-23T10:48:21.929635Z",
	"updated_at": "2023-09-23T10:48:21.929635Z"
}

```

### Update a User

Update the details of an existing user by its ID.

```
PUT /api/user/{user_id}/

Request Body:
	{
		"name": "Updated User",
		"email": "updateduser@mail.com",
		"avatar": "https://example.com/avatar-3.jpg",
	}

```

Example Response:

```json
{
	"id": 3,
	"name": "Updated User",
	"email": "updateduser@mail.com",
	"avatar": "https://example.com/avatar-3.jpg",
	"created_at": "2023-09-23T10:48:21.929635Z",
	"updated_at": "2023-09-23T10:48:21.929667Z"
}

```


## Events

### Get All Events

Retrieve all events from the API.

```
GET /api/events/

```

Example Response:

```json
[
	{
		"id": 1,
		"title": "Django Confrence",
		"description": "Join us for a keynote speech on saturday!",
		"location": "123 Main Street, Gotham",
		"start_date": "2023-09-24",
		"end_date": "2023-09-24",
		"start_time": "3:00 PM",
		"end_time": "5:00 PM",
		"thumbnail": "<https://example.com/thumbnail-party.jpg>",
		"creator": "John Doe"
	},
	{
		"id": 2,
		"title": "Gaming Tournament",
		"description": "Compete in a gaming tournament with cash prizes.",
		"location": "Cillian Bookstore, Main Street",
		"start_date": "2023-09-26",
		"end_date": "2023-09-26",
		"start_time": "5:00 PM",
		"end_time": "9:00 PM",
		"thumbnail": "<https://example.com/gaming-tournament-thumbnail.jpg>",
		"creator": "James Smith"
	},
  ...
]

```

### Get Event Details

Retrieve details of a specific event by its ID.

```
GET /api/events/{event_id}/

```

Example Response:

```json
	{
		"id": 1,
		"title": "Django Confrence",
		"description": "Join us for a keynote speech on saturday!",
		"location": "123 Main Street, Gotham",
		"start_date": "2023-09-24",
		"end_date": "2023-09-24",
		"start_time": "3:00 PM",
		"end_time": "5:00 PM",
		"thumbnail": "<https://example.com/thumbnail-party.jpg>",
		"creator": "John Doe"
	}

```

### Create an Event

Create a new event by providing the required parameters.

```
POST /api/events/

Request Body:
	{
		"title": "New Event",
		"description": "Event description",
		"location": "123 Location Street, Freetown",
		"start_date": "2023-09-24",
		"end_date": "2023-09-24",
		"start_time": "3:00 PM",
		"end_time": "5:00 PM",
		"thumbnail": "<https://example.com/thumbnail.jpg>",
		"creator": "John Doe"
	}

```

Example Response:

```json
{
	"id": 3,
	"title": "New Event",
	"description": "Event description",
	"location": "123 Location Street, Freetown",
	"start_date": "2023-09-24",
	"end_date": "2023-09-24",
	"start_time": "3:00 PM",
	"end_time": "5:00 PM",
	"thumbnail": "<https://example.com/thumbnail.jpg>",
	"creator": "John Doe"
}

```

### Update an Event

Update the details of an existing event by its ID.

```
PUT /api/events/{event_id}/

Request Body:
{
  "title": "Updated Event",
	"start_date": "2023-09-28",
	"end_date": "2023-09-29",
  "location": "Location 4",
	"start_time": "6:00 PM",
	"end_time": "8:00 PM"
}

```

Example Response:

```json
{
  "id": 3,
  "title": "Updated Event",
	"description": "Event description",
	"location": "Location 4",
	"start_date": "2023-09-28",
	"end_date": "2023-09-29",
	"start_time": "6:00 PM",
	"end_time": "8:00 PM",
	"thumbnail": "<https://example.com/thumbnail-party.jpg>"
}

```

### Delete an Event

Delete an existing event by its ID.

```
DELETE /api/events/{event_id}/

```

No response body is returned for this request.

These examples demonstrate the basic usage of the WetinDeySup API for retrieving, creating, updating, and deleting events.

## Groups

### Get All Groups

Retrieve all events from the API.

```
GET /api/groups/

```

Example Response:

```json
[
	{
		"id": "1",
		"title": "Group Title 1",
		"creator_id": "1"
	},
	{
		"id": "2",
		"title": "Group Title 2",
		"creator_id": "2"
	}
  ...
]

```

### Get Group Details

Retrieve details of a specific group by its ID.

```
GET /api/groups/{group_id}/

```

Example Response:

```json
	{
		"id": "3",
		"title": "Group Title 3",
		"creator_id": "1"
	}

```

### Create a Group

Create a new group by providing the required parameters.

```
POST /api/groups/

Request Body:
	{
	  "id": 3,
		"title": "New Group",
		"creator_id": "1"
	}

```

Example Response:

```json
{
  "id": 3,
  "title": "New Group",
	"created_at": "",
	"updated_at": "",
	"creator_id": "1"
}

```

### Update a Group

Update the details of an existing group by its ID.

```
PUT /api/groups/{group_id}/

Request Body:
{
	"id": "3",
  "title": "Updated Group",
	"creator_id": "1"
}

```

Example Response:

```json
{
  "id": 3,
  "title": "Updated Group",
	"created_at": "",
	"updated_at": "",
	"creator_id": "1"
}

```

### Delete a Group

Delete an existing group by its ID.

```
DELETE /api/groups/{group_id}/

```

No response body is returned for this request.

These examples demonstrate the basic usage of the WetinDeySup API for retrieving, creating, updating, and deleting groups.

## Group Images

### Get All Group Images

Retrieve all group images from the API.

```
GET /api/group-images/

```

Example Response:

```json
[
	{
		"id": 1,
		"group": "Group Name 1",
		"image": "<https://example.com/group-1.jpg>"
	},
	{
		"id": 2,
		"group": "Group Name 2",
		"image": "<https://example.com/group-2.jpg>"
	},
  ...
]

```

### Get Group Image Details

Retrieve details of a specific group image by its ID.

```
GET /api/group-images/{groupimage_id}/

```

Example Response:

```json
	{
		"id": 1,
		"group": "Group Name 1",
		"image": "<https://example.com/group-1.jpg>"
	}

```

### Create a Group Image

Create a new group image by providing the required parameters.

```
POST /api/group-images/

Request Body:
	{
		"group": "New Group",
		"image": "<https://example.com/new-group.jpg>"
	}

```

Example Response:

```json
{
  "id": 3,
	"group": "New Group",
	"image": "<https://example.com/new-group.jpg>"
}

```

### Update a Group Imae

Update the details of an existing g by its ID.

```
PUT /api/group-images/{groupimage_id}/

Request Body:
	{
	  "id": 3,
		"group": "Updated Group",
		"image": "<https://example.com/updated-group.jpg>"
	}

```

Example Response:

```json
{
  "id": 3,
  "title": "Updated Group",
	"created_at": "",
	"updated_at": "",
	"image": "<https://example.com/updated-group.jpg>"
}

```

### Delete a Group Image

Delete an existing group image by its ID.

```
DELETE /api/group-images/{groupimage_id}/

```

No response body is returned for this request.

These examples demonstrate the basic usage of the WetinDeySup API for retrieving, creating, updating, and deleting group images.

## Group Events

### Get All Group Events

Retrieve all group events from the API.

```
GET /api/groupevents/

```

Example Response:

```json
[
	{
		"id": 1,
		"event": 1,
		"group": "Group Name 1"
	},
	{
		"id": 2,
		"event": 2,
		"group": "Group Name 2"
	},
  ...
]

```

### Get Group Event Details

Retrieve details of a specific group event by its ID.

```
GET /api/groupevents/{groupevent_id}/

```

Example Response:

```json
{
	"id": 3,
	"event": 3,
	"group": "Group Name 3"
}

```

### Create a Group Event

Create a new group event by providing the required parameters.

```
POST /api/group-images/

Request Body:
	{
		"event": 4,
		"group": "New Group"
	}

```

Example Response:

```json
{
  "id": 4,
	"event": 4,
	"group": "New Group"
}

```

### Update a Group Event

Update the details of an existing group event by its ID.

```
PUT /api/groupevents/{groupevent_id}/

Request Body:
	{
		"event": 5,
		"group": "Updated Group",
	}

```

Example Response:

```json
	{
	  "id": 4,
		"event": 5,
		"group": "Updated Group",
	}

```

### Delete a Group Event

Delete an existing group event by its ID.

```
DELETE /api/groupevents/{groupevent_id}/

```

No response body is returned for this request.

These examples demonstrate the basic usage of the WetinDeySup API for retrieving, creating, updating, and deleting group events.

## Images

### Get All Images

Retrieve all images from the API.

```
GET /api/images/

```

Example Response:

```json
[
	{
		"id": "1",
		"url": "<https://example.com/image-1.jpg>"
	},
	{
		"id": "2",
		"url": "<https://example.com/image-2.jpg>"
	},
  ...
]

```

### Get Image Details

Retrieve details of a specific image by its ID.

```
GET /api/images/{image_id}/

```

Example Response:

```json
	{
		"id": "3",
		"url": "<https://example.com/image-3.jpg>"
	}

```

### Create an Image

Create a new image by providing the required parameters.

```
POST /api/images/

Request Body:
	{
		"id": "3",
		"url": "<https://example.com/new-image.jpg>"
	}

```

Example Response:

```json
{
	"id": "3",
	"url": "<https://example.com/new-image.jpg>"
}
```

### Update an Image

Update the details of an existing image by its ID.

```
PUT /api/images/{image_id}/

Request Body:
	{
		"id": "3",
		"url": "<https://example.com/updated-image.jpg>"
	}

```

Example Response:

```json
	{
		"id": "3",
		"url": "<https://example.com/updated-image.jpg>"
	}

```

### Delete an Image

Delete an existing image by its ID.

```
DELETE /api/images/{image_id}/

```

No response body is returned for this request.

These examples demonstrate the basic usage of the WetinDeySup API for retrieving, creating, updating, and deleting images.

## Likes

### Get All Likes

Retrieve all likes from the API.

```
GET /api/likes/
```

Example Response:

```json
[
	{
		"id": 1,
		"user": {
							"id": 1,
							"name": "John Doe",
							"email": "john@mail.com",
							"avatar": "",
							"created_at": "",
							"updated_at": ""
						},
		"comment": {
							"id": 1,
							"body": "Comment 1",
							"creator": "John Doe",
							"event": 1
						}
	},
	{
		"id": 2,
		"user": {
							"id": 2,
							"name": "James Smith",
							"email": "james@mail.com",
							"avatar": "",
							"created_at": "",
							"updated_at": ""
						},
		"comment": {
							"id": 2,
							"body": "Comment 2",
							"creator": "John Doe",
							"event": 2
						}
	},
  ...
]

```

### Get Like Details

Retrieve details of a specific like by its ID.

```
GET /api/images/{like_id}/

```

Example Response:

```json
	{
		"id": 3,
		"user": {
							"id": 3,
							"name": "James Smith",
							"email": "james@mail.com",
							"avatar": "",
							"created_at": "",
							"updated_at": ""
						},
		"comment": {
							"id": 3,
							"body": "Comment 2",
							"creator": "John Doe",
							"event": 3
						}
	}
```

### Like a Comment

Create a new image by providing the required parameters.

```
POST /api/likes/

Request Body:
	{
		"comment_id": 4,
	}

```

Example Response:

```json
	{
		"id": 4,
		"user": {
							"id": 4,
							"name": "James Smith",
							"email": "james@mail.com",
							"avatar": "",
							"created_at": "",
							"updated_at": ""
						},
		"comment": {
							"id": 4,
							"body": "Comment 2",
							"creator": "John Doe",
							"event": 4
						}
	}
```

## User Groups

### Get All User Groups

Retrieve all user groups from the API.

```
GET /api/usergroups/

```

Example Response:

```json
[
	{
		"id": 1,
		"user": "John Doe",
		"group": "Group 1"
	},
	{
		"id": 2,
		"user": "James Smith",
		"group": "Group 2"
	},
  ...
]

```

### Get User Group Details

Retrieve details of a specific user group by its ID.

```
GET /api/usergroups/{usergroup_id}/

```

Example Response:

```json
	{
		"id": 3,
		"user": "Emily Davis",
		"group": "Group 3"
	}
```

### Create a User Group

Create a new user group by providing the required parameters.

```
POST /api/usergroups/

Request Body:
	{
		"user": "Robert Johnson",
		"group": "Group 4"
	}

```

Example Response:

```json
{
	"id": 4,
	"url": "<https://example.com/new-image.jpg>"
}
```

### Update an Image

Update the details of an existing image by its ID.

```
PUT /api/images/{image_id}/

Request Body:
	{
		"id": "3",
		"url": "<https://example.com/updated-image.jpg>"
	}

```

Example Response:

```json
	{
		"id": "3",
		"url": "<https://example.com/updated-image.jpg>"
	}

```

### Delete an Image

Delete an existing image by its ID.

```
DELETE /api/images/{image_id}/

```

No response body is returned for this request.

These examples demonstrate the basic usage of the WetinDeySup API for retrieving, creating, updating, and deleting images.