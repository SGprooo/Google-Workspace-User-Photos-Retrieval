import os
import base64
from google.oauth2 import service_account
import googleapiclient.discovery

def get_user_photo(user_key):
    # Set the full path to the credentials JSON file
    credentials_path = r'C:\Users\User\Downloads\service_account_creds.json'

    # Set up credentials
    credentials = service_account.Credentials.from_service_account_file(
        credentials_path,
        scopes=['https://www.googleapis.com/auth/admin.directory.user.readonly']
    )

    # Specify the email address of the user to impersonate
    impersonated_user_email = 'user@example.com'  # Replace with the email of the user you want to impersonate
    credentials = credentials.with_subject(impersonated_user_email)

    # Create the Admin SDK API client
    service = googleapiclient.discovery.build('admin', 'directory_v1', credentials=credentials)

    # Call the API to retrieve the user's photo
    response = service.users().photos().get(userKey=user_key).execute()

    # Process the response
    photo_data = response['photoData']
    
    # Convert the web-safe base64 encoded string to standard base64
    standard_base64 = photo_data.replace('_', '/').replace('-', '+').replace('*', '=').replace('.', '=')

    # Decode the Base64 string
    photo_bytes = base64.b64decode(standard_base64)

    # Save the photo in the same directory as the credentials JSON file copilo
    photo_file_path = os.path.join(os.path.dirname(credentials_path), 'user_photo.jpg')
    with open(photo_file_path, 'wb') as photo_file:
        photo_file.write(photo_bytes)

    return photo_file_path

# Replace '' with the actual user key
user_key = 'user@example.com'
photo_file_path = get_user_photo(user_key)
print(f"Photo saved at: {photo_file_path}")
