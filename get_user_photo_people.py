import os
import base64
import googleapiclient.discovery
from google.oauth2 import service_account

# Specify the user to impersonate
USER_EMAIL_TO_IMPERSONATE = 'targetaccountphoto@example.com'

# Set the full path to the credentials JSON file
CREDENTIALS_PATH = r'C:\Users\User\Downloads\service_account_creds.json'

# Set up credentials
credentials = service_account.Credentials.from_service_account_file(
    CREDENTIALS_PATH, 
    scopes=['https://www.googleapis.com/auth/userinfo.profile']
).with_subject(USER_EMAIL_TO_IMPERSONATE)

# Create the People API client
service = googleapiclient.discovery.build('people', 'v1', credentials=credentials)

# Call the API to retrieve the user's photo
response = service.people().get(
    resourceName='people/me',
    personFields='photos'
).execute()

# Get the photo URL from the response
photo_url = response.get('photos', [{}])[0].get('url')

# Download the photo and save it to the file system
if photo_url:
    photo_url = photo_url + '?=s0-c'
    import urllib.request
    photo_file_path = os.path.join(os.path.dirname(CREDENTIALS_PATH), 'user_photo.jpg')
    urllib.request.urlretrieve(photo_url, photo_file_path)
    print(f'Photo saved at: {photo_file_path}')
else:
    print('No photo found for the user.')
