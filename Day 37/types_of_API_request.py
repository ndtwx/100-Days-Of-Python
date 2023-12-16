"""
TYPES OF HTTP REQUESTS
-----------------------
GET = requests.get()
- Ask an external system for a  particular data and they give that to us in the response

POST = requests.post()
- We give the external system some piece of data but not so interested in the response
  other than whether it is successful or not
- Example:
    1.Using Google Sheets API to save data into google sheets
    2.Using Twitter API to post a tweet

PUT = requests.put()
- Update a piece of data in the external service.
- Example:
    1. Update existing data in the Google sheet

DELETE = requests.delete()
- Delete a piece of data in the external service
"""