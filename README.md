# Documentation for the Pathik Website Data API

## Overview

This API is created for the Fern Hotel Rajkot to automatically upload and send data to the Pathik Website maintained by the Gujarat Government. The API is compatible with Innkeyys PMS. 

The base URL for all endpoints is: 
```
https://fastapi-production-04fb.up.railway.app/
```

## Endpoints

### 1. /upload

This endpoint is used to upload the data to the Pathik Website.

#### HTTP Method

POST

#### URL

```
https://fastapi-production-04fb.up.railway.app/upload
```

#### Request Headers

No headers are required for this API.

#### Request Body

The request body should contain a JSON object with a structure matching the following example:

```json
{
    "first_name": "SANJAY",
    "last_name": "TANK",
    "address": "702 Manisha Elite CHCL, Junction Of P.K. Road and VP Road, Near to Aditi Hospital, Mumbai, Mumbai Suburban, Maharashtra, 400080",
    "locality": "Mumbai",
    "city": "Mumbai",
    "district": "Mumbai",
    "zip_code": "400080",
    "country": "india",
    "state": "maharashtra",
    "dob": "30-11-1984",
    "mobile_no": "9820355183",
    "phone_no": "9820355183",
    "email": "saanjay3011@gmail.com",
    "coming_from": "Mumbai",
    "going_to": "Mumbai",
    "doc_type": "aadhar card",
    "doc_no": "950472452856",
    "doc_img": ["img_file_path"],
    "room_no": "305",
    "checkin_date": "03-06-2023",
    "checkin_time": "14:00",
    "checkout_date": "04-06-2023",
    "checkout_time": "12:00",
    "child": "0",
    "adult": "3",
    "vehicle_type": "Other",
    "vehicle_registration_no": "",
    "other_full_name": ["Dipti Tank", "Rashila Tank"],
    "other_mobile_number": ["9820355183", "9820355183"],
    "other_doc_type": ["aadhar card", "aadhar card"],
    "other_document_number": ["641263563311", "219510572201"],
    "action": "Add"
}
```

*Note: All parameters with "Required" in the description must be filled with the correct data, while those with "Disabled" can be empty.*

The `doc_type` can take the following values:
- "aadhar card"
- "election card"
- "driving license"
- "pan card"
- "passport no"

It must match exactly with one of these strings.

The `doc_img` should be a list of paths to the relevant document images. 

#### Responses

**Success:**

HTTP Status Code: 200

```json
{
    "message": "Files uploaded successfully"
}
```

## Errors

In case of any errors, the API will respond with the corresponding HTTP status code and a message providing additional information about the error. For example:

HTTP Status Code: 400

```json
{
    "message": "Invalid request data"
}
```

## Rate Limiting

There are currently no rate limits for this API. 

## Further Assistance

For further assistance or additional questions, please contact the API support team.
