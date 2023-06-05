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
    "middle_name": "",
    "last_name": "TANK",
    "company_name": "",
    "house_flat_no": "",
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
    "doc_img[]": "img_file_path",
    "room_no": "305",
    "checkin_date": "03-06-2023",
    "checkin_time": "14:00",
    "checkout_date": "04-06-2023",
    "checkout_time": "12:00",
    "child": "0",
    "adult": "3",
    "vehicle_type": "Other",
    "vehicle_registration_no": "",
    "other_full_name[]": "Dipti Tank",
    "other_full_name[]": "Rashila Tank",
    "other_mobile_number[]": "9820355183",
    "other_mobile_number[]": "9820355183",
    "other_doc_type[]": "aadhar card",
    "other_doc_type[]": "aadhar card",
    "other_document_number[]": "641263563311",
    "other_document_number[]": "219510572201",
    "action": "Add"
}
```

*Note: All parameters with "Required" in the description must be filled with the correct data, while those with "Disabled" can be empty.*

#### Request Body Parameters (Each can be have String input unless specified):

- `first_name` (Required): The first name of the person.
- `middle_name`: The middle name of the person.                                            # This parameter can be empty.
- `last_name` (Required): The last name of the person.
- `company_name`: The name of the company (if any).                                        # This parameter can be empty.
- `house_flat_no`: The House/ Flat Number of the address.                                  # This parameter can be empty.
- `address` (Required): The complete address of the person.
- `locality` (Required): The locality of the person's address.
- `city` (Required): The city of the person's address.
- `district` (Required): The district of the person's address.
- `zip_code` (Required): The ZIP code of the person's address.
- `country` (Required): The country of the person's address.                                # Lower Case necessary. Default "india"
- `state` (Required): The state of the person's address.                                    # Lower Case necessary. Default "gujarat"
- `dob` (Required): The date of birth of the person in the format "dd-mm-yyyy".
- `mobile_no` (Required): The mobile number of the person.                                  # Should be of 10 to 13 digits
- `phone_no` (Required): The phone number of the person.                                    # Should be of 10 to 13 digits
- `email` (Required): The email address of the person.                                      # Should be a proper mail id, i.e. should have @ & domain (.co/.com/.in etc)
- `coming_from` (Required): The place the person is coming from.                            # City where the person is coming from. Can be same as address.
- `going_to` (Required): The place the person is going to.                                  # City where the person is coming from. Can be same as address.
- `doc_type` (Required): The type of document provided by the person.                       # It can take the following values: "aadhar card", "election card", "driving license", "pan card", "passport no".
- `doc_no` (Required): The document number of the person.                                   # Minimum length is 5
- `doc_img[]` (Required): IT IS THE ONLY **FILE TYPE INPUT**. FILE SIZE SHOULD NOT EXCEED 250kb. FILE TYPE - PNG/ JPEG/ GIF
- `room_no` (Required): The room number of the person.
- `checkin_date` (Required): The check-in date in the format "dd-mm-yyyy".
- `checkin_time` (Required): The check-in time in the format "hh:mm".
- `checkout_date` (Required): The checkout date in the format "dd-mm-yyyy".
- `checkout_time` (Required): The checkout time in the format "hh:mm".
- `child` (Required): The number of children staying.
- `adult` (Required): The number of adults staying.
- `vehicle_type` (Required): The type of vehicle.
- `vehicle_registration_no`: The registration number of the vehicle.                          # This parameter can be empty.
- `other_full_name[]` (Required): A list of other full names associated with the booking.
- `other_mobile_number[]` (Required): A list of other mobile numbers associated with the booking.
- `other_doc_type[]` (Required): A list of other document types associated with the booking. Each value should match exactly with one of these strings: "aadhar card", "election card", "driving license", "pan card", "passport no".
- `other_document_number[]` (Required): A list of other document numbers associated with the booking.
- `action` (Required): The action to perform. Currently supports "Add".                      # Always constant "Add"

The `doc_type` can take the following values:
- "aadhar card"
- "election card"
- "driving license"
- "pan card"
- "passport no"
It must match exactly with one of these strings.

All array type arguments can have multiple inputs in the form of:
``` json
{
    "other_full_name[]": "Dipti Tank",
    "other_full_name[]": "Rashila Tank",
    "other_mobile_number[]": "9820355183",
    "other_mobile_number[]": "9820355183",
    "other_doc_type[]": "aadhar card",
    "other_doc_type[]": "aadhar card",
    "other_document_number[]": "641263563311",
    "other_document_number[]": "219510572201",
}
```
***Note:*** 
The 4 parameters namely:
- other_full_name[]
- other_mobile_number[]
- other_doc_type[]
- other_document_number[]
should have the exact number of inputs each i.e. one less than number of adults.
*For the above example the number of adults was 3 so each parameter had 2 inputs.*


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
