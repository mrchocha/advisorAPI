# advisorAPI
api to perform various tasks with jwt authentication facility.

# Table of Content
- Api Endpoint
- Tools & Technology used
- Functionality
- Postman Collection Link



# Api Endpoint
```
https://advisorapiassignment.herokuapp.com
```

# Tools & Technology used
- Django
- Django REST framework
- simplejwt

# Functionality

### Add Advisor

```
POST https://advisorapiassignment.herokuapp.com/admin/advisor
```
body should have `name` and `photo_url`
response will be status.

i.e.
```
status: 200
```


### Register User

```
POST https://advisorapiassignment.herokuapp.com/user/register
```
body should have `email` , `name` and `password`
response will be status, `user_id` and  `token`.

i.e.
```
status: 200
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIwMzIxODIwLCJqdGkiOiI5ZmQ0YTdlM2Q5NWQ0NzYyOGIyOGE3NWIxMTg0Zjc3NSIsInVzZXJfaWQiOjExfQ.PDi25DTCUBRFOLehTRcn0Kvav_FGKLfF6_WDu_BxaI0",
    "user_id": 11
}
```

### Login User
```
POST https://advisorapiassignment.herokuapp.com/user/login
```
body should have `email` and `password`
response will be status, `user_id` and  `token`.

i.e.
```
status: 200
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjIwMzIyNjgzLCJqdGkiOiIwZjJjNTQ5MzA1YzE0NWYzOTdhYjJlMzNmYWQyNDBjYiIsInVzZXJfaWQiOjExfQ.YMk14SpT_CmKLR6XqZOmKth-CJ1NYJtVeAZmXceK1iU",
    "user_id": 11
}

```
### Get Advisor List
```
GET https://advisorapiassignment.herokuapp.com/user/<user_id>/advisor
```
header should have `Authorization` token
response will be status, `id`, `advisor_name` and `advisor_photo_url`.

i.e.
```
status: 200
[
    {
        "id": 5,
        "advisor_name": "Ramesh",
        "advisor_photo_url": "https://avatars.githubusercontent.com/u/49686817?s=400&u=1548b92cc58e8021cf612cffaae6341264a7c57a&v=4"
    },
    {
        "id": 6,
        "advisor_name": "pathik",
        "advisor_photo_url": "https://avatars.githubusercontent.com/u/50065408?v=4"
    }
]

```
### Book Advisor Meeting
```
POST https://advisorapiassignment.herokuapp.com/user/<user_id>/advisor/<advisor_id>
```
header should have `Authorization` token
body should have `booking_time`
response will be status.

i.e.
```
status 200
```

### List of all Bookings
```
GET https://advisorapiassignment.herokuapp.com/user/<user_id>/advisor/booking
```
header should have `Authorization` token
response will be status `advisor_name`, `advisor_profile_pic`, `advisor_id`, `booking_time`, `booking_id`

i.e.
```
[
    {
        "advisor_name": "Ramesh",
        "advisor_profile_pic": "https://avatars.githubusercontent.com/u/49686817?s=400&u=1548b92cc58e8021cf612cffaae6341264a7c57a&v=4",
        "advisor_id": 5,
        "booking_time": "2021-05-21T10:00:00Z",
        "booking_id": 4
    }
]
```


# Postman Collection Link
please go [here](https://www.getpostman.com/collections/7c825310b3fd61b6a8ba)